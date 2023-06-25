# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LT.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(420, 130)
        Form.setMinimumSize(QSize(420, 130))
        Form.setMaximumSize(QSize(420, 130))
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, 3, 6, 3)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.doButton = QPushButton(Form)
        self.doButton.setObjectName(u"doButton")
        self.doButton.setEnabled(False)
        self.doButton.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.doButton, 4, 0, 1, 1)

        self.relRadioButton = QRadioButton(Form)
        self.relRadioButton.setObjectName(u"relRadioButton")
        self.relRadioButton.setChecked(True)

        self.gridLayout.addWidget(self.relRadioButton, 1, 0, 1, 1)

        self.labelSearchButton = QPushButton(Form)
        self.labelSearchButton.setObjectName(u"labelSearchButton")
        self.labelSearchButton.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.labelSearchButton, 3, 2, 1, 1)

        self.cancelButton = QPushButton(Form)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.cancelButton, 4, 2, 1, 1)

        self.absRadioButton = QRadioButton(Form)
        self.absRadioButton.setObjectName(u"absRadioButton")

        self.gridLayout.addWidget(self.absRadioButton, 0, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.labelLineEdit = QLineEdit(Form)
        self.labelLineEdit.setObjectName(u"labelLineEdit")
        self.labelLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.labelLineEdit, 3, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.imageLineEdit = QLineEdit(Form)
        self.imageLineEdit.setObjectName(u"imageLineEdit")

        self.gridLayout.addWidget(self.imageLineEdit, 2, 1, 1, 1)

        self.imageSearchButton = QPushButton(Form)
        self.imageSearchButton.setObjectName(u"imageSearchButton")

        self.gridLayout.addWidget(self.imageSearchButton, 2, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Make Dataset ", None))
        self.doButton.setText(QCoreApplication.translate("Form", u"Do", None))
        self.relRadioButton.setText(QCoreApplication.translate("Form", u"REL", None))
        self.labelSearchButton.setText(QCoreApplication.translate("Form", u"Search", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.absRadioButton.setText(QCoreApplication.translate("Form", u"ABS", None))
        self.label.setText(QCoreApplication.translate("Form", u"Image Folder", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Label Folder", None))
        self.imageSearchButton.setText(QCoreApplication.translate("Form", u"Search", None))
    # retranslateUi

