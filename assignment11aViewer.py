#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:49:08 2020

@author: ernie
"""
import sys
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsTextItem, QApplication, QMainWindow, QLabel 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QWheelEvent
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets

from assignment1 import outPutFor1A


class Ui_Form(QMainWindow):

    def openwindow(self, valueToTransfer):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Page2(self)
        self.ui.setupUi(self.window, valueToTransfer)
        
        Form.hide()
        self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(734, 428)
        self.label_imageDirectoryAndName = QtWidgets.QLabel(Form)
        self.label_imageDirectoryAndName.setGeometry(QtCore.QRect(0, 130, 461, 31))
        self.label_imageDirectoryAndName.setObjectName("label_imageDirectoryAndName")
        self.label_imageDirectoryAndName.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
        self.label_imageSliceValue = QtWidgets.QLabel(Form)
        self.label_imageSliceValue.setGeometry(QtCore.QRect(0, 160, 461, 21))
        self.label_imageSliceValue.setObjectName("label_imageSliceValue")
        self.label_imageSliceValue.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
        self.label_imageDirection = QtWidgets.QLabel(Form)
        self.label_imageDirection.setGeometry(QtCore.QRect(0, 190, 461, 21))
        self.label_imageDirection.setObjectName("label_imageDirection")
        self.label_imageDirection.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
        self.txt_input_imageDirectoryAndName = QtWidgets.QLineEdit(Form)
        self.txt_input_imageDirectoryAndName.setGeometry(QtCore.QRect(380, 140, 201, 21))
        self.txt_input_imageDirectoryAndName.setObjectName("txt_input_imageDirectoryAndName")
        
        self.txt_input_imageSliceValue = QtWidgets.QLineEdit(Form)
        self.txt_input_imageSliceValue.setGeometry(QtCore.QRect(380, 165, 201, 21))
        self.txt_input_imageSliceValue.setObjectName("txt_input_imageSliceValue")
        
        self.txt_input_imageDirection = QtWidgets.QLineEdit(Form)
        self.txt_input_imageDirection.setGeometry(QtCore.QRect(380, 190, 201, 21))
        self.txt_input_imageDirection.setObjectName("txt_input_imageDirection")
        
        
        self.btn_submit = QtWidgets.QPushButton(Form)
        self.btn_submit.setGeometry(QtCore.QRect(380, 240, 211, 32))
        self.btn_submit.setObjectName("btn_submit")
        
        self.text_title = QtWidgets.QTextEdit(Form)
        self.text_title.setGeometry(QtCore.QRect(60, 10, 629, 51))
        self.text_title.setObjectName("text_title")
        
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login Page"))
        self.label_imageDirectoryAndName.setText(_translate("Form", "Enter ImageDirection And Image Name, ex: 'images/t1.nii' :"))
        self.label_imageSliceValue.setText(_translate("Form", "Enter Slice value, ex '250' : "))
        self.label_imageDirection.setText(_translate("Form", "Enter Direction, ex 'axial' or 'sagittal' or 'coronal' : "))
        
        self.btn_submit.setText(_translate("Form", "Submit"))



        self.text_title.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#cf0f39;\">Viewer For Question 1A </span></p></body></html>"))
        

        self.btn_submit.clicked.connect(self.btn_submit_handler)

    
        
    def btn_submit_handler(self):

        imageDirectoryAndName = self.txt_input_imageDirectoryAndName.text()
        imageSliceValue = self.txt_input_imageSliceValue.text()
        imageDirection = self.txt_input_imageDirection.text()
        
        valueTransferForNextPage = []
        valueTransferForNextPage.append(imageDirectoryAndName)
        valueTransferForNextPage.append(imageSliceValue)
        valueTransferForNextPage.append(imageDirection)
        
        self.openwindow(valueTransferForNextPage)
        
        #Page2.show()
        #self.ui.btn_sumbit.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(0))


class Ui_Page2(QMainWindow):

    def openwindow(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    imagesSource = []
    def setupUi(self, Page2, valueToTransfer):

        Page2.setObjectName("Page2")
        Page2.resize(800, 1000)
        
        imageDirectoryAndName = valueToTransfer[0]
        imageSliceValue = int(valueToTransfer[1])
        imageDirection = valueToTransfer[2]

        outPutFor1A(imageDirectoryAndName, imageSliceValue, imageDirection)
        
        
        rawImage = QPixmap(imageDirection).scaledToWidth(256)
        self.rawImageLabel = QLabel(Page2)
        self.rawImageLabel.setPixmap(rawImage)
        self.rawImageLabel.setGeometry(0, 50, rawImage.width(), rawImage.height())
        
        self.rawImageLabelTitle = QLabel(Page2)
        self.rawImageLabelTitle.setText("raw Image")
        self.rawImageLabelTitle.setGeometry(0, 30, rawImage.width(), 20)
        
        
        outPutFor1A(imageDirectoryAndName, imageSliceValue, 'axial')
        outPutFor1A(imageDirectoryAndName, imageSliceValue, 'sagittal')
        outPutFor1A(imageDirectoryAndName, imageSliceValue, 'coronal')
        self.imagesSource = [QPixmap("axial.png"),QPixmap("sagittal.png"),QPixmap("coronal.png")]
        
        
        self.btn_back = QtWidgets.QPushButton(Page2)
        self.btn_back.setGeometry(QtCore.QRect(0, 0, 113, 32))
        self.btn_back.setObjectName("btn_back")

        self.retranslateUi(Page2)
        QtCore.QMetaObject.connectSlotsByName(Page2)

    def retranslateUi(self, Page2):
        _translate = QtCore.QCoreApplication.translate
        Page2.setWindowTitle(_translate("Page2", "Form"))
        
        self.btn_back.setText(_translate("Page2", "Back"))
        self.btn_back.clicked.connect(self.button_handler_back)

    def button_handler_back(self):
        self.openwindow()

    
    
    def wheelEvent(self, event):
        print(1111)
        self.changePics()
    def keyPressEvent(self, event):
        if event.key() == event.key() in [ Qt.Key_Left, Qt.Key_Right, Qt.Key_Up, Qt.Key_Down ]:
           self.changePics()    
    
    a = [0,0,0] #flag 
    def changePics(self):
        print("123")
        if (self.a[0] == 0 and self.a[1] == 0 and self.a[2] == 0):
           self.rawImageLabel.setPixmap(self.imagesSource[0])
           self.rawImageLabel.setGeometry(0, 30, self.imagesSource[0].width(), self.imagesSource[0].height())
           self.a[0] = 1
           self.a[1] = 0
           self.a[2] = 0
        elif (self.a[0] == 1 and self.a[1] == 0 and self.a[2] == 0):
           self.label.setPixmap(self.imagesSource[1])
           self.label.setGeometry(0, 30, self.imagesSource[1].width(), self.imagesSource[1].height())
           self.a[0] = 0
           self.a[1] = 1
           self.a[2] = 0
        elif (self.a[0] == 0 and self.a[1] == 1 and self.a[2] == 0):
           self.label.setPixmap(self.imagesSource[2])
           self.label.setGeometry(0, 30, self.imagesSource[2].width(), self.imagesSource[2].height())
           self.a[0] = 0
           self.a[1] = 0
           self.a[2] = 1
        elif (self.a[0] == 0 and self.a[1] == 0 and self.a[2] == 1):
           self.label.setPixmap(self.imagesSource[0])
           self.label.setGeometry(0, 30, self.imagesSource[0].width(), self.imagesSource[0].height())
           self.a[0] = 0
           self.a[1] = 0
           self.a[2] = 0


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())