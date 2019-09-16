# Using Python with Atom.io on a COGS Computer
## Atom.io
### Python Versions
We are not allowed to set a user-defined PATH variable. Therefore, following steps describes a workaround for this issue.
1. Open any editor, copy&paste following two lines:
```
set PATH=%PATH%;"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3"
atom
```
2. Save file as `Use Atom with Python 3x.bat` on your desktop
3. Create another file with following two lines:
```
set PATH=%PATH%;"C:\Python27"
atom
```
4. Save file as `Use Atom with Python 2x.bat` on your desktop
5. Double click the Batch file based on the Python version you want to start

### Required Plugins
1. Go to `File`/`Settings` in the Menu bar (if not displayed, you can display it by pressing the `ALT` key)
2. On the `Settings tab` change to `Install` (vertical tab) and search for `Script`
3. Click `Install` button
4. Search for `autocomplete-python` and click `Install` as well
5. On the `Settings tab` change to `Packages` (vertical tab), clear filter if necessary, you should see both installed packages
6. Wait until both are installed
7. Click the `Settings` button for `autocomplete-python`
8. Disable `Use Kite-powered Completions` (checkbox should be empty)
9. Restart Atom with one of the two batch files (you only need to install the packages this once)
10. Create a script or open an existing one
11. If you write your code, there should be auto-completion available :-)
12. Run your Python script with `Ctrl+Shift+B` (must be saved beforehand and cursor must be inside the script tab)

### Change Icons for Batch Files
1. Move batch files to another locations such as your D drive
2. Create Shortcuts on Desktop pointing to those batch files
3. Open `Properties` for each of those Shortcuts
4. Click `Change Icon...`
5. Clear input field and paste following path: `C:\Program Files\atom\app-1.38.2\atom.exe`
6. Press `OK` twice and close the `Properties` dialog

Note: if you want to pin the icon to the taskbar might be a bit tricky, you have to pin the cmd-window of the batch file and not Atom.io when the application is started, otherwise the user-defined path won't be set. However, it seems that this is not possible (I might be wrong tho ;))

### Using a language shell (REPL)
What is REPL? https://pythonprogramminglanguage.com/repl
1. Go to `File`/`Settings` in the Menu bar (if not displayed, you can display it by pressing the `ALT` key)
2. On the `Settings tab` change to `Install` (vertical tab) and search for `platformio-ide-terminal`
3. Click `Install` button, wait until package is installed
4. Click on the `Settings` button and scroll down to `Shell Override`
5. Replace content of input field with `C:\Windows\System32\cmd.exe` (unless you know what Powershell is and want to use it)
6. Close the `Settings tab`
7. Open Terminal with `Alt+Shift+T` in Atom.io
8. A new pane opens, press `Enter`
9. Type in `python` followed by another `Enter`
10. Voilà, your REPL is ready

## Other Settings which might be useful
- If Menu bar is not always show, press `ALT+V` and then choose `Toggle Menu Bar`

## Alternatives for your home computer
Use PyCharm (free student version) or Visual Studio Code (free as well). Personally, I like both editors.
