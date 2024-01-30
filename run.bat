cd /d %~dp0
call venv\Scripts\activate
cmd /k "venv\Scripts\python.exe __main__.py && pause"