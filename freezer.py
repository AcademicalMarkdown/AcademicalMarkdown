from cx_Freeze import setup, Executable

from info import *

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executable_file_path = os.path.join(PROJECT_ROOT_PATH, 'mdac.py')
build_exe_options = {"packages": ["fire", 'pygments']}

setup(name=PROJECT_SHORT_NAME,
      version=PROJECT_VERSION,
      description=PROJECT_SHORT_DESCRIPTION,
      options={"build_exe": build_exe_options},
      executables=[Executable(script=executable_file_path)])
