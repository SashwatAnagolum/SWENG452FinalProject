# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(823, 146)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(10, 50, 81, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(48)
        self.text1.setFont(font)
        self.text1.setText("")
        self.text1.setObjectName("text1")
        self.heading1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.heading1.setGeometry(QtCore.QRect(10, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(24)
        self.heading1.setFont(font)
        self.heading1.setText("")
        self.heading1.setObjectName("heading1")
        self.text2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.text2.setGeometry(QtCore.QRect(130, 50, 81, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(48)
        self.text2.setFont(font)
        self.text2.setText("")
        self.text2.setObjectName("text2")
        self.text3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.text3.setGeometry(QtCore.QRect(250, 50, 81, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(48)
        self.text3.setFont(font)
        self.text3.setText("")
        self.text3.setObjectName("text3")
        self.divider2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.divider2.setGeometry(QtCore.QRect(210, 60, 31, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(48)
        self.divider2.setFont(font)
        self.divider2.setText("")
        self.divider2.setObjectName("divider2")
        self.divider1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.divider1.setGeometry(QtCore.QRect(90, 60, 31, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(48)
        self.divider1.setFont(font)
        self.divider1.setText("")
        self.divider1.setObjectName("divider1")
        self.heading2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.heading2.setGeometry(QtCore.QRect(370, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(24)
        self.heading2.setFont(font)
        self.heading2.setText("")
        self.heading2.setObjectName("heading2")
        self.divider3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.divider3.setGeometry(QtCore.QRect(450, 60, 31, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(48)
        self.divider3.setFont(font)
        self.divider3.setText("")
        self.divider3.setObjectName("divider3")
        self.text5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.text5.setGeometry(QtCore.QRect(490, 50, 81, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(48)
        self.text5.setFont(font)
        self.text5.setText("")
        self.text5.setObjectName("text5")
        self.text4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.text4.setGeometry(QtCore.QRect(370, 50, 81, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(48)
        self.text4.setFont(font)
        self.text4.setText("")
        self.text4.setObjectName("text4")
        self.text6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.text6.setGeometry(QtCore.QRect(610, 50, 81, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(48)
        self.text6.setFont(font)
        self.text6.setText("")
        self.text6.setObjectName("text6")
        self.divider4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.divider4.setGeometry(QtCore.QRect(570, 60, 31, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(48)
        self.divider4.setFont(font)
        self.divider4.setText("")
        self.divider4.setObjectName("divider4")
        self.pushButton1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(700, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(700, 50, 111, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(700, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName("pushButton3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton1.clicked.connect(MainWindow.button1_pressed) # type: ignore
        self.pushButton2.clicked.connect(MainWindow.button2_pressed) # type: ignore
        self.pushButton3.clicked.connect(MainWindow.button3_pressed) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton1.setText(_translate("MainWindow", "Power"))
        self.pushButton2.setText(_translate("MainWindow", "Input"))
        self.pushButton3.setText(_translate("MainWindow", "Mode"))
