import os
import sys
from cx_Freeze import setup, Executable

# Add files
files = ['icon.ico',
         'Resources',
         'UI',
         'modules'
         ]

# target
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# setup
setup(
    name="WebDes",
    version="1.0.1",
    description="HTML Editor",
    author="Tanay Kar",
    options={'build_exe': {'include_files': files}},
    executables=[target]
)