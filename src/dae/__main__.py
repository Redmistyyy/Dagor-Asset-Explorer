import sys
from os import path

# Add project root so Lib/site-packages (and lib/, ui/, res/) are reachable
_srcdir = path.dirname(path.abspath(__file__))
_rootdir = path.dirname(path.dirname(_srcdir))  # src/dae/ -> src/ -> project root
if path.exists(path.join(_rootdir, "Lib", "site-packages")):
    sys.path.insert(0, path.join(_rootdir, "Lib", "site-packages"))
sys.path.insert(0, _srcdir)

from gui import app

sys.excepthook = lambda cls, e, t: sys.__excepthook__(cls, e, t)

app = app.App(sys.argv)

exitCode = app.exec_()

sys.exit(exitCode)