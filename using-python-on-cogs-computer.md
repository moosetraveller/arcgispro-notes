# Using Python on COGS Computer other than IDLE
## Issues
1. We are not allowed to set a User-defined PATH variable. 
2. No useful editor install
3. We won't be able to install third-party libraries (e.g. no linter to validate code such as flake8)

## Atom.io (not the best choice but the only useful editor installed)
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
6. Go to `File`/`Settings` in the Menu bar (if not displayed, you can display it by pressing the `ALT` key)
7. On the `Settings tab` change to `Install` (vertical tab) and search for `Script` (the authors name is rgbkrk, description is "Run code in Atom!" and it should have more than 2 million downloads)
8. Click `Install` button
9. Restart Atom with one of the two batch files (you only need to install `Script` plugin this once)
10. Run your Python script with `Ctrl+Shift+B` (must be saved beforehand and cursor must be inside the script tab)
### Disadvantages of using Atom.io over Idle
There is no auto-completion, looks like Idle has a auto-completion. Atom.io could also have one but not configureable without admin rights.

## Alternatives for your home computer
Use PyCharm (free student version) or Visual Studio Code (free as well). Personally I like both editors.
