"""Chinese (Simplified) translations for DAE user-visible strings.

Strings already handled by Qt .ui files (via QCoreApplication.translate) are NOT
included here — they live in the compiled ui_*.py files.

To add a new language: copy this file to <lang_code>.py and translate STRINGS.
"""

STRINGS = {
    # ── Menu bar (File) ──
    "Open asset folder": "打开资源文件夹",
    "Open assets": "打开资源文件",
    "Open level file": "打开关卡文件",
    "Unmount all assets": "卸载全部资源",
    "Close": "关闭",

    # ── Menu bar (View) ──
    "Collapse all": "全部折叠",
    "Expand all": "全部展开",

    # ── Settings dialog ──
    "Settings...": "设置...",
    "Select StudioMDL binary": "选择 StudioMDL 程序",
    "Select gameinfo.txt": "选择 gameinfo.txt",
    "Language": "语言",
    "General": "常规",

    # ── Status messages ──
    "Mounting assets": "正在挂载资源",
    "Loading files...": "正在加载文件...",
    "Expanding items...": "正在展开项目...",
    "Loading map...": "正在加载地图...",
    "Loading map data...": "正在加载地图数据...",
    "Loading cell entities": "正在加载区块实体",
    "Writing DPL": "正在写入 DPL",
    "Exporting assets": "正在导出资源",
    "Generating model data": "正在生成模型数据",
    "Exporting model data to QC, SMD and VMT": "正在导出模型数据到 QC/SMD/VMT",
    "Compiling": "正在编译",
    "Exporting textures": "正在导出纹理",
    "Converting textures to VTF": "正在转换纹理为 VTF",

    # ── Error / Dialog ──
    "Unfunny!": "出错了！",
    "Failed to compute preliminary data. Check the console for details.":
        "计算预数据失败，请查看控制台获取详细信息。",
    "An error occured during the process. Check the console for details.":
        "处理过程中发生错误，请查看控制台获取详细信息。",

    # ── Context menu actions ──
    "Extract": "提取",
    "Extract all": "全部提取",
    "Export to DDS": "导出为 DDS",
    "Export all to DDS": "全部导出为 DDS",
    "Open file location": "打开文件位置",
    "Open parent location": "打开父级位置",
    "Copy path to clipboard": "复制路径到剪贴板",
    "Copy name to clipboard": "复制名称到剪贴板",
    "Save to": "保存到",
    "Export LOD...": "导出 LOD...",

    # ── Tree view ──
    "Search...": "搜索...",
    "Asset tree": "资源树",
    "Map prop layout exporter": "地图物件布局导出器",
    "Folder": "文件夹",

    # ── Action texts (dynamic patterns are not translated) ──
    "Export LOD 0 to Source engine": "导出 LOD 0 到 Source 引擎",
    "Export skeleton to dmf": "导出骨骼到 dmf",
    "Export all LODs to Source engine": "导出全部 LOD 到 Source 引擎",
    "Preview LOD 0": "预览 LOD 0",
}
