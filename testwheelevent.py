#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 12:39:40 2020

@author: ernie
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 23:46:40 2020

@author: ernie
"""
import sys
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsTextItem, QApplication, QMainWindow, QLabel 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QWheelEvent
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt

from assignment1 import outPutFor1A

class Window(QMainWindow):
    
   
    def __init__(self):
        super().__init__()
      
        self.introLabel = QLabel(self)
        self.introLabel.setText("rotates the mouse wheel, or presses the ‘up’ or ‘down’ arrow keys, to change to a different slice")
        self.introLabel.setGeometry(700, 10, 800, 20)
        
        self.label_imageDirectoryAndName = QtWidgets.QLabel(self)
        self.label_imageDirectoryAndName.setGeometry(QtCore.QRect(0, 130, 461, 31))
        self.label_imageDirectoryAndName.setObjectName("label_imageDirectoryAndName")
        self.label_imageDirectoryAndName.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
        self.label_imageSliceValue = QtWidgets.QLabel(self)
        self.label_imageSliceValue.setGeometry(QtCore.QRect(0, 160, 461, 21))
        self.label_imageSliceValue.setObjectName("label_imageSliceValue")
        self.label_imageSliceValue.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
        self.label_imageDirection = QtWidgets.QLabel(self)
        self.label_imageDirection.setGeometry(QtCore.QRect(0, 190, 461, 21))
        self.label_imageDirection.setObjectName("label_imageDirection")
        self.label_imageDirection.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
        self.txt_input_imageDirectoryAndName = QtWidgets.QLineEdit(self)
        self.txt_input_imageDirectoryAndName.setGeometry(QtCore.QRect(380, 140, 201, 21))
        self.txt_input_imageDirectoryAndName.setObjectName("txt_input_imageDirectoryAndName")
        
        self.txt_input_imageSliceValue = QtWidgets.QLineEdit(self)
        self.txt_input_imageSliceValue.setGeometry(QtCore.QRect(380, 165, 201, 21))
        self.txt_input_imageSliceValue.setObjectName("txt_input_imageSliceValue")
        
        self.txt_input_imageDirection = QtWidgets.QLineEdit(self)
        self.txt_input_imageDirection.setGeometry(QtCore.QRect(380, 190, 201, 21))
        self.txt_input_imageDirection.setObjectName("txt_input_imageDirection")
        
        
        self.btn_submit = QtWidgets.QPushButton(self)
        self.btn_submit.setGeometry(QtCore.QRect(380, 240, 211, 32))
        self.btn_submit.setObjectName("btn_submit")
        
        self.text_title = QtWidgets.QTextEdit(self)
        self.text_title.setGeometry(QtCore.QRect(60, 10, 400, 51))
        self.text_title.setObjectName("text_title")
        
        self.label_imageDirectoryAndName.setText("Enter ImageDirection And Image Name, ex: 'images/t1.nii' :")
        self.label_imageSliceValue.setText("Enter Slice value, ex '250' : ")
        self.label_imageDirection.setText("Enter Direction, ex 'axial' or 'sagittal' or 'coronal' : ")
        
        self.rawImageLabel = QLabel(self)
        self.rawImageLabelTitle = QLabel(self)
        
        self.btn_submit.setText("Submit")



        self.text_title.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#cf0f39;\">Viewer For Question 1A </span></p></body></html>")
        

        self.btn_submit.clicked.connect(self.btn_submit_handler)
      
        
        self.setWindowTitle("Question 1A")        
        self.setGeometry(0, 0, 1700, 600)
        self.show()
    
    imagesSource = []
    def btn_submit_handler(self):
        
        
        self.txt_input_imageDirectoryAndName.clearFocus()
        self.txt_input_imageSliceValue.clearFocus()
        self.txt_input_imageDirection.clearFocus()
        
        imageDirectoryAndName = self.txt_input_imageDirectoryAndName.text()
        imageSliceValue = int(self.txt_input_imageSliceValue.text())
        imageDirection = self.txt_input_imageDirection.text()
        
        
        outPutFor1A(imageDirectoryAndName, imageSliceValue, imageDirection)
        
        
        rawImage = QPixmap(imageDirection).scaledToWidth(256)
        print(rawImage.width())
        
        self.rawImageLabel.setPixmap(rawImage)
        self.rawImageLabel.setGeometry(700, 50, rawImage.width(), rawImage.height())
        

        self.rawImageLabelTitle.setText("raw Image")
        self.rawImageLabelTitle.setGeometry(700, 30, rawImage.width(), 20)
        
        
        outPutFor1A(imageDirectoryAndName, imageSliceValue, 'axial')
        outPutFor1A(imageDirectoryAndName, imageSliceValue, 'sagittal')
        outPutFor1A(imageDirectoryAndName, imageSliceValue, 'coronal')
        self.imagesSource = [QPixmap("axial.png"),QPixmap("sagittal.png"),QPixmap("coronal.png")]
        
        
        #self.show()
        
        
    
    def wheelEvent(self, event):
        self.changePics()
    def keyPressEvent(self, event):
        if event.key() == event.key() in [ Qt.Key_Left, Qt.Key_Right, Qt.Key_Up, Qt.Key_Down ]:
           self.changePics()    
    
    a = [0,0,0] #flag 
    def changePics(self):
        if (self.a[0] == 0 and self.a[1] == 0 and self.a[2] == 0):
           self.rawImageLabel.setPixmap(self.imagesSource[0])
           self.rawImageLabel.setGeometry(700, 50, self.imagesSource[0].width(), self.imagesSource[0].height())
           self.a[0] = 1
           self.a[1] = 0
           self.a[2] = 0
        elif (self.a[0] == 1 and self.a[1] == 0 and self.a[2] == 0):
           self.rawImageLabel.setPixmap(self.imagesSource[1])
           self.rawImageLabel.setGeometry(700, 50, self.imagesSource[1].width(), self.imagesSource[1].height())
           self.a[0] = 0
           self.a[1] = 1
           self.a[2] = 0
        elif (self.a[0] == 0 and self.a[1] == 1 and self.a[2] == 0):
           self.rawImageLabel.setPixmap(self.imagesSource[2])
           self.rawImageLabel.setGeometry(700, 50, self.imagesSource[2].width(), self.imagesSource[2].height())
           self.a[0] = 0
           self.a[1] = 0
           self.a[2] = 1
        elif (self.a[0] == 0 and self.a[1] == 0 and self.a[2] == 1):
           self.rawImageLabel.setPixmap(self.imagesSource[0])
           self.rawImageLabel.setGeometry(700, 50, self.imagesSource[0].width(), self.imagesSource[0].height())
           self.a[0] = 0
           self.a[1] = 0
           self.a[2] = 0
           
           
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
