# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(846, 585)
        self.actionOpenFolder = QAction(MainWindow)
        self.actionOpenFolder.setObjectName(u"actionOpenFolder")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionAutoLabeling = QAction(MainWindow)
        self.actionAutoLabeling.setObjectName(u"actionAutoLabeling")
        self.actionAutoLabeling.setCheckable(True)
        self.actionAutoLabeling.setChecked(True)
        self.actionABS = QAction(MainWindow)
        self.actionABS.setObjectName(u"actionABS")
        self.actionABS.setCheckable(True)
        self.actionREL = QAction(MainWindow)
        self.actionREL.setObjectName(u"actionREL")
        self.actionREL.setCheckable(True)
        self.actionREL.setChecked(True)
        self.actionOpenFile = QAction(MainWindow)
        self.actionOpenFile.setObjectName(u"actionOpenFile")
        self.actionOpenClassFile = QAction(MainWindow)
        self.actionOpenClassFile.setObjectName(u"actionOpenClassFile")
        self.actionHardDelete = QAction(MainWindow)
        self.actionHardDelete.setObjectName(u"actionHardDelete")
        self.actionHardDelete.setCheckable(True)
        self.actionAddupFolder = QAction(MainWindow)
        self.actionAddupFolder.setObjectName(u"actionAddupFolder")
        self.actionNewClassFile = QAction(MainWindow)
        self.actionNewClassFile.setObjectName(u"actionNewClassFile")
        self.actionSaveSetting = QAction(MainWindow)
        self.actionSaveSetting.setObjectName(u"actionSaveSetting")
        self.actionMakeDataset = QAction(MainWindow)
        self.actionMakeDataset.setObjectName(u"actionMakeDataset")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 21))
        self.label.setMaximumSize(QSize(50, 21))

        self.horizontalLayout.addWidget(self.label)

        self.filesLabel = QLabel(self.centralwidget)
        self.filesLabel.setObjectName(u"filesLabel")
        self.filesLabel.setMinimumSize(QSize(150, 21))
        self.filesLabel.setMaximumSize(QSize(150, 21))

        self.horizontalLayout.addWidget(self.filesLabel)

        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setEnabled(False)
        self.deleteButton.setMaximumSize(QSize(86, 16777215))

        self.horizontalLayout.addWidget(self.deleteButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.fileListWidget = QListWidget(self.centralwidget)
        self.fileListWidget.setObjectName(u"fileListWidget")
        self.fileListWidget.setMinimumSize(QSize(300, 288))
        self.fileListWidget.setMaximumSize(QSize(300, 16777215))
        self.fileListWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.fileListWidget.setDragEnabled(False)
        self.fileListWidget.setTextElideMode(Qt.ElideNone)
        self.fileListWidget.setFlow(QListView.TopToBottom)

        self.verticalLayout.addWidget(self.fileListWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.downButton = QPushButton(self.centralwidget)
        self.downButton.setObjectName(u"downButton")
        self.downButton.setEnabled(False)
        self.downButton.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_2.addWidget(self.downButton)

        self.filesTextEdit = QLineEdit(self.centralwidget)
        self.filesTextEdit.setObjectName(u"filesTextEdit")
        self.filesTextEdit.setEnabled(False)
        self.filesTextEdit.setMinimumSize(QSize(0, 23))
        self.filesTextEdit.setMaximumSize(QSize(136, 23))
        self.filesTextEdit.setMaxLength(10)

        self.horizontalLayout_2.addWidget(self.filesTextEdit)

        self.upButton = QPushButton(self.centralwidget)
        self.upButton.setObjectName(u"upButton")
        self.upButton.setEnabled(False)
        self.upButton.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_2.addWidget(self.upButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.graphicsViewGridLayout = QGridLayout()
        self.graphicsViewGridLayout.setSpacing(0)
        self.graphicsViewGridLayout.setObjectName(u"graphicsViewGridLayout")
        self.graphicsViewGridLayout.setSizeConstraint(QLayout.SetMaximumSize)

        self.gridLayout_2.addLayout(self.graphicsViewGridLayout, 0, 1, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.classTableWidget = QTableWidget(self.centralwidget)
        if (self.classTableWidget.columnCount() < 3):
            self.classTableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.classTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.classTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.classTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.classTableWidget.setObjectName(u"classTableWidget")
        self.classTableWidget.setMinimumSize(QSize(0, 80))
        self.classTableWidget.setMaximumSize(QSize(16777215, 120))
        self.classTableWidget.setAutoScroll(False)
        self.classTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.classTableWidget.horizontalHeader().setDefaultSectionSize(90)

        self.verticalLayout_2.addWidget(self.classTableWidget)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.labelTableWidget = QTableWidget(self.centralwidget)
        if (self.labelTableWidget.columnCount() < 6):
            self.labelTableWidget.setColumnCount(6)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.labelTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.labelTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.labelTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.labelTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.labelTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.labelTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem8)
        self.labelTableWidget.setObjectName(u"labelTableWidget")
        self.labelTableWidget.setMinimumSize(QSize(0, 80))
        self.labelTableWidget.setMaximumSize(QSize(16777215, 120))
        self.labelTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.labelTableWidget.horizontalHeader().setDefaultSectionSize(80)

        self.gridLayout_4.addWidget(self.labelTableWidget, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 17, 0, 1, 2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_3.setVerticalSpacing(0)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 23))
        self.label_3.setMaximumSize(QSize(80, 23))

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.labelPathLineEdit = QLineEdit(self.centralwidget)
        self.labelPathLineEdit.setObjectName(u"labelPathLineEdit")
        self.labelPathLineEdit.setMinimumSize(QSize(0, 23))
        self.labelPathLineEdit.setMaximumSize(QSize(16777215, 23))
        self.labelPathLineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.labelPathLineEdit, 0, 1, 1, 1)

        self.classPathButton = QPushButton(self.centralwidget)
        self.classPathButton.setObjectName(u"classPathButton")
        self.classPathButton.setMinimumSize(QSize(0, 23))
        self.classPathButton.setMaximumSize(QSize(70, 23))

        self.gridLayout_3.addWidget(self.classPathButton, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 18, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 846, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menuSetting = QMenu(self.menubar)
        self.menuSetting.setObjectName(u"menuSetting")
        self.menuSaveValues = QMenu(self.menuSetting)
        self.menuSaveValues.setObjectName(u"menuSaveValues")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menu.addAction(self.actionOpenFile)
        self.menu.addAction(self.actionOpenFolder)
        self.menu.addSeparator()
        self.menu.addAction(self.actionNewClassFile)
        self.menu.addAction(self.actionOpenClassFile)
        self.menu.addSeparator()
        self.menu.addAction(self.actionClose)
        self.menuSetting.addAction(self.actionAutoLabeling)
        self.menuSetting.addAction(self.menuSaveValues.menuAction())
        self.menuSetting.addAction(self.actionHardDelete)
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.actionSaveSetting)
        self.menuSaveValues.addAction(self.actionABS)
        self.menuSaveValues.addAction(self.actionREL)
        self.menuTools.addAction(self.actionAddupFolder)
        self.menuTools.addAction(self.actionMakeDataset)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LabelMaker", None))
        self.actionOpenFolder.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionAutoLabeling.setText(QCoreApplication.translate("MainWindow", u"Auto Save", None))
        self.actionABS.setText(QCoreApplication.translate("MainWindow", u"ABS", None))
        self.actionREL.setText(QCoreApplication.translate("MainWindow", u"REL", None))
        self.actionOpenFile.setText(QCoreApplication.translate("MainWindow", u"Open File(s)", None))
        self.actionOpenClassFile.setText(QCoreApplication.translate("MainWindow", u"Open Class File", None))
        self.actionHardDelete.setText(QCoreApplication.translate("MainWindow", u"Hard Delete", None))
        self.actionAddupFolder.setText(QCoreApplication.translate("MainWindow", u"Add up Folder", None))
        self.actionNewClassFile.setText(QCoreApplication.translate("MainWindow", u"New Class File", None))
        self.actionSaveSetting.setText(QCoreApplication.translate("MainWindow", u"Save Setting", None))
        self.actionMakeDataset.setText(QCoreApplication.translate("MainWindow", u"Make Dataset", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Files : ", None))
        self.filesLabel.setText("")
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.downButton.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.upButton.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        ___qtablewidgetitem = self.classTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Check", None));
        ___qtablewidgetitem1 = self.classTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem2 = self.classTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Class Number", None));
        ___qtablewidgetitem3 = self.labelTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem4 = self.labelTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem5 = self.labelTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"X Center", None));
        ___qtablewidgetitem6 = self.labelTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Y Center", None));
        ___qtablewidgetitem7 = self.labelTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"X Size", None));
        ___qtablewidgetitem8 = self.labelTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Y Size", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Label Path : ", None))
        self.classPathButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSetting.setTitle(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.menuSaveValues.setTitle(QCoreApplication.translate("MainWindow", u"Save Values", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

