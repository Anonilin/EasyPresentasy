# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 160, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SlideList = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.SlideList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SlideList.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SlideList.setObjectName("SlideList")
        self.verticalLayout.addWidget(self.SlideList)
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(0, 550, 71, 41))
        self.addBtn.setObjectName("addBtn")
        self.remBtn = QtWidgets.QPushButton(self.centralwidget)
        self.remBtn.setGeometry(QtCore.QRect(80, 550, 71, 41))
        self.remBtn.setObjectName("remBtn")
        self.styleBox = QtWidgets.QComboBox(self.centralwidget)
        self.styleBox.setGeometry(QtCore.QRect(618, 10, 181, 22))
        self.styleBox.setObjectName("styleBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 9, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 47, 13))
        self.label_2.setObjectName("label_2")
        self.fileNameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.fileNameEdit.setGeometry(QtCore.QRect(50, 10, 113, 16))
        self.fileNameEdit.setPlaceholderText("")
        self.fileNameEdit.setObjectName("fileNameEdit")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(170, 6, 75, 21))
        self.saveBtn.setObjectName("saveBtn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 40, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.titleEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.titleEdit.setGeometry(QtCore.QRect(230, 36, 511, 20))
        self.titleEdit.setObjectName("titleEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.subtitleEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.subtitleEdit.setGeometry(QtCore.QRect(230, 70, 511, 20))
        self.subtitleEdit.setObjectName("subtitleEdit")
        self.img1 = QtWidgets.QGraphicsView(self.centralwidget)
        self.img1.setGeometry(QtCore.QRect(310, 110, 121, 101))
        self.img1.setObjectName("img1")
        self.img2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.img2.setGeometry(QtCore.QRect(620, 110, 121, 101))
        self.img2.setObjectName("img2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 130, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 130, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.importImg1 = QtWidgets.QPushButton(self.centralwidget)
        self.importImg1.setGeometry(QtCore.QRect(190, 180, 75, 23))
        self.importImg1.setObjectName("importImg1")
        self.importImg2 = QtWidgets.QPushButton(self.centralwidget)
        self.importImg2.setGeometry(QtCore.QRect(490, 180, 75, 23))
        self.importImg2.setObjectName("importImg2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(170, 220, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(150, 30, 21, 561))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 560, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 260, 621, 291))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addBtn.setText(_translate("MainWindow", "Add slide"))
        self.remBtn.setText(_translate("MainWindow", "Remove slide"))
        self.label.setText(_translate("MainWindow", "Presentation style:"))
        self.label_2.setText(_translate("MainWindow", "File name:"))
        self.saveBtn.setText(_translate("MainWindow", "Save"))
        self.label_3.setText(_translate("MainWindow", "Title:"))
        self.label_4.setText(_translate("MainWindow", "Subtitle:"))
        self.label_5.setText(_translate("MainWindow", "Image 1:"))
        self.label_6.setText(_translate("MainWindow", "Image 2:"))
        self.importImg1.setText(_translate("MainWindow", "Import"))
        self.importImg2.setText(_translate("MainWindow", "Import"))
        self.label_7.setText(_translate("MainWindow", "Slide text:"))
        self.pushButton.setText(_translate("MainWindow", "Accept"))
