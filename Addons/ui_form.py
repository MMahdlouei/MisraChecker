# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(522, 340)
        MainWindow.setMinimumSize(QSize(522, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnanalyze = QPushButton(self.centralwidget)
        self.btnanalyze.setObjectName(u"btnanalyze")

        self.gridLayout.addWidget(self.btnanalyze, 2, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.filepath = QLineEdit(self.frame_2)
        self.filepath.setObjectName(u"filepath")

        self.horizontalLayout_2.addWidget(self.filepath)

        self.btnBrowseFile = QPushButton(self.frame_2)
        self.btnBrowseFile.setObjectName(u"btnBrowseFile")

        self.horizontalLayout_2.addWidget(self.btnBrowseFile)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 7)
        self.horizontalLayout_2.setStretch(2, 1)

        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.txtpath = QLineEdit(self.frame)
        self.txtpath.setObjectName(u"txtpath")

        self.horizontalLayout.addWidget(self.txtpath)

        self.btnBrowseText = QPushButton(self.frame)
        self.btnBrowseText.setObjectName(u"btnBrowseText")

        self.horizontalLayout.addWidget(self.btnBrowseText)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 7)
        self.horizontalLayout.setStretch(2, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnanalyze.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"File To Analyze", None))
        self.btnBrowseFile.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Text Rule File", None))
        self.btnBrowseText.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
    # retranslateUi

