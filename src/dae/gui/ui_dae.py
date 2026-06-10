# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dae.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

from .customtreeview import CustomTreeView
from .mapDialog import MapTab

class Ui_DAEWindow(object):
    def setupUi(self, DAEWindow):
        if not DAEWindow.objectName():
            DAEWindow.setObjectName(u"DAEWindow")
        DAEWindow.resize(912, 827)
        DAEWindow.setStyleSheet(u"")
        DAEWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.actionOpenFolder = QAction(DAEWindow)
        self.actionOpenFolder.setObjectName(u"actionOpenFolder")
        self.actionCollapse = QAction(DAEWindow)
        self.actionCollapse.setObjectName(u"actionCollapse")
        self.actionExpand = QAction(DAEWindow)
        self.actionExpand.setObjectName(u"actionExpand")
        self.actionOpenFiles = QAction(DAEWindow)
        self.actionOpenFiles.setObjectName(u"actionOpenFiles")
        self.actionUnmount = QAction(DAEWindow)
        self.actionUnmount.setObjectName(u"actionUnmount")
        self.actionClose = QAction(DAEWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionSettings = QAction(DAEWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionOpenMap = QAction(DAEWindow)
        self.actionOpenMap.setObjectName(u"actionOpenMap")
        self.centralwidget = QWidget(DAEWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.treeView = CustomTreeView(self.tab)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setDragDropMode(QAbstractItemView.DropOnly)

        self.verticalLayout.addWidget(self.treeView)

        self.tabWidget.addTab(self.tab, "")
        self.mapTab = MapTab()
        self.mapTab.setObjectName(u"mapTab")
        self.tabWidget.addTab(self.mapTab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        DAEWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DAEWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 912, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        DAEWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuFile.addAction(self.actionOpenFolder)
        self.menuFile.addAction(self.actionOpenFiles)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionUnmount)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionClose)
        self.menuView.addAction(self.actionCollapse)
        self.menuView.addAction(self.actionExpand)

        self.retranslateUi(DAEWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DAEWindow)
    # setupUi

    def retranslateUi(self, DAEWindow):
        DAEWindow.setWindowTitle(QCoreApplication.translate("DAEWindow", u"Dagor Asset Explorer", None))
        self.actionOpenFolder.setText(QCoreApplication.translate("DAEWindow", u"Open asset folder", None))
#if QT_CONFIG(shortcut)
        self.actionOpenFolder.setShortcut(QCoreApplication.translate("DAEWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionCollapse.setText(QCoreApplication.translate("DAEWindow", u"Collapse all", None))
#if QT_CONFIG(shortcut)
        self.actionCollapse.setShortcut(QCoreApplication.translate("DAEWindow", u"Alt+0", None))
#endif // QT_CONFIG(shortcut)
        self.actionExpand.setText(QCoreApplication.translate("DAEWindow", u"Expand all", None))
#if QT_CONFIG(shortcut)
        self.actionExpand.setShortcut(QCoreApplication.translate("DAEWindow", u"Alt+Shift+0", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpenFiles.setText(QCoreApplication.translate("DAEWindow", u"Open assets", None))
#if QT_CONFIG(shortcut)
        self.actionOpenFiles.setShortcut(QCoreApplication.translate("DAEWindow", u"Ctrl+Shift+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionUnmount.setText(QCoreApplication.translate("DAEWindow", u"Unmount all assets", None))
        self.actionClose.setText(QCoreApplication.translate("DAEWindow", u"Close", None))
#if QT_CONFIG(shortcut)
        self.actionClose.setShortcut(QCoreApplication.translate("DAEWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionSettings.setText(QCoreApplication.translate("DAEWindow", u"Settings...", None))
        self.actionOpenMap.setText(QCoreApplication.translate("DAEWindow", u"Open level file", None))
#if QT_CONFIG(shortcut)
        self.actionOpenMap.setShortcut(QCoreApplication.translate("DAEWindow", u"Ctrl+Alt+O", None))
#endif // QT_CONFIG(shortcut)
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("DAEWindow", u"Search...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("DAEWindow", u"Asset tree", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mapTab), QCoreApplication.translate("DAEWindow", u"Map prop layout exporter", None))
        self.menuFile.setTitle(QCoreApplication.translate("DAEWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("DAEWindow", u"View", None))
    # retranslateUi

