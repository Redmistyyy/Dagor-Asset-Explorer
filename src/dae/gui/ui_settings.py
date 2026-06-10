# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_settings(object):
    def setupUi(self, settings):
        if not settings.objectName():
            settings.setObjectName(u"settings")
        settings.resize(550, 365)
        self.vLayout = QVBoxLayout(settings)
        self.vLayout.setObjectName(u"vLayout")
        self.tabWidget = QTabWidget(settings)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.general = QWidget()
        self.general.setObjectName(u"general")
        self.verticalLayout = QVBoxLayout(self.general)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.extractFolder = QCheckBox(self.general)
        self.extractFolder.setObjectName(u"extractFolder")
        self.extractFolder.setChecked(True)

        self.verticalLayout.addWidget(self.extractFolder)

        self.exportFolder = QCheckBox(self.general)
        self.exportFolder.setObjectName(u"exportFolder")
        self.exportFolder.setChecked(True)

        self.verticalLayout.addWidget(self.exportFolder)

        self.convertTex = QCheckBox(self.general)
        self.convertTex.setObjectName(u"convertTex")
        self.convertTex.setChecked(True)

        self.verticalLayout.addWidget(self.convertTex)

        self.outputFolder = QCheckBox(self.general)
        self.outputFolder.setObjectName(u"outputFolder")

        self.verticalLayout.addWidget(self.outputFolder)

        self.noTexExport = QCheckBox(self.general)
        self.noTexExport.setObjectName(u"noTexExport")

        self.verticalLayout.addWidget(self.noTexExport)

        self.expandAll = QCheckBox(self.general)
        self.expandAll.setObjectName(u"expandAll")
        self.expandAll.setCheckable(True)

        self.verticalLayout.addWidget(self.expandAll)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.general, "")
        self.Streamlining = QWidget()
        self.Streamlining.setObjectName(u"Streamlining")
        self.verticalLayout_2 = QVBoxLayout(self.Streamlining)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.Streamlining)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.Streamlining)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.line = QFrame(self.Streamlining)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.studiomdlLine = QLineEdit(self.Streamlining)
        self.studiomdlLine.setObjectName(u"studiomdlLine")
        self.studiomdlLine.setEnabled(False)

        self.horizontalLayout.addWidget(self.studiomdlLine)

        self.studioMdlBtn = QPushButton(self.Streamlining)
        self.studioMdlBtn.setObjectName(u"studioMdlBtn")

        self.horizontalLayout.addWidget(self.studioMdlBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gameInfoLine = QLineEdit(self.Streamlining)
        self.gameInfoLine.setObjectName(u"gameInfoLine")
        self.gameInfoLine.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.gameInfoLine)

        self.gameInfoBtn = QPushButton(self.Streamlining)
        self.gameInfoBtn.setObjectName(u"gameInfoBtn")

        self.horizontalLayout_4.addWidget(self.gameInfoBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.exportSMD = QCheckBox(self.Streamlining)
        self.exportSMD.setObjectName(u"exportSMD")
        self.exportSMD.setChecked(True)

        self.verticalLayout_2.addWidget(self.exportSMD)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(24, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.exportSMDLayout = QVBoxLayout()
        self.exportSMDLayout.setObjectName(u"exportSMDLayout")
        self.exportSourceCollision = QCheckBox(self.Streamlining)
        self.exportSourceCollision.setObjectName(u"exportSourceCollision")
        self.exportSourceCollision.setChecked(True)

        self.exportSMDLayout.addWidget(self.exportSourceCollision)

        self.noMDL = QCheckBox(self.Streamlining)
        self.noMDL.setObjectName(u"noMDL")

        self.exportSMDLayout.addWidget(self.noMDL)


        self.horizontalLayout_6.addLayout(self.exportSMDLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.exportGameInfo = QCheckBox(self.Streamlining)
        self.exportGameInfo.setObjectName(u"exportGameInfo")

        self.verticalLayout_2.addWidget(self.exportGameInfo)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(24, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.exportGameInfoLayout = QVBoxLayout()
        self.exportGameInfoLayout.setObjectName(u"exportGameInfoLayout")
        self.dontExportExistingTextures = QCheckBox(self.Streamlining)
        self.dontExportExistingTextures.setObjectName(u"dontExportExistingTextures")
        self.dontExportExistingTextures.setEnabled(False)
        self.dontExportExistingTextures.setCheckable(True)
        self.dontExportExistingTextures.setChecked(False)

        self.exportGameInfoLayout.addWidget(self.dontExportExistingTextures)


        self.horizontalLayout_3.addLayout(self.exportGameInfoLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.Streamlining, "")

        self.vLayout.addWidget(self.tabWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.githubLabel = QLabel(settings)
        self.githubLabel.setObjectName(u"githubLabel")
        self.githubLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.githubLabel.setOpenExternalLinks(True)
        self.githubLabel.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.horizontalLayout_2.addWidget(self.githubLabel)

        self.label = QLabel(settings)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.horizontalLayout_2.addWidget(self.label)


        self.vLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(settings)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(settings)
    # setupUi

    def retranslateUi(self, settings):
        settings.setWindowTitle(QCoreApplication.translate("settings", u"Dagor Asset Explorer - Settings", None))
        self.extractFolder.setText(QCoreApplication.translate("settings", u"Create a folder when batch-extracting packed files", None))
        self.exportFolder.setText(QCoreApplication.translate("settings", u"Create a folder when batch-exporting packed files", None))
        self.convertTex.setText(QCoreApplication.translate("settings", u"Convert textures to DXT5", None))
        self.outputFolder.setText(QCoreApplication.translate("settings", u"Disable \"Save to...\" dialog and save everything to the \"output\" folder", None))
        self.noTexExport.setText(QCoreApplication.translate("settings", u"Do not export textures when exporting models", None))
        self.expandAll.setText(QCoreApplication.translate("settings", u"Expand all items by default", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.general), QCoreApplication.translate("settings", u"General", None))
        self.label_2.setText(QCoreApplication.translate("settings", u"<html><head/><body><p><span style=\" font-weight:600;\">WIP / DEMO</span> - Streamline model production to the Source Engine</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("settings", u"Features basic VMT, VTF, QC and SMD generation + skeleton support (max 128 bones)", None))
        self.studiomdlLine.setPlaceholderText(QCoreApplication.translate("settings", u"path/to/studiomdl.exe", None))
        self.studioMdlBtn.setText(QCoreApplication.translate("settings", u"Browse...", None))
        self.gameInfoLine.setPlaceholderText(QCoreApplication.translate("settings", u"path/to/gameinfo.txt", None))
        self.gameInfoBtn.setText(QCoreApplication.translate("settings", u"Browse...", None))
        self.exportSMD.setText(QCoreApplication.translate("settings", u"Export SMDs", None))
        self.exportSourceCollision.setText(QCoreApplication.translate("settings", u"Export collision models", None))
        self.noMDL.setText(QCoreApplication.translate("settings", u"Do not compile to .mdl", None))
        self.exportGameInfo.setText(QCoreApplication.translate("settings", u"Export to the game's \"models\" and \"materials\" folders", None))
        self.dontExportExistingTextures.setText(QCoreApplication.translate("settings", u"Do not export existing textures", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Streamlining), QCoreApplication.translate("settings", u"Streamlining", None))
        self.githubLabel.setText(QCoreApplication.translate("settings", u"<html><head/><body><p><a href=\"https://github.com/Gredwitch/Dagor-Asset-Explorer\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub</span></a></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("settings", u"<html><head/><body><p><a href=\"https://github.com/Gredwitch/Dagor-Asset-Explorer-Tools\"><span style=\" text-decoration: underline; color:#0000ff;\">Blender DMF / DPL importer</span></a></p></body></html>", None))
    # retranslateUi

