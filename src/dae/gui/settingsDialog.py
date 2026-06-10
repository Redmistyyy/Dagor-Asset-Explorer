
from PySide6.QtWidgets import QDialog, QWidget, QCheckBox, QLineEdit, QPushButton, QFileDialog, QVBoxLayout, QComboBox, QLabel
from . import ui_settings
from ..util.misc import openFile
from ..util.enums import *
from ..util.settings import SETTINGS
from ..strings import _, load_lang


class SettingsDialog(QDialog, ui_settings.Ui_settings):
	vLayout:QVBoxLayout

	exportFolder:QCheckBox
	expandAll:QCheckBox
	extractFolder:QCheckBox
	noTexExport:QCheckBox
	outputFolder:QCheckBox
	exportSourceCollision:QCheckBox
	exportGameInfo:QCheckBox
	exportSMD:QCheckBox
	noMDL:QCheckBox
	dontExportExistingTextures:QCheckBox
	convertTex:QCheckBox

	studiomdlLine:QLineEdit
	studioMdlBtn:QPushButton
	gameInfoLine:QLineEdit
	gameInfoBtn:QPushButton

	exportGameInfoLayout:QVBoxLayout
	exportSMDLayout:QVBoxLayout

	
	def __init__(self, parent:QWidget):
		super().__init__(parent)

		self.setupUi(self)

		self.vLayout.setContentsMargins(-1, -1, -1, -1)

		self.setupCheckBox(self.exportFolder, SETTINGS_EXPORT_FOLDER)
		self.setupCheckBox(self.convertTex, SETTINGS_FORCE_DDS_CONVERSION)
		self.setupCheckBox(self.expandAll, SETTINGS_EXPAND_ALL)
		self.setupCheckBox(self.extractFolder, SETTINGS_EXTRACT_FOLDER)
		self.setupCheckBox(self.noTexExport, SETTINGS_NO_TEX_EXPORT)
		self.setupCheckBox(self.outputFolder, SETTINGS_OUTPUT_FOLDER)
		self.setupCheckBox(self.exportSourceCollision, SETTINGS_STUDIOMDL_EXPORT_COLLISION)
		self.setupCheckBox(self.exportGameInfo, SETTINGS_EXPORT_GAMEINFO, self.exportGameInfoLayout)
		self.setupCheckBox(self.exportSMD, SETTINGS_EXPORT_SMD, self.exportSMDLayout)
		self.setupCheckBox(self.noMDL, SETTINGS_NO_MDL)
		self.setupCheckBox(self.dontExportExistingTextures, SETTINGS_DONT_EXPORT_EXISTING_TEXTURES)


		self.studiomdlLine.setText(SETTINGS.getValue(SETTINGS_STUDIOMDL_PATH))
		self.studioMdlBtn.clicked.connect(lambda: self.selectFile(_("Select StudioMDL binary"), ["studiomdl.exe"], SETTINGS_STUDIOMDL_PATH, self.studiomdlLine))

		self.gameInfoLine.setText(SETTINGS.getValue(SETTINGS_GAMEINFO_PATH))
		self.gameInfoBtn.clicked.connect(lambda: self.selectFile(_("Select gameinfo.txt"), ["gameinfo.txt"], SETTINGS_GAMEINFO_PATH, self.gameInfoLine))

		# Language selector
		langLabel = QLabel(_("Language"), self.general)
		self.verticalLayout.addWidget(langLabel)

		self.langCombo = QComboBox(self.general)
		self.langCombo.addItem("English", "en")
		self.langCombo.addItem("中文", "zh")
		idx = self.langCombo.findData(SETTINGS.getValue(SETTINGS_LANGUAGE))
		if idx >= 0:
			self.langCombo.setCurrentIndex(idx)
		self.langCombo.currentIndexChanged.connect(self.onLangChanged)
		self.verticalLayout.addWidget(self.langCombo)
		# Note: language change takes effect on next launch
	
	def selectFile(self, title:str, nameFilters:list[str], settingKey:str, lineEdit:QLineEdit):
		dialog = openFile(self, title = title, nameFilters = nameFilters, fileMode = QFileDialog.ExistingFile)

		if dialog is None:
			return
		
		path = dialog.selectedFiles()[0]

		lineEdit.setText(path)
		SETTINGS.setValue(settingKey, path)
		SETTINGS.saveSettings()

	def setupCheckBox(self, cBox:QCheckBox, setting:str, layout:QVBoxLayout = None):
		val = SETTINGS.getValue(setting)
		cBox.setChecked(val)
		cBox.stateChanged.connect(lambda: self.toggleSetting(setting, layout))

		if layout is not None:
			self.handleLayout(layout, not val)

	def handleLayout(self, layout:QVBoxLayout, enable:bool):
		for i in range(layout.count()):
			child = layout.itemAt(i).widget()

			if not isinstance(child, QCheckBox):
				continue

			child.setDisabled(enable)

	def toggleSetting(self, setting:str, layout:QVBoxLayout = None):
		newVal = not SETTINGS.getValue(setting)

		SETTINGS.setValue(setting, newVal)

		if layout is not None:
			self.handleLayout(layout, not newVal)

	def onLangChanged(self, idx):
		lang = self.langCombo.itemData(idx)
		if lang:
			SETTINGS.setValue(SETTINGS_LANGUAGE, lang)
			load_lang(lang)