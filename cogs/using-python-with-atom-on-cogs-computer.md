# Using Python with Atom.io on a COGS Computer
## Set user-defined path to a Python version
1. Open the `Run dialog` with `Win+R`
2. Enter `rundll32 sysdm.cpl,EditEnvironmentVariables` followed by `Enter`
3. In the first table, double click the Variable `Path`
4. In the new dialog, click in the first empty row and type in `C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3` (for Python 3.x) or `C:\Python27` (for Python 2.7) followed by Enter
5. Click Ok twice to close all dialogs

## Atom.io
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

### Using a language shell (REPL)
What is REPL? https://pythonprogramminglanguage.com/repl

1. Go to `File`/`Settings` in the Menu bar (if not displayed, you can display it by pressing the `ALT` key)
2. On the `Settings tab` change to `Install` (vertical tab) and search for `platformio-ide-terminal`
3. Click `Install` button, wait until package is installed
4. Click on the `Settings` button and scroll down to `Shell Override`
5. Replace content of input field with `C:\Windows\System32\cmd.exe` (unless you know what Powershell is and want to use it)
6. Close the `Settings tab`
7. Open Terminal with `Alt+Shift+T` in Atom.io
8. A new pane opens, press `Enter` if you don't see an input cursor
9. Type in `python` followed by another `Enter`
10. Voilà, your REPL is ready

### Recommended Packages/Plugins
- file-icons
- highlight-selected
- minimap
- pigments
- split-diff
- atom-beautify

## Other Settings which might be useful
- If Menu bar is not always show, press `ALT+V` and then choose `Toggle Menu Bar`

## Alternatives for your home computer
Use PyCharm (free student version) or Visual Studio Code (free as well). Personally, I like both editors.
