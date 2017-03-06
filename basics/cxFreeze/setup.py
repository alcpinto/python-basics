from cx_Freeze import setup, Executable

setup(name='urlParse',
      version=0.1,
      description='My url parser',
      executables=[Executable('myProgram.py')])

