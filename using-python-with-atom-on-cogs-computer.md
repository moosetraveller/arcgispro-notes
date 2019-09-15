# Using Python on COGS Computer
## Atom.io
We are not allowed to set a user-defined PATH variable. Therefore, following steps describes a workaround for this issue.
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
5. Double click the Batch file based on the Python version you want to start
6. Go to `File`/`Settings` in the Menu bar (if not displayed, you can display it by pressing the `ALT` key)
7. On the `Settings tab` change to `Install` (vertical tab) and search for `Script` (the authors name is rgbkrk, description is "Run code in Atom!" and it should have more than 2 million downloads)
8. Click `Install` button
9. Search for `autocomplete-python` and click `Install` as well
10. On the `Settings tab` change to `Packages` (vertical tab), clear filter if necessary, you should see both installed packages
11. Wait until both are installed
12. Click the `Settings` button for `autocomplete-python`
13. Disable `Use Kite-powered Completions` (checkbox should be empty)
14. Restart Atom with one of the two batch files (you only need to install the packages this once)
15. Create a script or open an existing one
16. If you write your code, there should be auto-completion available :-)
17. Run your Python script with `Ctrl+Shift+B` (must be saved beforehand and cursor must be inside the script tab)

## Other recommended Settings
- If Menu bar is not always show, press `ALT+V` and then choose `Toggle Menu Bar`
- Also, I recommend to use `Toggle Soft Wrap`

## Alternatives for your home computer
Use PyCharm (free student version) or Visual Studio Code (free as well). Personally, I like both editors.
