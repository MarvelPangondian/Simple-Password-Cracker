@echo off

set success=false

python src/main.py
if %errorlevel%==0 set success=true

if %success%==false (
    py src/main.py
    if %errorlevel%==0 set success=true
)

if %success%==false (
    python3 src/main.py
    if %errorlevel%==0 set success=true
)

if %success%==false (
    echo All attempts to run main.py failed.
) 

pause
