@echo off

set success=false

python test/test.py
if %errorlevel%==0 set success=true

if %success%==false (
    py test/test.py
    if %errorlevel%==0 set success=true
)

if %success%==false (
    python3 test/test.py
    if %errorlevel%==0 set success=true
)

if %success%==false (
    echo All attempts to run main.py failed.
) 

pause
