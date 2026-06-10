from PySide6 import QtWidgets, QtGui
from . import ui_progress
from ..util.misc import getResPath
from ..strings import _
from winsound import PlaySound, SND_ALIAS, SND_ASYNC

LOADING_GIF_PATH = getResPath("loading.gif")
ERROR_ICO_PATH = getResPath("failure.png")



class MessageBox(QtWidgets.QMessageBox):
	def __init__(self, text:str):
		super().__init__()

		PlaySound("SystemHand", SND_ALIAS | SND_ASYNC)

		self.setIcon(QtWidgets.QMessageBox.Icon.Critical)
		self.setIconPixmap(QtGui.QPixmap(ERROR_ICO_PATH))
		self.setWindowTitle(_("Unfunny!"))
		self.setText(text)
		self.setStandardButtons(QtWidgets.QMessageBox.Ok)



class ProgressDialog(QtWidgets.QDialog, ui_progress.Ui_Dialog):
	progressLabel:QtWidgets.QLabel
	movieLabel:QtWidgets.QLabel
	progressBar:QtWidgets.QProgressBar
	cancelButton:QtWidgets.QPushButton

	def __init__(self, mainWindow):
		super().__init__()

		self.mainWindow = mainWindow

		self.setupUi(self)

		movie = QtGui.QMovie(LOADING_GIF_PATH)
		# movie.setScaledSize(LOADINGGIF_SIZE)
		movie.start()

		self.movieLabel.setMovie(movie)

		self.cancelButton.clicked.connect(self.cancel)

		self.show()
	
	def cancel(self):
		self.cancelButton.setEnabled(False)
		self.mainWindow.terminateThreads()
	
	def setStatus(self, status:str):
		self.progressLabel.setText(status)
		
	def setProgress(self, value:int):
		self.progressBar.setProperty("value", value)

class BusyProgressDialog(ProgressDialog):
	def __init__(self, *args, **kargs):
		super().__init__(*args, **kargs)

		self.progressBar.setMaximum(0)
		self.progressBar.setMinimum(0)
		self.progressBar.setValue(0)
