import sys

from .gui import app

sys.excepthook = lambda cls, e, t: sys.__excepthook__(cls, e, t)

app = app.App(sys.argv)

exitCode = app.exec_()

sys.exit(exitCode)