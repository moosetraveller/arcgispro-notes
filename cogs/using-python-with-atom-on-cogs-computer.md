# Using Python with Atom.io on a COGS Computer
## Set user-defined Path to a Python version
1. Open the `Run dialog` with `Win+R`
2. Enter `rundll32 sysdm.cpl,EditEnvironmentVariables` followed by `Enter`
3. In the first table, double click the Variable `PATH`
4. In the new dialog, click in the first empty row and type in `C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3` (for Python 3.x) or `C:\Python27` (for Python 2.7) followed by Enter
5. Click Ok twice to close all dialogs

Note: If you need to switch, change the `PATH` variable's value pointing to the other Python version. However, you need to restart Atom.

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
- linter-eslint
- linter-csslint

## Other Settings which might be useful
- If Menu bar is not always show, press `ALT+V` and then choose `Toggle Menu Bar`

## Language Shell (REPL)
What is REPL? https://pythonprogramminglanguage.com/repl

1. Open the `Run dialog` with `Win+R`
2. Type in `cmd` followed by `Enter` to open the Command Prompt
3. In the Command Prompt, enter `python` also followed by `Enter`

Note: To close the REPL, type in `quit()` followed by `Enter`. To close the Command Prompt, type in `exit` followed by `Enter`.

## Alternatives for your home computer
Use PyCharm (free student version) or Visual Studio Code (free as well). Personally, I like both editors.
