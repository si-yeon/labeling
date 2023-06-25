# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FC.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(487, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(400, 90))
        Form.setMaximumSize(QSize(16666, 16666))
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 3, 0, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)

        self.pathLineEdit = QLineEdit(Form)
        self.pathLineEdit.setObjectName(u"pathLineEdit")
        self.pathLineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.pathLineEdit, 2, 1, 1, 1)

        self.findButton = QPushButton(Form)
        self.findButton.setObjectName(u"findButton")

        self.gridLayout_3.addWidget(self.findButton, 2, 2, 1, 1)

        self.classLineEdit = QLineEdit(Form)
        self.classLineEdit.setObjectName(u"classLineEdit")

        self.gridLayout_3.addWidget(self.classLineEdit, 0, 1, 1, 2)

        self.classNumberLineEdit = QLineEdit(Form)
        self.classNumberLineEdit.setObjectName(u"classNumberLineEdit")
        self.classNumberLineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.classNumberLineEdit, 1, 1, 1, 2)

        self.filesLineEdit = QLineEdit(Form)
        self.filesLineEdit.setObjectName(u"filesLineEdit")
        self.filesLineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.filesLineEdit, 3, 1, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.findFolderButton = QPushButton(Form)
        self.findFolderButton.setObjectName(u"findFolderButton")

        self.gridLayout.addWidget(self.findFolderButton, 0, 1, 1, 1)

        self.cancelButton = QPushButton(Form)
        self.cancelButton.setObjectName(u"cancelButton")

        self.gridLayout.addWidget(self.cancelButton, 0, 4, 1, 1)

        self.doButton = QPushButton(Form)
        self.doButton.setObjectName(u"doButton")
        self.doButton.setEnabled(False)

        self.gridLayout.addWidget(self.doButton, 0, 3, 1, 1)

        self.findFileButton = QPushButton(Form)
        self.findFileButton.setObjectName(u"findFileButton")

        self.gridLayout.addWidget(self.findFileButton, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        QWidget.setTabOrder(self.classLineEdit, self.classNumberLineEdit)
        QWidget.setTabOrder(self.classNumberLineEdit, self.pathLineEdit)
        QWidget.setTabOrder(self.pathLineEdit, self.findButton)
        QWidget.setTabOrder(self.findButton, self.filesLineEdit)
        QWidget.setTabOrder(self.filesLineEdit, self.findFileButton)
        QWidget.setTabOrder(self.findFileButton, self.findFolderButton)
        QWidget.setTabOrder(self.findFolderButton, self.doButton)
        QWidget.setTabOrder(self.doButton, self.cancelButton)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"FileConcat", None))
        self.label.setText(QCoreApplication.translate("Form", u"Files", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Class Name", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Class Number", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Path", None))
        self.findButton.setText(QCoreApplication.translate("Form", u"Find", None))
        self.classLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Input Class Name", None))
        self.filesLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"You need to add a file.", None))
        self.findFolderButton.setText(QCoreApplication.translate("Form", u"Find Folder", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.doButton.setText(QCoreApplication.translate("Form", u"Do", None))
        self.findFileButton.setText(QCoreApplication.translate("Form", u"Find Files", None))
    # retranslateUi

