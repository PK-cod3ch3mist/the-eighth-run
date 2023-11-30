# cx_Freeze setup script for The Eighth Run
# To get an executable, run `python setup.py build` in the terminal
# This will create a build folder with the executable in it
# You can also run `python setup.py bdist_msi` to create an installer
# This will create a dist folder with the installer in it
# You can also run `python setup.py bdist_dmg` to create a DMG file
# This will create a dist folder with the DMG file in it

import cx_Freeze

base = None
if cx_Freeze.sys.platform == "win32":
    base = "Win32GUI"

executables = [
    cx_Freeze.Executable(
        script="main.py", icon="icon.ico", target_name="The Eighth Run", base=base
    ),
]

build_exe_options = {"packages": ["pygame"], "include_files": ["assets"]}

bdist_dmg_options = {"applications_shortcut": True, "volume_label": "The Eighth Run"}

shortcut_table = [
    (
        "DesktopShortcut",
        "DesktopFolder",
        "The Eighth Run",
        "TARGETDIR",
        "[TARGETDIR]The Eighth Run.exe",
        None,
        None,
        None,
        None,
        None,
        None,
        "TARGETDIR",
    )
]
msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {"data": msi_data}

cx_Freeze.setup(
    name="The Eighth Run",
    version="1.1",
    description="A game made for the GitHub Game Off 2023",
    author="Pratyush Kumar",
    options={
        "build_exe": build_exe_options,
        "bdist_dmg": bdist_dmg_options,
        "bdist_msi": bdist_msi_options,
    },
    executables=executables,
)
