@echo off
cd /d "%~dp0src"
python -m pip install pyinstaller -q
python -m PyInstaller -p "./dae/gui;./dae/util;./dae/parse" -F dae/__main__.py -n DagorAssetExplorer
echo.
echo Build complete: dist\DagorAssetExplorer.exe
pause
