# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 153)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.text1 = QLabel(self.centralwidget)
        self.text1.setObjectName(u"text1")
        self.text1.setGeometry(QRect(10, 50, 81, 71))
        font = QFont()
        font.setFamilies([u"OCR A Extended"])
        font.setPointSize(48)
        self.text1.setFont(font)
        self.heading1 = QLabel(self.centralwidget)
        self.heading1.setObjectName(u"heading1")
        self.heading1.setGeometry(QRect(10, 10, 171, 41))
        font1 = QFont()
        font1.setFamilies([u"OCR A Extended"])
        font1.setPointSize(24)
        self.heading1.setFont(font1)
        self.text2 = QLabel(self.centralwidget)
        self.text2.setObjectName(u"text2")
        self.text2.setGeometry(QRect(130, 50, 81, 71))
        self.text2.setFont(font)
        self.text3 = QLabel(self.centralwidget)
        self.text3.setObjectName(u"text3")
        self.text3.setGeometry(QRect(250, 50, 81, 71))
        self.text3.setFont(font)
        self.divider2 = QLabel(self.centralwidget)
        self.divider2.setObjectName(u"divider2")
        self.divider2.setGeometry(QRect(210, 60, 31, 61))
        self.divider2.setFont(font)
        self.divider1 = QLabel(self.centralwidget)
        self.divider1.setObjectName(u"divider1")
        self.divider1.setGeometry(QRect(90, 60, 31, 61))
        self.divider1.setFont(font)
        self.heading2 = QLabel(self.centralwidget)
        self.heading2.setObjectName(u"heading2")
        self.heading2.setGeometry(QRect(370, 10, 171, 41))
        self.heading2.setFont(font1)
        self.divider3 = QLabel(self.centralwidget)
        self.divider3.setObjectName(u"divider3")
        self.divider3.setGeometry(QRect(450, 60, 31, 61))
        self.divider3.setFont(font)
        self.text5 = QLabel(self.centralwidget)
        self.text5.setObjectName(u"text5")
        self.text5.setGeometry(QRect(490, 50, 81, 71))
        self.text5.setFont(font)
        self.text4 = QLabel(self.centralwidget)
        self.text4.setObjectName(u"text4")
        self.text4.setGeometry(QRect(370, 50, 81, 71))
        self.text4.setFont(font)
        self.text6 = QLabel(self.centralwidget)
        self.text6.setObjectName(u"text6")
        self.text6.setGeometry(QRect(610, 50, 81, 71))
        self.text6.setFont(font)
        self.divider4 = QLabel(self.centralwidget)
        self.divider4.setObjectName(u"divider4")
        self.divider4.setGeometry(QRect(570, 60, 31, 61))
        self.divider4.setFont(font)
        self.pushButton1 = QPushButton(self.centralwidget)
        self.pushButton1.setObjectName(u"pushButton1")
        self.pushButton1.setGeometry(QRect(700, 10, 111, 31))
        font2 = QFont()
        font2.setFamilies([u"OCR A Extended"])
        self.pushButton1.setFont(font2)
        self.pushButton2 = QPushButton(self.centralwidget)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setGeometry(QRect(700, 40, 111, 31))
        self.pushButton2.setFont(font2)
        self.pushButton3 = QPushButton(self.centralwidget)
        self.pushButton3.setObjectName(u"pushButton3")
        self.pushButton3.setGeometry(QRect(700, 70, 111, 31))
        self.pushButton3.setFont(font2)
        self.pushButton3_2 = QPushButton(self.centralwidget)
        self.pushButton3_2.setObjectName(u"pushButton3_2")
        self.pushButton3_2.setGeometry(QRect(700, 100, 111, 31))
        self.pushButton3_2.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton1.clicked.connect(MainWindow.button1_pressed)
        self.pushButton2.clicked.connect(MainWindow.button2_pressed)
        self.pushButton3.clicked.connect(MainWindow.button3_pressed)
        self.pushButton3_2.clicked.connect(MainWindow.button4_pressed)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.text1.setText("")
        self.heading1.setText("")
        self.text2.setText("")
        self.text3.setText("")
        self.divider2.setText("")
        self.divider1.setText("")
        self.heading2.setText("")
        self.divider3.setText("")
        self.text5.setText("")
        self.text4.setText("")
        self.text6.setText("")
        self.divider4.setText("")
        self.pushButton1.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.pushButton2.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.pushButton3.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.pushButton3_2.setText(QCoreApplication.translate("MainWindow", u"Input Select", None))
    # retranslateUi

