# Using Python on COGS Computer other than IDLE
## Issue
We are not allowed to set a User-defined PATH variable. 
## Atom.io
1. Open any editor, copy&paste following two lines:
```
set PATH=%PATH%;"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3"
"C:\Program Files\atom\app-1.38.2\atom.exe"
```
2. Save file as `Use Atom with Python 3x.bat` on your desktop
3. Create another file with following two lines:
```
set PATH=%PATH%;"C:\Python27"
"C:\Program Files\atom\app-1.38.2\atom.exe"
```
4. Save file as `Use Atom with Python 2x.bat` on your desktop
5. Double click the Batch file based on the Python version you need
