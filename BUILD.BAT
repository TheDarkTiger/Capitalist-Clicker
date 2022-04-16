@echo off

echo Compile
pyinstaller "Capitalist Clicker.py" --onefile --noconsole

echo Clean
rmdir __pycache__ /S /Q
rmdir build /S /Q

echo Done
