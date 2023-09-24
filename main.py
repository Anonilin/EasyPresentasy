from PyQt5 import QtWidgets, QtCore
from PyQt5 import uic
from tkinter.messagebox import showerror,showinfo
import sys
import ui # file with GUI
import generator # file for generate pptx file
from pptx import Presentation

class slide():
    def __init__(self):
        self.title="Title"
        self.subtitle="Subtitle"
        self.text = "Text"
        self.img1 = "image"
        self.img2 = "image_2"
        self.style = 0
        self.id = 0

class Window(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.slideList = []
        self.addBtn.clicked.connect(self.addSlide)
        self.remBtn.clicked.connect(self.removeSlide)
        
        self.mainWindowFrame = self.centralWidget
        self.slidesWindowFrame = self.SlideList

        self.saveBtn.clicked.connect(self.saveFile)

    def addSlide(self):
        print('Add')
        self.slideList.append(slide())
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
            self.slideBtn.show()
    
    def loadSlideData(self, index):
        print(index)
        self.pushButton.disconnect() # Save Slide Data
        currentSlide = self.slideList[index]
        self.titleEdit.setText(currentSlide.title)
        self.subtitleEdit.setText(currentSlide.subtitle)
        self.textEdit.setText(currentSlide.text)
        self.pushButton.clicked.connect(lambda checked, index=index: self.saveSlideData(index)) # Save Slide Data

        #print(currentSlide.title, currentSlide.subtitle, currentSlide.text)
    
    def saveSlideData(self, index):
        currentSlide = self.slideList[index]

        currentSlide.title = self.titleEdit.text()
        currentSlide.subtitle = self.subtitleEdit.text()
        currentSlide.text = self.textEdit.toPlainText()
        print("Saved")
        #print(self.slideList[x].title for x in range(len(self.slideList)+1))
    
    def saveFile(self):
        fileName = self.fileNameEdit.text()
        generator.generate(self.slideList, fileName)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()

    window.show()
    app.exec_()

if __name__=="__main__":
    main()
    
