# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mapWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(761, 724)
        Form.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout.addWidget(self.lineEdit)

        self.browse = QPushButton(Form)
        self.browse.setObjectName(u"browse")
        self.browse.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout.addWidget(self.browse)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalSpacer_2 = QSpacerItem(400, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_2)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 737, 473))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.infoLabel = QLabel(Form)
        self.infoLabel.setObjectName(u"infoLabel")

        self.verticalLayout_3.addWidget(self.infoLabel)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.enlistedMap = QCheckBox(Form)
        self.enlistedMap.setObjectName(u"enlistedMap")

        self.horizontalLayout_2.addWidget(self.enlistedMap)

        self.exportVegetation = QCheckBox(Form)
        self.exportVegetation.setObjectName(u"exportVegetation")
        self.exportVegetation.setChecked(True)

        self.horizontalLayout_2.addWidget(self.exportVegetation)

        self.exportNonVegetation = QCheckBox(Form)
        self.exportNonVegetation.setObjectName(u"exportNonVegetation")
        self.exportNonVegetation.setChecked(True)

        self.horizontalLayout_2.addWidget(self.exportNonVegetation)

        self.exportAssets = QCheckBox(Form)
        self.exportAssets.setObjectName(u"exportAssets")

        self.horizontalLayout_2.addWidget(self.exportAssets)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.exportButton = QPushButton(Form)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setEnabled(False)

        self.verticalLayout.addWidget(self.exportButton)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Dagor Asset Explorer - Per-cell map prop layout export", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Path to map file", None))
        self.browse.setWindowTitle(QCoreApplication.translate("Form", u"Dagor Asset Explorer - Per-cell map prop layout export", None))
        self.browse.setText(QCoreApplication.translate("Form", u"Browse...", None))
        self.infoLabel.setText(QCoreApplication.translate("Form", u"Map info...", None))
        self.enlistedMap.setText(QCoreApplication.translate("Form", u"Enlisted map", None))
        self.exportVegetation.setText(QCoreApplication.translate("Form", u"Export vegetation", None))
        self.exportNonVegetation.setText(QCoreApplication.translate("Form", u"Export non-vegetation", None))
        self.exportAssets.setText(QCoreApplication.translate("Form", u"Export loaded assets", None))
        self.exportButton.setText(QCoreApplication.translate("Form", u"Export to DPL...", None))
    # retranslateUi

