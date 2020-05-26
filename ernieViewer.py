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


from assignment1 import outPutImage

class Window(QMainWindow):
    
    imagesSource = []
    def __init__(self):
        super().__init__()
        self.top = 100
        self.left = 100
        self.width = 100
        self.height = 100
        
        self.introLabel = QLabel(self)
        self.introLabel.setText("rotates the mouse wheel, or presses the ‘up’ or ‘down’ arrow keys, to change to a different slice")
        self.introLabel.setGeometry(0, 0, 800, 20)
        
        self.label = QLabel(self)
        
        #prepare images
        outPutImage("axial", 250)
        outPutImage("sagittal", 190)
        outPutImage("coronal", 190)
        self.label.setPixmap(QPixmap("axial.png"))
        self.imagesSource = [QPixmap("axial.png"),QPixmap("sagittal.png"),QPixmap("coronal.png")]
        
        #init window with axial pic
        self.label.setGeometry(0, 20, self.imagesSource[0].width(), self.imagesSource[0].height())
        
        
        
        self.setGeometry(0, 0, 800, 800)
        self.show()

   
    def wheelEvent(self, event):
       self.changePics()
    def keyPressEvent(self, event):
       if event.key() == event.key() in [ Qt.Key_Left, Qt.Key_Right, Qt.Key_Up, Qt.Key_Down ]:
           self.changePics()    
    
    a = [0,0,0] #flag 
    def changePics(self):
         if (self.a[0] == 0 and self.a[1] == 0 and self.a[2] == 0):
            self.label.setPixmap(self.imagesSource[0])
            self.label.setGeometry(0, 20, self.imagesSource[0].width(), self.imagesSource[0].height())
            self.a[0] = 1
            self.a[1] = 0
            self.a[2] = 0
         elif (self.a[0] == 1 and self.a[1] == 0 and self.a[2] == 0):
            self.label.setPixmap(self.imagesSource[1])
            self.label.setGeometry(0, 20, self.imagesSource[1].width(), self.imagesSource[1].height())
            self.a[0] = 0
            self.a[1] = 1
            self.a[2] = 0
         elif (self.a[0] == 0 and self.a[1] == 1 and self.a[2] == 0):
            self.label.setPixmap(self.imagesSource[2])
            self.label.setGeometry(0, 20, self.imagesSource[2].width(), self.imagesSource[2].height())
            self.a[0] = 0
            self.a[1] = 0
            self.a[2] = 1
         elif (self.a[0] == 0 and self.a[1] == 0 and self.a[2] == 1):
            self.label.setPixmap(self.imagesSource[0])
            self.label.setGeometry(0, 20, self.imagesSource[0].width(), self.imagesSource[0].height())
            self.a[0] = 0
            self.a[1] = 0
            self.a[2] = 0
            
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())