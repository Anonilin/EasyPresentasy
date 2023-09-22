# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 592)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 30, 160, 521))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.SlideList = QFrame(self.verticalLayoutWidget)
        self.SlideList.setObjectName(u"SlideList")
        self.SlideList.setFrameShape(QFrame.StyledPanel)
        self.SlideList.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.SlideList)

        self.addBtn = QPushButton(self.centralwidget)
        self.addBtn.setObjectName(u"addBtn")
        self.addBtn.setGeometry(QRect(0, 550, 71, 41))
        self.remBtn = QPushButton(self.centralwidget)
        self.remBtn.setObjectName(u"remBtn")
        self.remBtn.setGeometry(QRect(80, 550, 71, 41))
        self.styleBox = QComboBox(self.centralwidget)
        self.styleBox.setObjectName(u"styleBox")
        self.styleBox.setGeometry(QRect(618, 10, 181, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 9, 131, 21))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 10, 47, 13))
        self.fileNameEdit = QLineEdit(self.centralwidget)
        self.fileNameEdit.setObjectName(u"fileNameEdit")
        self.fileNameEdit.setGeometry(QRect(50, 10, 113, 16))
        self.saveBtn = QPushButton(self.centralwidget)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setGeometry(QRect(170, 6, 75, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 40, 47, 13))
        self.label_3.setFont(font)
        self.titleEdit = QLineEdit(self.centralwidget)
        self.titleEdit.setObjectName(u"titleEdit")
        self.titleEdit.setGeometry(QRect(230, 36, 511, 20))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 70, 61, 16))
        self.label_4.setFont(font)
        self.subtitleEdit = QLineEdit(self.centralwidget)
        self.subtitleEdit.setObjectName(u"subtitleEdit")
        self.subtitleEdit.setGeometry(QRect(230, 70, 511, 20))
        self.img1 = QGraphicsView(self.centralwidget)
        self.img1.setObjectName(u"img1")
        self.img1.setGeometry(QRect(310, 110, 121, 101))
        self.img2 = QGraphicsView(self.centralwidget)
        self.img2.setObjectName(u"img2")
        self.img2.setGeometry(QRect(620, 110, 121, 101))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(170, 130, 131, 41))
        font1 = QFont()
        font1.setPointSize(24)
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(470, 130, 131, 41))
        self.label_6.setFont(font1)
        self.importImg1 = QPushButton(self.centralwidget)
        self.importImg1.setObjectName(u"importImg1")
        self.importImg1.setGeometry(QRect(190, 180, 75, 23))
        self.importImg2 = QPushButton(self.centralwidget)
        self.importImg2.setObjectName(u"importImg2")
        self.importImg2.setGeometry(QRect(490, 180, 75, 23))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(170, 220, 141, 41))
        self.label_7.setFont(font1)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(150, 30, 21, 561))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(380, 560, 151, 31))
        self.pushButton.setFont(font)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(170, 260, 621, 291))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.addBtn.setText(QCoreApplication.translate("MainWindow", u"Add slide", None))
        self.remBtn.setText(QCoreApplication.translate("MainWindow", u"Remove slide", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Presentation style:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"File name:", None))
        self.fileNameEdit.setPlaceholderText("")
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Title:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Subtitle:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Image 1:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Image 2:", None))
        self.importImg1.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.importImg2.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Slide text:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Accept", None))
    # retranslateUi

