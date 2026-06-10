# Dagor Asset Explorer — 代码审查与改进清单

> 审查日期：2026-06-10

---

## 目录

1. [项目概况](#1-项目概况)
2. [P0 — 功能性 Bug & 崩溃风险](#2-p0--功能性-bug--崩溃风险)
3. [P1 — 性能问题（卡顿的直接原因）](#3-p1--性能问题卡顿的直接原因)
4. [P2 — 架构与工程质量](#4-p2--架构与工程质量)
5. [P3 — 功能缺口与路线图建议](#5-p3--功能缺口与路线图建议)
6. [依赖升级记录](#6-依赖升级记录)
7. [PySide6 迁移评估](#7-pyside6-迁移评估)
8. [附录：文件级改动清单](#8-附录文件级改动清单)

---

## 1. 项目概况

| 项目 | 说明 |
|------|------|
| **名称** | Dagor Asset Explorer (DAE) |
| **用途** | 浏览和导出 Dagor 引擎游戏（《战争雷霆》《从军》等）的 3D 资源 |
| **语言** | Python 3 + C（SSE intrinsics DLL） |
| **GUI** | PyQt5 |
| **规模** | ~5,000 行 Python，13 个 ImHex pattern 文件，5 个 `.ui` 布局 |
| **状态** | 单人业余项目，最后更新 2021 年 10 月 |
| **总提交** | 20 次 |

**核心功能已可用**：GRP/DXP/DBLD 解析，OBJ/DMF/Source 引擎导出，地图布局导出。不存在死代码，是一个有实际价值的工具。

---

## 2. P0 — 功能性 Bug & 崩溃风险

### 2.1 Worker 线程非法操作 Qt GUI

| 项目 | 内容 |
|------|------|
| **位置** | `src/dae/gui/app.py:385-423`（`MapLoadThread.run` / `MapExportThread.run`） |
| **严重性** | 🔴 硬崩溃（segfault） |
| **现象** | 多线程操作 Widget 时随机崩溃，无 Python traceback |
| **根因** | Qt 要求 GUI 对象只能在主线程访问。`QRunnable.run()` 中直接调用 `mainWindow.setRequestedDialog()`、`mainWindow.setTaskStatus()`、`mainWindow.setTaskTitle()` 等，绕过 Qt 线程亲和性 |
| **修复方案** | worker 线程改为通过 `pyqtSignal` 发射进度信息，主线程连接信号到 UI 更新槽 |

### 2.2 ctypes 调用无边界保护

| 项目 | 内容 |
|------|------|
| **位置** | `src/dae/parse/dbld.py:20-24`（以及所有 ctypes 调用点） |
| **严重性** | 🔴 硬崩溃（segfault） |
| **现象** | 传错指针或拿到空指针 → Python 解释器直接崩溃 |
| **根因** | C 函数指针（`get_v482`）未设置 `.argtypes` / `.restype`，无返回值检查，无异常包装 |
| **修复方案** | 为每个 ctypes 函数显式声明 argtypes/restype，包装为抛出 `RuntimeError` 的安全 Python 函数 |

### 2.3 SafeRange 迭代器逻辑错误

| 项目 | 内容 |
|------|------|
| **位置** | `src/dae/util/terminable.py:52` |
| **严重性** | 🔴 数据损坏 / 越界读取 |
| **现象** | 反向步长时不正确；终止条件 `self.cur >= self.val1 or self.cur < self.val2` 有 off-by-one |
| **根因** | 手工实现 range 语义但用了错误的不等式方向，尤其是负步长时 `val1`/`val2` 赋值分支隐晦 |
| **修复方案** | 内部直接包装 `range(start, stop, step)` + 每次迭代检查 `parent.shouldTerminate`，去掉手工状态管理 |

### 2.4 BinFile / BinBlock 继承链错误

| 项目 | 内容 |
|------|------|
| **位置** | `src/dae/util/fileread.py:17-189` |
| **严重性** | 🔴 隐蔽崩溃 |
| **现象** | 第三方库做 `isinstance(obj, io.BufferedReader)` 时触发 C 层未初始化状态错误 |
| **根因** | `BinFile` 错误 `class BinFile(BufferedReader)` 但覆盖 `__init__` 不调 `super()`；`BinBlock` 继承 `BinFile` 也不调 `super()` |
| **修复方案** | 改为组合模式：`BinFile` 包裹内部 `bytes` 对象实现 `read()/seek()/tell()`，不继承 `BufferedReader` |

### 2.5 碰撞模型导出偏移

| 项目 | 内容 |
|------|------|
| **位置** | `src/dae/parse/realres.py`（CollisionGeom 相关） |
| **严重性** | 🔴 功能缺陷 |
| **现象** | 导出的碰撞模型坐标偏移 |
| **根因** | README 标注已知问题，可能与 SSE intrinsics 的坐标变换或引擎坐标系映射（Y-up vs Z-up）有关 |
| **修复方案** | 排查 `dae_intrinsics.c` 中的 `get_v482` 变换逻辑及相关矩阵乘法代码 |

---

## 3. P1 — 性能问题（卡顿的直接原因）

### 3.1 右键菜单触发主线程重型解析

| 项目 | 内容 |
|------|------|
| **位置** | `src/dae/gui/customtreeview.py:94` |
| **严重性** | 🟠 UI 冻结 300ms~数秒 |
| **现象** | 右键点击 RendInst/DynModel 资产时界面卡死 |
| **根因** | `populateMenu()` 中调用 `asset.computeData()` 在主线程同步执行：解压缩 → 解析顶点缓冲区 → 读取面索引。且**每次右键都重复执行** |
| **修复方案** | 改为延迟计算或缓存结果，仅在导出操作时触发 `computeData()`；右键菜单仅读取已缓存的元数据（LOD 数量等） |

### 3.2 资产挂载时全量解析（无懒加载）

| 项目 | 内容 |
|------|------|
| **位置** | `src/dae/gui/app.py:275` |
| **严重性** | 🟠 启动耗时 30s~数分钟 |
| **现象** | 打开游戏根目录后长时间无响应 |
| **根因** | `exploreFileInfo()` 递归遍历所有文件，对每个 `.grp` 调用 `AssetManager.initializeAsset()` 立即完成全部解析 |
| **修复方案** | 实现懒加载：Tree Item 展开时才解析对应资产；或至少分批延迟初始化 |

### 3.3 Packed.getBin() 无缓存策略

| 项目 | 内容 |
|------|------|
| **位置** | `src/dae/util/terminable.py:231-241` |
| **严重性** | 🟠 大量重复磁盘 I/O |
| **现象** | 批量导出/多次访问 GRP 子文件时慢 |
| **根因** | 每次调用 `getBin()` 都 `open().read()` 同一文件。`setCachedBinFile()` 仅在显式调用后生效，大部分代码路径未调用 |
| **修复方案** | 在 `Pack.enableCaching()` 之后自动设置子文件缓存；或默认缓存第一次读取结果 |

### 3.4 内存泄漏 → 长期使用后 GC 卡顿

| 项目 | 内容 |
|------|------|
| **位置** | `src/dae/gui/customtreeview.py:34,44-46` |
| **严重性** | 🟠 使用越久越卡 |
| **现象** | 长时间浏览后界面逐渐变慢 |
| **根因** | `SafeStandardItem.setParentItem()` 中的 lambda 闭包 `lambda: self.clearData()` 捕获 `self`，产生循环引用。源码注释确认：「WARNING: if the data is not cleared manually, this will lead to memory leaks (fuck qt for that)」。同时每个资产创建 3 个 `QStandardItem`，对象数随加载增长 |
| **修复方案** | 使用 `functools.weakref` 或明确的生命周期管理替代 lambda 闭包 |

### 3.5 AssetCacher 无容量限制

| 项目 | 内容 |
|------|------|
| **位置** | `src/dae/util/assetcacher.py` |
| **严重性** | 🟠 长期内存膨胀 |
| **现象** | 浏览大量资产后内存占用持续增长 |
| **根因** | 缓存只有 `cacheAsset()` 无淘汰机制；`getModelTextures()` 等每次 O(n) 线性遍历所有 GameResDesc |
| **修复方案** | 添加 LRU 淘汰 + 最大容量限制；GameResDesc 索引改用 `dict` 直接查找而非遍历 |

### 3.6 Python 层面的向量运算

| 项目 | 内容 |
|------|------|
| **位置** | `src/dae/parse/realres.py:110-127` |
| **严重性** | 🟡 大规模顶点处理慢 |
| **现象** | 高精度模型导出时 CPU 占用高 |
| **根因** | `subVert()` / `crossProduct()` / `normalize()` 用纯 Python 元组实现，每次创建新对象 |
| **修复方案** | 向量运算改用 `list` 或 `numpy`（如体积可接受）；或至少复用临时变量 |

---

## 4. P2 — 架构与工程质量

### 4.1 上帝类

| 文件 | 行数 | 内含 |
|------|------|------|
| `src/dae/parse/realres.py` | 2,174 | RendInst、DynModel、SkinnedMesh、GeomNodeTree、CollisionGeom、FX、AnimChar、PhysObj、LandClass、RandomGrass **以及**所有导出逻辑（OBJ、DMF、SMD/QC/VMT/VTF） |
| `src/dae/gui/customtreeview.py` | 1,042 | QTreeView、TreeModel、菜单、导出 Action、VTF 转换、文件操作 |
| `src/dae/parse/dbld.py` | 1,118 | DBLD 解析 + RIGen + LandMesh + 碰撞数据 + 高度图 |

**建议拆分**：
```
src/dae/
├── parse/           # 纯解析（数据类）
│   ├── realres/
│   │   ├── rendinst.py
│   │   ├── dynmodel.py
│   │   ├── skeleton.py
│   │   ├── collision.py
│   │   └── animchar.py
│   └── ...
├── export/          # 导出（纯函数，无 GUI 依赖）
│   ├── obj.py
│   ├── dmf.py
│   ├── source.py
│   └── dpl.py
├── gui/             # GUI 组件
│   ├── app.py
│   ├── treeview.py
│   ├── actions/     # 菜单 Action 类
│   └── ...
```

### 4.2 `sys.path.append` 污染

| 位置 | 说明 |
|------|------|
| 几乎所有 `.py` 文件顶部 | `sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))` |
| `src/dae/__main__.py:4-8` | 注释掉的旧 path hack |

**修复**：使用 `python -m dae` 启动，所有导入改用相对导入（`from .parse import realres`）。

### 4.3 无单元测试

| 现状 | 风险 |
|------|------|
| 0 个测试文件 | 二进制解析器高度依赖输入格式，改一行可能破坏多种格式 |

**建议**：为核心解析函数添加 pytest 用例（用少量匿名化的二进制片段验证返回值结构）。

### 4.4 无类型注解

当前 ~5,000 行 Python 中极少使用 `typing` 模块。二进制解析器的输入输出类型不明确，调试和重构困难。

### 4.5 依赖版本固化且过时

| 依赖 | 当前版本 | 问题 |
|------|----------|------|
| PyQt5 | 5.15.9 | 2021 年版本，可能存在安全漏洞 |
| Pillow | 10.0.0 | 2023 年版本 |
| zstandard | 0.15.1 | 2021 年版本 |
| Requests | 2.31.0 | 实际未使用 |

### 4.6 代码卫生

- 大量注释掉的代码块（`customtreeview.py:83,126`；`app.py:4-8,176`；`assetcacher.py:89-116` 等）
- `format_exc()` 被当作常规错误处理（应统一改为 logging）
- Tab/空格混用（部分文件）
- `broad Except` 吞掉具体异常信息
- `type(data) == str` 而非 `isinstance()` 检查（`fileread.py:19`）

### 4.7 无 CI/CD

每次发布需手动：
1. `pyinstaller -F -n DagorAssetExplorer`
2. `gcc -shared dae_intrinsics.c -o dae_intrinsics.dll`

**建议**：添加 GitHub Actions 自动构建 + 发布 Release。

---

## 5. P3 — 功能缺口与路线图建议

### 5.1 已知功能缺失

| 功能 | 状态 | 说明 |
|------|------|------|
| 3D 模型预览 | UI 已定义（`preview.ui`），代码未实现 | `PreviewModel` 类存在但 `run()` 为空 |
| 音效导出 | 曾实现后移除 | README：「lacked the courage to add it back」 |
| 动画导出 | `AnimChar` 类已定义，无导出逻辑 | |
| 物理数据导出 | `PhysObj` 类已定义，无导出逻辑 | |
| Blender 插件 | 依赖外部 repo | [Dagor-Asset-Explorer-Tools](https://github.com/Gredwitch/Dagor-Asset-Explorer-Tools) 需维护 |
| 碰撞模型偏移 | README 标注已知 Bug | 见 §2.5 |

### 5.2 GRP3 格式未支持

| 项目 | 内容 |
|------|------|
| **位置** | `src/dae/parse/gameres.py`（GameResourcePack 解析） |
| **严重性** | 🟡 功能缺口 |
| **现象** | 新版 Dagor 游戏改用 GRP3 格式，头部魔法字与当前支持的 GRP2 不同，工具无法识别和打开 |
| **根因** | 当前仅实现了 GRP2 格式解析，GRP3 格式为后续版本的容器格式，布局和索引机制可能有变化 |
| **修复方案** | 从新版游戏中提取 GRP3 样本，比对二进制头部差异，研究 ImHex 模式文件后扩充解析逻辑 |

### 5.3 中文本地化

| 项目 | 内容 |
|------|------|
| **位置** | 全局 — 所有 GUI 字符串硬编码为英文 |
| **严重性** | 🟢 可增强 |
| **现状** | 菜单、按钮、状态提示、错误信息共约 60-80 处英文硬编码字符串，无本地化机制 |
| **需求评估** | 用户群（Dagor 模组社区）以英文为主，多语言不是刚需。但开发者本人使用中文，工具支持中文界面可提升使用体验 |
| **建议方案** | 轻量方案：不引入 `.ts`/`.po` 完整 gettext 管线。用 `QObject.tr()` 标记所有用户可见字符串，搭配一个 `_zh.py` 字典文件做运行时替换。英文保持为 fallback |
| **工作量** | 0.5 天 |

### 5.4 优先级路线图

```
Phase 1 — 稳定化（P0）
  ├─ 修复 ctypes 安全性
  ├─ 修复线程安全（GUI 操作移到主线程）
  ├─ 修复 SafeRange 迭代器
  └─ 重写 BinFile/BinBlock 继承

Phase 2 — 可用性（P1）
  ├─ 移除右键菜单中的 computeData()
  ├─ 实现资产懒加载
  ├─ 修复 Packed.getBin() 缓存
  ├─ 修复 QStandardItem 内存泄漏
  └─ AssetCacher 限容 + 索引优化

Phase 3 — 工程化（P2）
  ├─ 拆分上帝类（realres.py → 子模块）
  ├─ 消除 sys.path.append
  ├─ 添加类型注解
  ├─ 添加核心解析器 pytest
  ├─ 更新依赖 + 添加 CI/CD
  └─ 清理注释代码 + 统一代码格式

Phase 4 — 功能扩展（P3）
  ├─ 实现 3D 模型预览
  ├─ 修复碰撞模型偏移
  ├─ 支持 GRP3 格式（新版 Dagor 游戏）
  ├─ 恢复音效导出
  ├─ 动画/物理导出
  └─ 中文本地化（轻量 tr() + 字典）
```

---

## 6. 依赖升级记录

> 执行日期：2026-06-10

### 6.1 已完成变更

| 依赖 | 旧版本 | 新版本 | 操作 |
|------|--------|--------|------|
| **pylzma** | 0.5.0 | — | 🗑 移除，改用 Python stdlib `lzma`（零依赖） |
| **Requests** | 2.31.0 | — | 🗑 移除，代码中未使用 |
| Pillow | ==10.0.0 | >=11.0.0 | 版本范围放宽 |
| zstandard | ==0.15.1 | >=0.22.0 | 版本升级 |
| pyperclip | ==1.8.2 | >=1.8.2 | 保持兼容 |
| PyQt5 | ==5.15.9 | >=5.15.9 | 保持兼容（PySide6 迁移见 §7） |
| PyQt5_sip | ==12.12.0 | >=12.12.0 | 保持兼容 |

### 6.2 代码变更

`src/dae/util/decompression.py`:
```python
# 旧
from pylzma import decompress as lzmadecompress
from pylzma import compress as lzmacompress

def lzmaDecompress(data:bytes):
    return lzmadecompress(data)

# 新
from lzma import decompress as lzmadecompress, compress as lzmacompress, FORMAT_RAW

def lzmaDecompress(data:bytes):
    return lzmadecompress(data, format=FORMAT_RAW)
```

> ⚠️ 需用 `cMethod=0x20` 的实际文件验证 `FORMAT_RAW` 兼容性。

---

## 7. PySide6 迁移评估

> 评估日期：2026-06-10

### 7.1 当前状态

项目使用 **PyQt5 5.15.9**，通过 `loadUi()` 运行时加载 5 个 `.ui` 文件。PyQt5 由 Riverbank Computing 维护（GPL/商业双授权），PySide6 是 Qt 官方维护的 Python 绑定（LGPL）。

### 7.2 迁移收益

| 收益 | 说明 |
|------|------|
| Qt 6 原生渲染 | 自动获得 Windows 11 / Fluent 风格、更好高 DPI 支持 |
| 官方维护 | Qt Company 直接维护，Qt 6 新特性第一时间支持 |
| LGPL 协议 | 比 PyQt5 GPL 更宽松，无商业授权顾虑 |
| 长期存续 | PyQt5 随 Qt5 逐步停止维护，PySide6 是 Qt for Python 的未来 |

### 7.3 受影响文件

```
src/dae/gui/app.py              ← 主窗口，含 pyqtSignal × 7, loadUi, QRunnable, QThreadPool
src/dae/gui/customtreeview.py   ← 树控件，Qt 类型最多
src/dae/gui/mapDialog.py        ← 地图页，含 pyqtSignal, loadUi
src/dae/gui/settingsDialog.py   ← 设置弹窗，含 loadUi
src/dae/gui/progressDialog.py   ← 进度弹窗，含 uic.loadUi, winsound
src/dae/util/terminable.py      ← TerminableQObject(QObject, ...)
src/dae/util/misc.py            ← QDir, Qt, QFileDialog, QDialog
```

### 7.4 核心 API 差异

| PyQt5 | PySide6 | 影响文件数 |
|-------|---------|:---:|
| `from PyQt5.QtWidgets import ...` | `from PySide6.QtWidgets import ...` | 7 |
| `from PyQt5.QtCore import pyqtSignal` | `from PySide6.QtCore import Signal` | 2 |
| `from PyQt5.QtGui import ...` | `from PySide6.QtGui import ...` | 3 |
| `from PyQt5.uic import loadUi` | `PySide6.QtUiTools.QUiLoader` | 3 |
| `app.exec_()` | `app.exec()` | 1 |

### 7.5 .ui 文件加载策略

PySide6 不提供 `loadUi()` 便利函数。两个方案：

| 方案 | 做法 | 优点 | 缺点 |
|------|------|------|------|
| **A（推荐）** | 构建时 `pyside6-uic dae.ui -o dae_ui.py` | 启动更快、IDE 有补全、无运行时依赖 | 改 .ui 需重新编译 |
| B | 运行时 `QUiLoader().load(uiPath, self)` | 改动最小 | 每次启动解析 XML、需 `pip install PySide6-Addons` |

**推荐方案 A**，5 个 .ui 编译为 5 个 .py 类，一次编译、长期缓存。

```
ui/
├── dae.ui           →  src/dae/gui/ui_dae.py           (MainWindow)
├── mapWidget.ui     →  src/dae/gui/ui_mapwidget.py     (MapTab)
├── preview.ui       →  src/dae/gui/ui_preview.py       (未使用)
├── progressDialog.ui → src/dae/gui/ui_progress.py      (ProgressDialog)
└── settings.ui      →  src/dae/gui/ui_settings.py      (SettingsDialog)
```

### 7.6 特殊注意事项

| 项目 | 说明 |
|------|------|
| `winsound` | `progressDialog.py:8` — Windows 专用，迁移无影响 |
| `QMessageBox.Icon.Critical` | PySide6 枚举名相同，无需改动 |
| `Qt.AlignCenter` 等 | PySide6 中短形式仍然可用 |
| `QDir.Files`, `QDir.AllDirs` 等 | 枚举一致，无需改动 |
| `QFileDialog.DirectoryOnly` | 一致 |
| 拖放事件 `QMimeData` | 一致 |
| `QThreadPool`, `QRunnable` | 一致 |

### 7.7 迁移工作量评估

```
改动行数：        ~30 行 import 重命名
              +  5 个 .ui → .py 编译
              +  __main__.py  exec_() → exec()
              ─────────────────────────────
预估工时：        2-3 小时（含验证）
风险等级：        低（API 高度兼容，1:1 映射）
```

### 7.8 建议迁移时机

```
Phase 3 (工程化) 阶段执行，理由：
├─ P0/P1 修复不应被框架迁移噪音干扰
├─ 迁移后自动获得更好的 Windows 外观（无需额外美化工作）
└─ 对现有功能零影响，纯替换性重构
```

---

## 8. 附录：文件级改动清单

| 文件 | 问题数 | 关键问题 |
|------|--------|----------|
| `src/dae/gui/customtreeview.py` | 4 | 右键 `computeData()`、内存泄漏、上帝类、注释代码 |
| `src/dae/gui/app.py` | 3 | 线程不安全、全量加载、`format_exc` |
| `src/dae/util/terminable.py` | 3 | SafeRange Bug、Packed.getBin() 无缓存、继承问题 |
| `src/dae/util/fileread.py` | 2 | BinFile 错误继承 BufferedReader、type(data) == str |
| `src/dae/util/assetcacher.py` | 2 | 无淘汰机制、O(n) 材质查找 |
| `src/dae/parse/realres.py` | 4 | 上帝类、向量运算慢、PHYSMAT dict 过大、无类型注解 |
| `src/dae/parse/dbld.py` | 2 | ctypes 无保护、上帝类 |
| `src/dae/parse/mesh.py` | 1 | ShaderMesh 与 MatVData 复杂度过高 |
| `__main__.py` / 所有 `.py` | 2 | `sys.path.append` 污染、无相对导入 |
| 全局 | 4 | 无测试、无 CI/CD、过时依赖、无类型注解 |

---

> *此清单应在每次修复后更新，标记已完成项及发现的新问题。*
