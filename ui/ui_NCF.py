# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NCF.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(273, 305)
        Form.setMinimumSize(QSize(273, 305))
        Form.setMaximumSize(QSize(546, 610))
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEditTriggers(QAbstractItemView.DoubleClicked)

        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 3)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(86, 0))
        self.label.setMaximumSize(QSize(86, 16777215))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.nameLineEdit = QLineEdit(Form)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setMaxLength(32767)

        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 2)

        self.pathLineEdit = QLineEdit(Form)
        self.pathLineEdit.setObjectName(u"pathLineEdit")
        self.pathLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.pathLineEdit, 2, 0, 1, 2)

        self.searchButton = QPushButton(Form)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setMaximumSize(QSize(86, 16777215))

        self.gridLayout.addWidget(self.searchButton, 2, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addButton = QPushButton(Form)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setEnabled(False)
        self.addButton.setMinimumSize(QSize(60, 0))
        self.addButton.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.addButton)

        self.deleteButton = QPushButton(Form)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setEnabled(False)
        self.deleteButton.setMinimumSize(QSize(60, 0))
        self.deleteButton.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.deleteButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.makeFileButton = QPushButton(Form)
        self.makeFileButton.setObjectName(u"makeFileButton")
        self.makeFileButton.setEnabled(False)
        self.makeFileButton.setMinimumSize(QSize(0, 0))
        self.makeFileButton.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.makeFileButton)

        self.cancelButton = QPushButton(Form)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setMinimumSize(QSize(0, 0))
        self.cancelButton.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.cancelButton)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 3)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.classLineEdit = QLineEdit(Form)
        self.classLineEdit.setObjectName(u"classLineEdit")

        self.gridLayout.addWidget(self.classLineEdit, 3, 1, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        QWidget.setTabOrder(self.listWidget, self.nameLineEdit)
        QWidget.setTabOrder(self.nameLineEdit, self.pathLineEdit)
        QWidget.setTabOrder(self.pathLineEdit, self.searchButton)
        QWidget.setTabOrder(self.searchButton, self.classLineEdit)
        QWidget.setTabOrder(self.classLineEdit, self.addButton)
        QWidget.setTabOrder(self.addButton, self.deleteButton)
        QWidget.setTabOrder(self.deleteButton, self.makeFileButton)
        QWidget.setTabOrder(self.makeFileButton, self.cancelButton)

        self.retranslateUi(Form)

        self.listWidget.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"New Class File", None))
        self.label.setText(QCoreApplication.translate("Form", u"File Name :", None))
        self.nameLineEdit.setInputMask("")
        self.nameLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Input Name", None))
        self.searchButton.setText(QCoreApplication.translate("Form", u"Search", None))
        self.addButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.deleteButton.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.makeFileButton.setText(QCoreApplication.translate("Form", u"Make File", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Class Name :", None))
        self.classLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Input Name", None))
    # retranslateUi

