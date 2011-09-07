#!/usr/bin/env python

#Filename: gui.py
#Author: Akhil K, Jithu Sunny, Rahul CP, Salim Ali
#Date: March 1, 2011
#Blog: http://jithusunnyk.blogspot.com/

import sys, serial
from PyQt4.QtGui import *
from PyQt4.QtCore import *

s = serial.Serial('/dev/ttyUSB0', 1200)

class Window(QWidget):
    def button_clicked(self, code):
        s.write(code)
        print code
        
    def key_pressed(self, code):
        s.write(code)
        print code

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            self.key_pressed('.f')
        elif event.key() == Qt.Key_Z:
            self.key_pressed('.b')
        elif event.key() == Qt.Key_A:
            self.key_pressed('.l')
        elif event.key() == Qt.Key_Q:
            self.key_pressed('.L')
        elif event.key() == Qt.Key_S:
            self.key_pressed('.r')
        elif event.key() == Qt.Key_E:
            self.key_pressed('.R')
        elif event.key() == Qt.Key_X:
            self.key_pressed('.h')            
                        
    def __init__(self):
        QWidget.__init__(self, parent = None)

        #Button creation
        forward_button = QPushButton("Forward")
        reverse_button = QPushButton("Reverse")
        left_button = QPushButton("Left")
        s_left_button = QPushButton("Sharp Left")
        right_button = QPushButton("Right")
        s_right_button = QPushButton("Sharp Right")
        brake_button = QPushButton("Brake")

        #Connecting the buttons with the function button_clicked
        forward_button.clicked.connect(lambda: self.button_clicked('.f'))
        reverse_button.clicked.connect(lambda: self.button_clicked('.b'))
        left_button.clicked.connect(lambda: self.button_clicked('.l'))
        s_left_button.clicked.connect(lambda: self.button_clicked('.L'))
        right_button.clicked.connect(lambda: self.button_clicked('.r'))
        s_right_button.clicked.connect(lambda: self.button_clicked('.R'))
        brake_button.clicked.connect(lambda: self.button_clicked('.h'))
        
        
        #Setting the layout
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(forward_button, 1, 1)
        grid.addWidget(reverse_button, 4, 1)
        grid.addWidget(left_button, 2, 0)
        grid.addWidget(s_left_button, 3, 0)
        grid.addWidget(right_button, 2, 2)
        grid.addWidget(s_right_button, 3, 2)

        vbox = QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addWidget(brake_button)

        self.setLayout(vbox)

        #Centering the window
        screen = QDesktopWidget().screenGeometry()
        mysize = self.geometry()
        hpos = ( screen.width() - mysize.width() ) / 2
        vpos = ( screen.height() - mysize.height() ) / 2
        self.move(hpos, vpos)
        
        self.resize(300, 350)
        
if __name__=="__main__" :
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
