cd /d %~dp0
call venv\Scripts\activate
cmd /k "venv\Scripts\pytest.exe -vv test.py && pause"