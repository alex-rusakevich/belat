from cx_Freeze import Executable, setup

import belat

includefiles = ["config.json", "LICENSE", "README.md"]
includes = [
    "belat.official",
    "belat.classic",
    "belat.gost1687671tb1",
    "belat.gost1687671tb2",
    "belat.gost7792000sysa",
    "belat.gost7792000sysb",
]
excludes = []
packages = []

setup(
    name="belat",
    version=belat.VERSION,
    description="belat",
    author="Alexander Rusakevich",
    options={
        "build_exe": {
            "includes": includes,
            "excludes": excludes,
            "packages": packages,
            "include_files": includefiles,
        }
    },
    executables=[Executable("belat.pyw", icon="icon.ico", base="Win32GUI")],
)
