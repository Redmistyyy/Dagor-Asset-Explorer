import sys
from os import path

# When run from src/, Python loses the project root's Lib/site-packages.
# Add it back so PySide6 (installed to <root>/Lib/site-packages) is found.
# __file__ = src/dae/__main__.py → dirname×3 = project root
_rootdir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
_lib = path.join(_rootdir, "Lib", "site-packages")
if path.exists(_lib):
	sys.path.insert(0, _lib)

from .gui import app

from .gui import app

sys.excepthook = lambda cls, e, t: sys.__excepthook__(cls, e, t)

app = app.App(sys.argv)

exitCode = app.exec()

sys.exit(exitCode)