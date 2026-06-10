@echo off
cd /d "%~dp0src"
pip install pyinstaller -q
pyinstaller -p "./dae/gui;./dae/util;./dae/parse" -F dae/__main__.py -n DagorAssetExplorer
echo.
echo Build complete: dist\DagorAssetExplorer.exe
pause
