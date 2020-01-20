# Using Python with Atom.io on a COGS Computer
## Set user-defined Path to a Python version
1. Open the `Run dialog` with `Win+R`
2. Enter `rundll32 sysdm.cpl,EditEnvironmentVariables` followed by `Enter`
3. In the first table, double click the Variable `PATH`
4. In the new dialog, click in the first empty row and type in `C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3` for Python 3.x (or `C:\Python27` for Python 2.7 followed by Enter)
5. Click Ok twice to close all dialogs

Note: If you need to switch, change the `PATH` variable's value pointing to the other Python version. However, you need to restart Atom.

Note: In Fall 2019, we had to clone our ArcGIS Pro Python environment, the path might be different (eg. `C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3-clone`).

Note: If there is another path set in the system Path (where we do not have privileges to make changes), then you might need to follow the instructions of one of the alternatives below.

Note: If you have QGIS's `bin` directory in your Path variable (e.g. in order to use GDAL), make sure it is added below (after) the Python installation path. Otherwise Python from QGIS will be found.

### Alternative 1
1. Create a (batch) file on your desktop with the name `atom.bat`
2. Add on first line: `SET %PATH%="C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3";%PATH%`
3. Add on second line: `C:\Program Files\atom\app-1.43.0\atom.exe`
4. Save and close file
5. Start Atom with this batch file instead with your start menu.

Note: If you use this alternative, it is important that you do not close the console/terminal window, otherwise atom will be closed down as well (and you might have data loss)

### Alternative 2
1. Open Atom
2. Menu `File`, then `Settings` (or open Settings with `Ctrl+,`)
3. Click on button `Open Config Folder`
4. Navigate to `package\script\lib\grammars\python.coffee`
5. On line 12: replace `python` with `C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python`
6. Save with `Ctrl+S`
7. Close both (Atom) windows
8. Re-open Atom

Note: requires `script` package to be installed, but you need that anyway for Python development with Atom. How to install see below in Required Plugins.

Note: if you upgrade the `script` package, you have to redo above steps.

## Required Plugins
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

### Recommended Packages/Plugins
- file-icons
- highlight-selected
- minimap
- pigments
- split-diff
- atom-beautify

## Other Settings which might be useful
- If Menu bar is not always show, press `ALT+V` and then choose `Toggle Menu Bar`

## Language Shell (REPL)
What is REPL? https://pythonprogramminglanguage.com/repl

**Note:** To use REPL, it might be useful to use IDLE since it provides auto-complete.

### Command Prompt as an alternative to IDLE
1. Open the `Run dialog` with `Win+R`
2. Type in `cmd` followed by `Enter` to open the Command Prompt
3. In the Command Prompt, enter `python` also followed by `Enter`

Note: To close the REPL, type in `quit()` followed by `Enter`. To close the Command Prompt, type in `exit` followed by `Enter`.

## Alternatives for your home computer
Use PyCharm (free student version) or Visual Studio Code (free as well). Personally, I like both editors.
