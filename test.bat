@echo off
cd /d "%~dp0"
python -m pip install pytest -q
python -m pytest tests\ -v
pause
