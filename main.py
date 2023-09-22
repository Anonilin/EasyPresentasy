from PyQt5 import QtWidgets, QtCore
from PyQt5 import uic
from tkinter.messagebox import showerror
import sys
import ui

class slide():
    title="Title"
    subtitle="Subtitle"
    text = "Text"
    img1 = "image"
    img2 = "image_2"
    style = 0
    id = 0

class Window(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.slideList = []
        self.addBtn.clicked.connect(self.addSlide)
        self.remBtn.clicked.connect(self.removeSlide)
        
        self.mainWindowFrame = self.centralWidget
        self.slidesWindowFrame = self.SlideList

    def addSlide(self):
        print('Add')
        self.slideList.append(slide)
        return self.refreshSlideList()
    
    def removeSlide(self):
        self.slideList.pop() if len(self.slideList) > 0 else showerror("So deep!", "All slides was removed")
        return self.refreshSlideList()
    
    def refreshSlideList(self):

        buttons = self.slidesWindowFrame.findChildren(QtWidgets.QPushButton)
        
        print(len(self.slideList))

        for button in buttons:
            button.deleteLater()

        for i in range(len(self.slideList)):
            self.slideList[i].id = i
            self.slideBtn = QtWidgets.QPushButton(self.slidesWindowFrame)
            self.slideBtn.setGeometry(QtCore.QRect(0,i*30,150,30))
            self.slideBtn.setObjectName(f"slide_{i}")
            self.slideBtn.setText(f"Slide {i+1}")
            self.slideBtn.clicked.connect(lambda checked, button=self.slideBtn, i=i: self.loadSlideData(i))
            self.pushButton.clicked.connect(lambda checked, button=self.pushButton, i=i: self.saveSlideData(i)) # Save Slide Data
            self.slideBtn.show()
    
    def loadSlideData(self, index):
        print(index)
        currentSlide = self.slideList[index]
        self.titleEdit.setText(currentSlide.title)
        self.subtitleEdit.setText(currentSlide.subtitle)
        self.textEdit.setText(currentSlide.text)

        print(currentSlide.title, currentSlide.subtitle, currentSlide.text)
    
    def saveSlideData(self, index):
        currentSlide = self.slideList[index]

        currentSlide.title = self.titleEdit.text()
        currentSlide.subtitle = self.subtitleEdit.text()
        currentSlide.text = self.textEdit.toPlainText()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()

    window.show()
    app.exec_()

if __name__=="__main__":
    main()
    
