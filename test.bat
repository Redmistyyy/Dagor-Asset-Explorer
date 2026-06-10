@echo off
cd /d "%~dp0"
pip install pytest -q
python -m pytest tests\ -v
pause
