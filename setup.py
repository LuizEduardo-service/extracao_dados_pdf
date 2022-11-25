import sys
import os
from cx_Freeze import setup,Executable

files = []
exe = Executable(script="extracao_dados_pdf.py", base='Win32GUI')
includes = []

setup(
    name="Extração de dados PDF",
    version='1.0',
    description="",
    author='Luiz Eduardo Cassimiro',
    options={'builder_exe':{'include_files': files,'includes': includes}},
    executables=[exe]

)