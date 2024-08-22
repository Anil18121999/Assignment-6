

import datetime
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator
import subprocess, shutil, os, platform

'''
from print_test_popup import P_POP_TEST_Ui_MainWindow
from email_popup_test_report import popup_email_test_Ui_MainWindow
from comment_popup import comment_Ui_MainWindow
from TY_07_UTM_MANNUAL_CONTROL_3 import  TY_07_3_Ui_MainWindow
from pop_graph_data import pop_graph_data_Ui_MainWindow
'''
import inspect

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.Qt import QTableWidgetItem

### ##### This Lib is for General Purpose.
import sqlite3
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import datetime
import random
import serial,time
import array  as arr
import numpy as np

### This lib is for Graph only 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import re

#### PDF creation Libs ########
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY 
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import portrait,landscape, letter,inch,A4
from reportlab.lib import colors
from reportlab.graphics.shapes import Line, Drawing
import sys
import os


class TY_74_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.load_unit = ""
        self.initial_values = []
        self.kg_to_lb = []
        self.kg_to_N = []
        self.kg_to_gm = []
        self.lb_to_kg = []
        self.lb_to_N = []
        self.lb_to_gm = []
        self.N_to_kg = []
        self.N_to_lb = []
        self.N_to_gm = []
        self.gm_to_kg = []
        self.gm_to_lb = []
        self.gm_to_N = []
        self.mm_to_inch = []
        self.inch_to_mm = []
        self.initial_value_for_deflec = []
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 1321, 701))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 200, 1321, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_47 = QtWidgets.QLabel(self.frame)
        self.label_47.setGeometry(QtCore.QRect(1160, 10, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_47.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(1160, 40, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_6.setStyleSheet("#pushButton_6 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_6:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"#pushButton_6:pressed {\n"
"background-color: rgb(198, 198, 198);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 270, 1281, 421))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setGeometry(QtCore.QRect(810, 60, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_7.setStyleSheet("#pushButton_7 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 0, 0), stop:1  rgb(158, 3, 3));\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_7:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(158, 3, 3), stop:1  rgb(255, 0, 0));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"#pushButton_7:pressed {\n"
"background-color: rgb(255, 0, 0);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_11.setGeometry(QtCore.QRect(810, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_11.setStyleSheet("#pushButton_11 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(85, 255, 0), stop:1  rgb(7, 240, 151));\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_11:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(7, 240, 151), stop:1  rgb(85, 255, 0));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"#pushButton_11:pressed {\n"
"background-color: rgb(85, 255, 0);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_12.setGeometry(QtCore.QRect(810, 110, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_12.setStyleSheet("#pushButton_12 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(37, 197, 255), stop:1  rgb(44, 69, 211));\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_12:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(44, 69, 211), stop:1  rgb(37, 197, 255));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"#pushButton_12:pressed {\n"
"background-color: rgb(37, 197, 255);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_13.setGeometry(QtCore.QRect(810, 310, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_13.setStyleSheet("#pushButton_13 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(37, 197, 255), stop:1  rgb(44, 69, 211));\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_13:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(44, 69, 211), stop:1  rgb(37, 197, 255));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"#pushButton_13:pressed {\n"
"background-color: rgb(37, 197, 255);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_13.setFlat(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_14.setGeometry(QtCore.QRect(810, 260, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_14.setStyleSheet("#pushButton_14 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(85, 255, 255), stop:1  rgb(44, 69, 211));\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_14:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(44, 69, 211), stop:1  rgb(85, 255, 255));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"#pushButton_14:pressed {\n"
"background-color: rgb(85, 255, 255);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_14.setFlat(False)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_15.setGeometry(QtCore.QRect(810, 210, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_15.setStyleSheet("#pushButton_15 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(37, 197, 255), stop:1  rgb(44, 69, 211));\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_15:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(44, 69, 211), stop:1  rgb(37, 197, 255));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"#pushButton_15:pressed {\n"
"background-color: rgb(37, 197, 255);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_15.setFlat(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setGeometry(QtCore.QRect(930, 20, 341, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        self.tableWidget.setColumnWidth(1, 150)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()         
        self.tableWidget.setItem(4, 0, item)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)                                 #font: 75 18pt \"Arial\"
        self.tableWidget.setStyleSheet("QTableWidget {gridline-color: rgb(0, 0, 0);}\n"
"QTableWidget::item:selected{\n"
"color: rgb(255, 255, 255);}\n"
"QHeaderView{font: 75 12pt \"Arial\";}\n"
"QHeaderView::section{font: 75 10pt \"Arial\";background-color: rgb(85, 255, 255);}\n"
"QTableWidget::item:hover{background-color: rgb(255, 255, 0); color: rgb(0, 0, 0);}")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_16.setGeometry(QtCore.QRect(810, 160, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_16.setStyleSheet("#pushButton_16 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(37, 197, 255), stop:1  rgb(44, 69, 211));\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_16:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(44, 69, 211), stop:1  rgb(37, 197, 255));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"#pushButton_16:pressed {\n"
"background-color: rgb(37, 197, 255);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_16.setFlat(False)
        self.pushButton_16.setObjectName("pushButton_16")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_3)
        self.lcdNumber.setGeometry(QtCore.QRect(940, 280, 231, 51))
        self.lcdNumber.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_41 = QtWidgets.QLabel(self.frame_3)
        self.label_41.setGeometry(QtCore.QRect(1180, 290, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("")
        self.label_41.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame_3)
        self.lcdNumber_2.setGeometry(QtCore.QRect(940, 350, 231, 51))
        self.lcdNumber_2.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_42 = QtWidgets.QLabel(self.frame_3)
        self.label_42.setGeometry(QtCore.QRect(1190, 350, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("")
        self.label_42.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName("label_42")
        self.layoutWidget = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 791, 401))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_49.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_49.setObjectName("label_49")
        self.gridLayout.addWidget(self.label_49, 0, 0, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_18.setGeometry(QtCore.QRect(810, 360, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_18.setStyleSheet("#pushButton_18 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(37, 197, 255), stop:1  rgb(44, 69, 211));\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_18:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(44, 69, 211), stop:1  rgb(37, 197, 255));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"#pushButton_18:pressed {\n"
"background-color: rgb(37, 197, 255);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_18.setFlat(False)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(1160, 160, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_8.setStyleSheet("#pushButton_8 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(85, 255, 0), stop:1  rgb(7, 240, 151));\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_8:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(7, 240, 151), stop:1  rgb(85, 255, 0));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"#pushButton_8:pressed {\n"
"background-color: rgb(85, 255, 0);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 160, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_9.setStyleSheet("#pushButton_9 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(12, 146, 158), stop:1  rgb(97, 242, 255));\n"
"    \n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_9:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(97, 242, 255), stop:1  rgb(12, 146, 158));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_9:pressed {\n"
"background-color: rgb(97, 242, 255);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(80, 10, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(910, 140, 51, 41))
        self.comboBox.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                    "color: rgb(0, 0, 0);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.comboBox.setMaxVisibleItems(8)
        self.comboBox.setObjectName("comboBox")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(160, 50, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(160, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("")
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(140, 0, 20, 211))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(490, 0, 20, 211))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(980, 0, 20, 211))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(670, 70, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("")
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(510, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("")
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setGeometry(QtCore.QRect(600, 70, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(740, 0, 20, 211))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(750, 100, 241, 21))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(510, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("")
        self.label_27.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_12.setGeometry(QtCore.QRect(600, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_12.setFont(font)
        reg_ex = QRegExp("[A-Za-z]{0,20}")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_12)
        self.lineEdit_12.setValidator(input_validator)
        self.lineEdit_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(10, 60, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("")
        self.label_29.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(90, 60, 51, 31))
        self.comboBox_2.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                      "color: rgb(0, 0, 0);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.comboBox_2.setObjectName("comboBox_2")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(10, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("")
        self.label_30.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(90, 110, 51, 41))
        self.comboBox_3.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                      "color: rgb(0, 0, 0);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.comboBox_3.setObjectName("comboBox_3")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(1140, 0, 20, 211))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(990, 40, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("")
        self.label_31.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_13.setGeometry(QtCore.QRect(1050, 40, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_13.setFont(font)
        reg_ex = QRegExp("\\d+\\.\\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_13)
        self.lineEdit_13.setValidator(input_validator)
        self.lineEdit_13.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(990, 90, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("")
        self.label_32.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_14.setGeometry(QtCore.QRect(1050, 90, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_14.setFont(font)
        reg_ex = QRegExp("\\d+\\.\\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_14)
        self.lineEdit_14.setValidator(input_validator)
        self.lineEdit_14.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(1000, 150, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_10.setStyleSheet("#pushButton_10 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 38, 154), stop:1  rgb(226, 102, 135));\n"
"    \n"
"\n"
"\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_10:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(226, 102, 135), stop:1  rgb(255, 38, 154));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_10:pressed {\n"
"background-color: rgb(255, 38, 154);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_35 = QtWidgets.QLabel(self.frame)
        self.label_35.setGeometry(QtCore.QRect(160, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("")
        self.label_35.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_15.setGeometry(QtCore.QRect(280, 90, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_15.setFont(font)
        reg_ex = QRegExp("[A-Za-z]{0,20}")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_15)
        self.lineEdit_15.setValidator(input_validator)
        self.lineEdit_15.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_36 = QtWidgets.QLabel(self.frame)
        self.label_36.setGeometry(QtCore.QRect(160, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("")
        self.label_36.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_16.setGeometry(QtCore.QRect(280, 130, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_45 = QtWidgets.QLabel(self.frame)
        self.label_45.setGeometry(QtCore.QRect(1010, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("")
        self.label_45.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_45.setObjectName("label_45")
        self.line_8 = QtWidgets.QFrame(self.frame)
        self.line_8.setGeometry(QtCore.QRect(0, 250, 1321, 21))
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setObjectName("line_8")
        self.label_46 = QtWidgets.QLabel(self.frame)
        self.label_46.setGeometry(QtCore.QRect(500, 170, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("")
        self.label_46.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_17.setGeometry(QtCore.QRect(620, 170, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_17.setFont(font)
        reg_ex = QRegExp("\\d+\\.\\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_17)
        self.lineEdit_17.setValidator(input_validator)
        self.lineEdit_17.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_50 = QtWidgets.QLabel(self.frame)
        self.label_50.setGeometry(QtCore.QRect(500, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("")
        self.label_50.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_50.setObjectName("label_50")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_18.setGeometry(QtCore.QRect(620, 130, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_18.setFont(font)
        reg_ex = QRegExp("\\d+\\.\\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_18)
        self.lineEdit_18.setValidator(input_validator)
        self.lineEdit_18.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_34 = QtWidgets.QLabel(self.frame)
        self.label_34.setGeometry(QtCore.QRect(700, 130, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("")
        self.label_34.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.label_51 = QtWidgets.QLabel(self.frame)
        self.label_51.setGeometry(QtCore.QRect(700, 170, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("")
        self.label_51.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_51.setObjectName("label_51")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_19.setGeometry(QtCore.QRect(300, 170, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_19.setFont(font)
        reg_ex = QRegExp("\\d+\\.\\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_19)
        self.lineEdit_19.setValidator(input_validator)
        self.lineEdit_19.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame)
        self.pushButton_17.setGeometry(QtCore.QRect(1160, 100, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_17.setStyleSheet("#pushButton_17 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(253, 169, 0), stop:1  rgb(206, 221, 71));\n"
"    \n"
"    \n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_17:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(206, 221, 71), stop:1  rgb(253, 169, 0));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_17:pressed {\n"
"background-color: rgb(253, 169, 0);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_17.setFlat(False)
        self.pushButton_17.setObjectName("pushButton_17")
        self.line_9 = QtWidgets.QFrame(self.frame)
        self.line_9.setGeometry(QtCore.QRect(500, 100, 251, 20))
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setObjectName("line_9")
        self.label_63 = QtWidgets.QLabel(self.frame)
        self.label_63.setGeometry(QtCore.QRect(1110, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("")
        self.label_63.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_63.setObjectName("label_63")
        self.label_37 = QtWidgets.QLabel(self.frame)
        self.label_37.setGeometry(QtCore.QRect(1110, 40, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("")
        # self.label_37.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(180, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(850, 59, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(750, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(400, 170, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("")
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(750, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("")
        self.label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_10.setGeometry(QtCore.QRect(840, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(910, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("")
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        # self.pushButton_19 = QtWidgets.QPushButton(self.frame)
        # self.pushButton_19.setGeometry(QtCore.QRect(760, 140, 131, 41))
        # font = QtGui.QFont()
        # font.setFamily("Arial")
        # font.setPointSize(10)
        # font.setBold(True)
        # font.setWeight(75)
#         self.pushButton_19.setFont(font)
#         self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
#         self.pushButton_19.setStyleSheet("#pushButton_19 {\n"
# "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 0), stop:1  rgb(217, 200, 64));\n"
# "    \n"
# "\n"
# "border-radius:20px;\n"
# "border-color: rgb(0, 0, 0);\n"
# "border-style:outset;\n"
# "border-width:3px;\n"
# "}\n"
# "#pushButton_19:hover {\n"
# "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(217, 200, 64), stop:1  rgb(255, 255, 0));\n"
# "padding-bottom: 5px;\n"
# "padding-right: 5px;\n"
# "}\n"
# "\n"
# "#pushButton_19:pressed {\n"
# "background-color: rgb(255, 255, 0);\n"
# "padding-top: 5px;\n"
# "padding-left: 5px;\n"
# "}")
#         self.pushButton_19.setFlat(False)
#         self.pushButton_19.setObjectName("pushButton_19")
        self.label_90 = QtWidgets.QLabel(self.frame)
        self.label_90.setGeometry(QtCore.QRect(10, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.label_90.setFont(font)
        self.label_90.setStyleSheet("")
        self.label_90.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_90.setObjectName("label_90")
        self.label_91 = QtWidgets.QLabel(self.frame)
        self.label_91.setGeometry(QtCore.QRect(110, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(50)
        self.label_91.setFont(font)
        self.label_91.setStyleSheet("")
        self.label_91.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_91.setObjectName("label_91")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_37.setGeometry(QtCore.QRect(70, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_37.setFont(font)
        reg_ex = QRegExp("\\d+\\.\\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_37)
        self.lineEdit_37.setValidator(input_validator)
        self.lineEdit_37.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.label_92 = QtWidgets.QLabel(self.frame)
        self.label_92.setGeometry(QtCore.QRect(150, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.label_92.setFont(font)
        self.label_92.setStyleSheet("")
        self.label_92.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_92.setObjectName("label_92")
        self.label_93 = QtWidgets.QLabel(self.frame)
        self.label_93.setGeometry(QtCore.QRect(250, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(50)
        self.label_93.setFont(font)
        self.label_93.setStyleSheet("")
        self.label_93.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_93.setObjectName("label_93")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_38.setGeometry(QtCore.QRect(210, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_38.setFont(font)
        reg_ex = QRegExp("\\d+\\.\\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_38)
        self.lineEdit_38.setValidator(input_validator)
        self.lineEdit_38.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.label_94 = QtWidgets.QLabel(self.frame)
        self.label_94.setGeometry(QtCore.QRect(290, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.label_94.setFont(font)
        self.label_94.setStyleSheet("")
        self.label_94.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_94.setObjectName("label_94")
        self.label_95 = QtWidgets.QLabel(self.frame)
        self.label_95.setGeometry(QtCore.QRect(390, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(50)
        self.label_95.setFont(font)
        self.label_95.setStyleSheet("")
        self.label_95.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_95.setObjectName("label_95")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_39.setGeometry(QtCore.QRect(350, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_39.setFont(font)
        reg_ex = QRegExp("\\d+\\.\\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_39)
        self.lineEdit_39.setValidator(input_validator)
        self.lineEdit_39.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.label_96 = QtWidgets.QLabel(self.frame)
        self.label_96.setGeometry(QtCore.QRect(430, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.label_96.setFont(font)
        self.label_96.setStyleSheet("")
        self.label_96.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_96.setObjectName("label_96")
        self.label_97 = QtWidgets.QLabel(self.frame)
        self.label_97.setGeometry(QtCore.QRect(530, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(50)
        self.label_97.setFont(font)
        self.label_97.setStyleSheet("")
        self.label_97.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_97.setObjectName("label_97")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_40.setGeometry(QtCore.QRect(490, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_40.setFont(font)
        reg_ex = QRegExp("\\d+\\.\\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_40)
        self.lineEdit_40.setValidator(input_validator)
        self.lineEdit_40.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.label_98 = QtWidgets.QLabel(self.frame)
        self.label_98.setGeometry(QtCore.QRect(570, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.label_98.setFont(font)
        self.label_98.setStyleSheet("")
        self.label_98.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_98.setObjectName("label_98")
        self.label_99 = QtWidgets.QLabel(self.frame)
        self.label_99.setGeometry(QtCore.QRect(670, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(50)
        self.label_99.setFont(font)
        self.label_99.setStyleSheet("")
        self.label_99.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_99.setObjectName("label_99")
        self.lineEdit_41 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_41.setGeometry(QtCore.QRect(630, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_41.setFont(font)
        reg_ex = QRegExp("\\d+\\.\\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_41)
        self.lineEdit_41.setValidator(input_validator)
        self.lineEdit_41.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(280, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(760, 140, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label_50")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setGeometry(QtCore.QRect(280, 50, 191, 31))
        self.comboBox_4.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                      "color: rgb(0, 0, 0);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.comboBox_4.setObjectName("comboBox_4")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_4.setFont(font)
        
        self.lineEdit_42 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_42.setGeometry(QtCore.QRect(770, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_42.setFont(font)
        reg_ex = QRegExp("\\d+\\.\\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_42)
        self.lineEdit_42.setValidator(input_validator)
        self.lineEdit_42.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.label_100 = QtWidgets.QLabel(self.frame)
        self.label_100.setGeometry(QtCore.QRect(710, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.label_100.setFont(font)
        self.label_100.setStyleSheet("")
        self.label_100.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_100.setObjectName("label_100")
        self.label_101 = QtWidgets.QLabel(self.frame)
        self.label_101.setGeometry(QtCore.QRect(810, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(50)
        self.label_101.setFont(font)
        self.label_101.setStyleSheet("")
        self.label_101.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_101.setObjectName("label_101")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_43.setGeometry(QtCore.QRect(910, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_43.setFont(font)
        reg_ex = QRegExp("\\d+\\.\\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_43)
        self.lineEdit_43.setValidator(input_validator)
        self.lineEdit_43.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.label_102 = QtWidgets.QLabel(self.frame)
        self.label_102.setGeometry(QtCore.QRect(850, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.label_102.setFont(font)
        self.label_102.setStyleSheet("")
        self.label_102.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_102.setObjectName("label_102")
        self.label_103 = QtWidgets.QLabel(self.frame)
        self.label_103.setGeometry(QtCore.QRect(950, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(50)
        self.label_103.setFont(font)
        self.label_103.setStyleSheet("")
        self.label_103.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_103.setObjectName("label_103")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_44.setGeometry(QtCore.QRect(1050, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_44.setFont(font)
        reg_ex = QRegExp("\\d+\\.\\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_44)
        self.lineEdit_44.setValidator(input_validator)
        self.lineEdit_44.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.label_104 = QtWidgets.QLabel(self.frame)
        self.label_104.setGeometry(QtCore.QRect(990, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.label_104.setFont(font)
        self.label_104.setStyleSheet("")
        self.label_104.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_104.setObjectName("label_104")
        self.label_105 = QtWidgets.QLabel(self.frame)
        self.label_105.setGeometry(QtCore.QRect(1090, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(50)
        self.label_105.setFont(font)
        self.label_105.setStyleSheet("")
        self.label_105.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_105.setObjectName("label_105")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(1130, 220, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.non_empty_line_edits = []
        self.retranslateUi(MainWindow)
        self.cycle_num=0
        self.test_type=""
        self.test_id="1"
        self.remark=""
        self.timer3=QtCore.QTimer()
        self.timer31=QtCore.QTimer()
        self.cycle_num=0
        self.show_lcd_vals="N"
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_47.setText(_translate("MainWindow", "05 Aug 2020 14:23:00"))
        self.pushButton_6.setText(_translate("MainWindow", "Return"))
        self.pushButton_7.setText(_translate("MainWindow", "Stop"))
        self.pushButton_11.setText(_translate("MainWindow", "Start"))
        self.pushButton_12.setText(_translate("MainWindow", "All Graphs"))
        self.pushButton_13.setText(_translate("MainWindow", "View Report"))
        self.pushButton_14.setText(_translate("MainWindow", "Email"))
        self.pushButton_15.setText(_translate("MainWindow", "Comment"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Load  (Kg)"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Deflection  (mm)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Rec# "))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sample #"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "100"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "123.8"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "200"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "300"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "400"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "500"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_16.setText(_translate("MainWindow", "Print"))
        self.label_41.setText(_translate("MainWindow", "Kg."))
        self.label_42.setText(_translate("MainWindow", "mm."))
        self.label_49.setText(_translate("MainWindow", "Data Saved Successfully ......"))
        self.pushButton_18.setText(_translate("MainWindow", "Data"))
        self.pushButton_8.setText(_translate("MainWindow", "Go For Report"))
        self.pushButton_9.setText(_translate("MainWindow", "Reset"))
        self.label_11.setText(_translate("MainWindow", "Test ID:"))
        self.label_12.setText(_translate("MainWindow", "0001"))
        self.comboBox.setItemText(0, _translate("MainWindow", "02"))
        self.comboBox.setItemText(1, _translate("MainWindow", "03"))
        self.comboBox.setItemText(2, _translate("MainWindow", "04"))
        self.comboBox.setItemText(3, _translate("MainWindow", "05"))
        self.comboBox.setItemText(4, _translate("MainWindow", "06"))
        self.comboBox.setItemText(5, _translate("MainWindow", "07"))
        self.comboBox.setItemText(6, _translate("MainWindow", "08"))
        self.label_14.setText(_translate("MainWindow", "Specimen Name:"))
        self.label_15.setText(_translate("MainWindow", "LoadCell. Capacity :"))
        self.label_20.setText(_translate("MainWindow", "(Mm/min)"))
        self.label_21.setText(_translate("MainWindow", "Test Speed: "))
        self.label_27.setText(_translate("MainWindow", "Operator :"))
        self.label_29.setText(_translate("MainWindow", "Load Unit:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Kg"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Lb"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "N"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Gm"))
        self.label_30.setText(_translate("MainWindow", "Deflection \n"
" Unit:"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Mm"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Cm"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Inch"))
        self.label_31.setText(_translate("MainWindow", "X-axis: "))
        self.label_32.setText(_translate("MainWindow", "Y-axis: "))
        self.pushButton_10.setText(_translate("MainWindow", "Set Graph"))
        self.label_35.setText(_translate("MainWindow", "Job Name :"))
        self.label_36.setText(_translate("MainWindow", "Batch Number :"))
        self.label_45.setText(_translate("MainWindow", "Graph Scale "))
        self.label_46.setText(_translate("MainWindow", "Max. Load:"))
        self.label_50.setText(_translate("MainWindow", "Max. Deflection:"))
        self.label_34.setText(_translate("MainWindow", "(mm)"))
        self.label_51.setText(_translate("MainWindow", "(Kg)"))
        self.pushButton_17.setText(_translate("MainWindow", "Set Sample"))
        self.label_63.setText(_translate("MainWindow", "(Kg)"))
        self.label_37.setText(_translate("MainWindow", "(mm)"))
        self.label_16.setText(_translate("MainWindow", "Test Name :"))
        self.label_26.setText(_translate("MainWindow", "01"))
        self.label_28.setText(_translate("MainWindow", "Spec. Count:"))
        self.label_22.setText(_translate("MainWindow", "(Kg)"))
        self.label_23.setText(_translate("MainWindow", "Rev Speed: "))
        self.label_25.setText(_translate("MainWindow", "(Mm/min)"))
        self.label.setText(_translate("MainWindow", "Set Load Points"))
        # self.pushButton_19.setText(_translate("MainWindow", "Set Load Points"))
        self.label_90.setText(_translate("MainWindow", "Load (1):"))
        self.label_91.setText(_translate("MainWindow", "(Kg)"))
        self.label_92.setText(_translate("MainWindow", "Load (2):"))
        self.label_93.setText(_translate("MainWindow", "(Kg)"))
        self.label_94.setText(_translate("MainWindow", "Load (3):"))
        self.label_95.setText(_translate("MainWindow", "(Kg)"))
        self.label_96.setText(_translate("MainWindow", "Load (4):"))
        self.label_97.setText(_translate("MainWindow", "(Kg)"))
        self.label_98.setText(_translate("MainWindow", "Load (5):"))
        self.label_99.setText(_translate("MainWindow", "(Kg)"))
        self.label_13.setText(_translate("MainWindow", "Radial Test"))
        self.label_100.setText(_translate("MainWindow", "Load (6):"))
        self.label_101.setText(_translate("MainWindow", "(Kg)"))
        self.label_102.setText(_translate("MainWindow", "Load (7):"))
        self.label_103.setText(_translate("MainWindow", "(Kg)"))
        self.label_104.setText(_translate("MainWindow", "Load (8):"))
        self.label_105.setText(_translate("MainWindow", "(Kg)"))
        self.label_10.setText(_translate("MainWindow", "Graph set Done."))
        self.label_22.hide()
        self.frame_3.hide()
        self.label_10.hide()
        self.timer = QtCore.QTimer()
        self.timer.start(1)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.dateAndTime)
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.load_data()
        self.load_points_on_change()
        self.load_unit_on_change()
        self.deflection_unit_on_change()
        self.comboBox_2.currentTextChanged.connect(self.load_unit_on_change)
        self.comboBox_3.currentTextChanged.connect(self.deflection_unit_on_change)
        self.comboBox_4.currentTextChanged.connect(self.specimen_name_on_change)
        self.pushButton_10.clicked.connect(self.graph_scale_on_change)
        self.pushButton_8.clicked.connect(self.go_for_report)
        self.pushButton_9.clicked.connect(self.readWrite_fields)
        self.pushButton_13.clicked.connect(self.open_pdf)
        self.go_for_report()
        
    
    def dateAndTime(self):
        self.label_47.setText(datetime.datetime.now().strftime("%d %b %Y %H : %M : %S"))
   
    def readWrite_fields(self):
        self.pushButton_8.setEnabled(True)
        self.frame_3.hide()
        fields = [self.comboBox, self.comboBox_2, self.comboBox_3, self.comboBox_4, self.lineEdit_15, self.lineEdit_16, self.lineEdit_19, self.lineEdit_12, 
                  self.lineEdit_9, self.lineEdit_17, self.lineEdit_18, self.lineEdit_10, self.lineEdit_13, self.lineEdit_14, self.lineEdit_37, self.lineEdit_39, 
                  self.lineEdit_38, self.lineEdit_39, self.lineEdit_40, self.lineEdit_41, self.lineEdit_42, self.lineEdit_43
                ]
        self.indx=0
        for field in fields:
                if ( int(self.indx) <= 3 ):
                      field.setEnabled(True)
                else:
                
                      field.setReadOnly(True)
                self.indx = self.indx + 1
          
    def readOnly_fields(self):
        fields = [self.comboBox, self.comboBox_2, self.comboBox_3, self.comboBox_4, self.lineEdit_15, self.lineEdit_16, self.lineEdit_19, self.lineEdit_12, 
                  self.lineEdit_9, self.lineEdit_17, self.lineEdit_18, self.lineEdit_10, self.lineEdit_13, self.lineEdit_14, self.lineEdit_37, self.lineEdit_39, 
                  self.lineEdit_38, self.lineEdit_39, self.lineEdit_40, self.lineEdit_41, self.lineEdit_42, self.lineEdit_43
                ]
        self.indx=0
        for field in fields:
                if ( int(self.indx) <= 3 ):
                      field.setEnabled(False)
                else:
                      field.setReadOnly(True)
                self.indx = self.indx + 1


    def update_data(self):
                connection = sqlite3.connect("tyr.db") 
                          
                with connection:
                        cursor = connection.cursor()                  
                        cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(int(self.label_12.text()))+"'")
                        cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_MAX_LOAD='"+str(self.lineEdit_17.text())+"',NEW_TEST_MAX_LENGTH='"+str(self.lineEdit_18.text())+"'")
                        
                        cursor.execute("UPDATE TEST_MST SET SPECIMEN_NAME = '"+str(self.comboBox_4.currentText())+"', JOB_NAME = '"+str(self.lineEdit_15.text())+"', BATCH_ID = '"+str(self.lineEdit_16.text())+"', MOTOR_SPEED = '"+str(self.lineEdit_9.text())+"', MOTOR_REV_SPEED = '"+str(self.lineEdit_10.text())+"', OPERATOR = '"+str(self.lineEdit_12.text())+"', MOTOR_SPEED='"+str(self.lineEdit_9.text())+"', LAST_UNIT_LOAD = '"+str(self.comboBox_2.currentText())+"', LAST_UNIT_DISP = '"+str(self.comboBox_3.currentText())+"', NEW_TEST_MAX_LOAD = '"+str(self.lineEdit_17.text())+"', NEW_TEST_MAX_LENGTH = '"+str(self.lineEdit_18.text())+"'  WHERE  TEST_ID = '"+str(int(self.label_12.text()))+"'")                                        
                        cursor.execute("UPDATE TEST_DATA_RADIAL SET SPEC_ID = '"+str(self.label_26.text())+"', LOAD_POINTS = '"+str(self.comboBox.currentText())+"', MAX_LOAD = '"+self.lineEdit_17.text()+"', MAX_LENGTH = '"+self.lineEdit_18.text()+"', L1 = '"+self.lineEdit_37.text()+"', L2 = '"+self.lineEdit_38.text()+"', L3 = '"+self.lineEdit_39.text()+"', L4 = '"+self.lineEdit_40.text()+"', L5 = '"+self.lineEdit_41.text()+"', L6 = '"+self.lineEdit_42.text()+"', L7 = '"+self.lineEdit_43.text()+"', L8 = '"+self.lineEdit_44.text()+"', LOAD_UNIT = '"+str(self.comboBox_2.currentText())+"', LENGTH_UNIT = '"+str(self.comboBox_3.currentText())+"' WHERE TEST_ID = '"+str(self.label_12.text())+"'")
                connection.commit()
                connection.close() 
                if (self.comboBox_3.currentText() == "Mm"):
                        connection = sqlite3.connect("tyr.db")              
                        with connection:
                                cursor = connection.cursor() 
                                cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_X_LENGTH='"+self.lineEdit_13.text()+"' WHERE TEST_ID='"+str(int(self.label_12.text()))+"'")
                        connection.commit()
                        connection.close() 
                elif (self.comboBox_3.currentText() == "Inch"):
                        connection = sqlite3.connect("tyr.db")              
                        with connection:
                                cursor = connection.cursor() 
                                cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_X_LENGTH_INCH  = '"+self.lineEdit_13.text()+"' WHERE TEST_ID='"+str(int(self.label_12.text()))+"'")
                        connection.commit()
                        connection.close()
                elif (self.comboBox_3.currentText() == "Cm"):

                        connection = sqlite3.connect("tyr.db")              
                        with connection:
                                cursor = connection.cursor() 
                                cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_X_LENGTH_CM ='"+self.lineEdit_13.text()+"' WHERE TEST_ID='"+str(int(self.label_12.text()))+"'")
                        connection.commit()
                        connection.close()
                else:
                        pass        
                if (self.comboBox_2.currentText() == "Kg"):
                        connection = sqlite3.connect("tyr.db") 
                        with connection:
                                cursor = connection.cursor() 
                                cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_Y_LOAD='"+self.lineEdit_14.text()+"' WHERE TEST_ID='"+str(int(self.label_12.text()))+"'")
                        connection.commit()
                        connection.close() 
                elif (self.comboBox_2.currentText() == "Lb"):
                        connection = sqlite3.connect("tyr.db")              
                        with connection:
                                cursor = connection.cursor() 
                                cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_Y_LOAD_LB='"+self.lineEdit_14.text()+"' WHERE TEST_ID='"+str(int(self.label_12.text()))+"'")
                                      
                        connection.commit()
                        connection.close()
                elif (self.comboBox_2.currentText() == "N"):
                        connection = sqlite3.connect("tyr.db")              
                        with connection:
                                cursor = connection.cursor() 
                                cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_Y_LOAD_N='"+self.lineEdit_14.text()+"' WHERE TEST_ID='"+str(int(self.label_12.text()))+"'")
                        connection.commit()
                        connection.close()
                elif (self.comboBox_2.currentText() == "Gm"):
                        connection = sqlite3.connect("tyr.db")              
                        with connection:
                                cursor = connection.cursor() 
                                cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_X_LENGTH_CM ='"+self.lineEdit_14.text()+"' WHERE TEST_ID='"+str(int(self.label_12.text()))+"'")
                        connection.commit()
                        connection.close()   
                else:
                        pass
                connection = sqlite3.connect("tyr.db")              
                with connection:
                        cursor = connection.cursor()
                        results = cursor.execute("SELECT LOAD_UNIT FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"'  ")
                        for x in results:
                                self.load_unit = str(x[0])
                        print("seeeee rrrreesssu :", results)
                        print("seeeee rrrreesssu :", self.load_unit)         
                connection.commit()
                connection.close()        
                if  (self.initial_unit == "Kg" and self.load_unit == "Lb") :
                        connection = sqlite3.connect("tyr.db")              
                        with connection:
                                cursor = connection.cursor() 
                                cursor.execute("UPDATE TEST_DATA_RADIAL SET D1 = D1 * 0.0393701, D2 = D2 * 0.0393701, D3 = D3 * 0.0393701, D4 = D4 * 0.0393701, D5 = D5 * 0.0393701, D6 = D6 * 0.0393701, D7 = D7 * 0.0393701, D8 = D8 * 0.0393701 WHERE TEST_ID = '"+str(self.label_12.text())+"' ")        
                        connection.commit()
                        connection.close()
               
                elif  (self.initial_unit == "N" and self.load_unit == "Lb") :
                        connection = sqlite3.connect("tyr.db")              
                        with connection:
                                cursor = connection.cursor() 
                                cursor.execute("UPDATE TEST_DATA_RADIAL SET D1 = D1 * 0.0393701, D2 = D2 * 0.0393701, D3 = D3 * 0.0393701, D4 = D4 * 0.0393701, D5 = D5 * 0.0393701, D6 = D6 * 0.0393701, D7 = D7 * 0.0393701, D8 = D8 * 0.0393701 WHERE TEST_ID = '"+str(self.label_12.text())+"' ")        
                        connection.commit()
                        connection.close()
                elif  (self.initial_unit == "Gm" and self.load_unit == "Lb") :
                        connection = sqlite3.connect("tyr.db")              
                        with connection:
                                cursor = connection.cursor() 
                                cursor.execute("UPDATE TEST_DATA_RADIAL SET D1 = D1 * 0.0393701, D2 = D2 * 0.0393701, D3 = D3 * 0.0393701, D4 = D4 * 0.0393701, D5 = D5 * 0.0393701, D6 = D6 * 0.0393701, D7 = D7 * 0.0393701, D8 = D8 * 0.0393701 WHERE TEST_ID = '"+str(self.label_12.text())+"' ")        
                        connection.commit()
                        connection.close()
                elif  (self.initial_unit == "Lb" and self.load_unit == "Kg") :
                        connection = sqlite3.connect("tyr.db")              
                        with connection:
                                cursor = connection.cursor() 
                                cursor.execute("UPDATE TEST_DATA_RADIAL SET D1 = D1 * 25.4, D2 = D2 * 25.4, D3 = D3 * 25.4, D4 = D4 * 25.4, D5 = D5 * 25.4, D6 = D6 * 25.4, D7 = D7 * 25.4, D8 = D8 * 25.4 WHERE TEST_ID = '"+str(self.label_12.text())+"' ")       
                        connection.commit()
                        connection.close()
                elif  (self.initial_unit == "Lb" and self.load_unit == "N") :
                        connection = sqlite3.connect("tyr.db")              
                        with connection:
                                cursor = connection.cursor() 
                                cursor.execute("UPDATE TEST_DATA_RADIAL SET D1 = D1 * 25.4, D2 = D2 * 25.4, D3 = D3 * 25.4, D4 = D4 * 25.4, D5 = D5 * 25.4, D6 = D6 * 25.4, D7 = D7 * 25.4, D8 = D8 * 25.4 WHERE TEST_ID = '"+str(self.label_12.text())+"' ")       
                        connection.commit()
                        connection.close()
                elif  (self.initial_unit == "Lb" and self.load_unit == "Gm") :
                        connection = sqlite3.connect("tyr.db")              
                        with connection:
                                cursor = connection.cursor() 
                                cursor.execute("UPDATE TEST_DATA_RADIAL SET D1 = D1 * 25.4, D2 = D2 * 25.4, D3 = D3 * 25.4, D4 = D4 * 25.4, D5 = D5 * 25.4, D6 = D6 * 25.4, D7 = D7 * 25.4, D8 = D8 * 25.4 WHERE TEST_ID = '"+str(self.label_12.text())+"' ")       
                        connection.commit()
                        connection.close() 
                else:
                        pass        
                connection = sqlite3.connect("tyr.db")              
                with connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE TEST_DATA_RADIAL SET STIFFNESS = ((MAX_LOAD)/(MAX_LENGTH)) WHERE TEST_ID='"+str(int(self.label_12.text()))+"'")     
                connection.commit()
                connection.close()
    def go_for_report(self):
        self.validations()
        self.update_data() 
        self.show_grid_data()       
        if(self.go_ahead=="Yes"):
                        self.readOnly_fields()
                        self.frame_3.show()
                        self.label_49.setText("All Graphs")
                        self.sc_blank = PlotCanvas(self)  
                        self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
                        self.pushButton_11.hide()
                        self.pushButton_7.hide() 
                            
                        

    def validations(self):
        self.go_ahead="No"
        self.msg=""     
        if not self.msg:
                if(self.lineEdit_15.text() == ""):
                        self.msg="job Name Should not Empty."
                elif(self.lineEdit_16.text() == ""):
                        self.msg="Batch Number Should not Empty."
                elif(self.lineEdit_19.text() == ""):
                        self.msg="LoadCell Capacity Should not Empty."
                elif(self.lineEdit_9.text() == ""):
                        self.msg="Test Speed Should not Empty."
                elif(self.lineEdit_18.text() == ""):
                        self.msg="Max Deflection Should not Empty."
                elif(self.lineEdit_17.text() == ""):
                        self.msg="Max Load Should not Empty."
                elif(self.lineEdit_10.text() == ""):
                        self.msg="Rev. Speed Should not Empty."
                elif(self.lineEdit_12.text() == ""):
                        self.msg="Operator Should not Empty."
                elif(self.lineEdit_13.text() == ""):
                        self.msg="Graph Scale x-axsis Should not Empty."
                elif(self.lineEdit_14.text() == ""):
                        self.msg="Graph Scale y-axsis  Should not Empty."
                else:
                        load_value = str(self.comboBox.currentText())

                        load_points = {
                        "02": [self.lineEdit_37, self.lineEdit_38],     
                        "03": [self.lineEdit_37, self.lineEdit_39, self.lineEdit_38],
                        "04": [self.lineEdit_37, self.lineEdit_39, self.lineEdit_38, self.lineEdit_39],
                        "05": [self.lineEdit_37, self.lineEdit_39, self.lineEdit_38, self.lineEdit_39, self.lineEdit_40],
                        "06": [self.lineEdit_37, self.lineEdit_39, self.lineEdit_38, self.lineEdit_39, self.lineEdit_40, self.lineEdit_41],
                        "07": [self.lineEdit_37, self.lineEdit_39, self.lineEdit_38, self.lineEdit_39, self.lineEdit_40, self.lineEdit_41, self.lineEdit_42],
                        "08": [self.lineEdit_37, self.lineEdit_39, self.lineEdit_38, self.lineEdit_39, self.lineEdit_40, self.lineEdit_41, self.lineEdit_42, self.lineEdit_43]
                        }

                        empty_line_edits = []
                        self.non_empty_line_edits = []

                        if load_value in load_points:
                                for lineWidget in load_points[load_value]:
                                        if lineWidget.text() == "":
                                                empty_line_edits.append(lineWidget)
                                        else:
                                                print("load point is not empty.")
                                                self.non_empty_line_edits.append(lineWidget)
                        else:
                                print("not valid.")

                        # Display message for each empty line edit
                        # print("empty line edit :" , "," .join([widget.objectName() for widget in empty_line_edits]))
                        if empty_line_edits:
                                self.msg = "Load point(s) should not be empty.... "     
                        else:
                                print("load point is not empty........")
                                
                              
                                
        
        if not self.msg:
              self.go_ahead = "Yes"
        
        if(self.go_ahead=="Yes"): 
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("select count(*) from TEST_MST WHERE TEST_ID = '"+str(int(self.label_12.text()))+"'")  
                    
                for x in results:           
                        if(int(x[0]) > 0):
                                # print("check for count :", x[0])      
                                self.test_id_exist="Yes"
                        else:
                                self.test_id_exist="No"
                                # print("check for count :", x[0])                     
                connection.close() 
                                
                if(self.test_id_exist=="Yes"):                   
                        ### Update global var
                        connection = sqlite3.connect("tyr.db")              
                        with connection:
                                cursor = connection.cursor()                  
                                cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(int(self.label_12.text()))+"'")
                                cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_MAX_LOAD='"+str(self.lineEdit_17.text())+"',NEW_TEST_MAX_LENGTH='"+str(self.lineEdit_18.text())+"'")
                                cursor.execute("UPDATE TEST_MST SET SPECIMEN_NAME = '"+str(self.comboBox_4.currentText())+"', JOB_NAME = '"+str(self.lineEdit_15.text())+"', BATCH_ID = '"+str(self.lineEdit_16.text())+"', MOTOR_SPEED = '"+str(self.lineEdit_9.text())+"', MOTOR_REV_SPEED = '"+str(self.lineEdit_10.text())+"', OPERATOR = '"+str(self.lineEdit_12.text())+"', GRAPH_SCAL_Y_LOAD='"+self.lineEdit_14.text()+"', GRAPH_SCAL_X_LENGTH='"+self.lineEdit_13.text()+"', MOTOR_SPEED='"+str(self.lineEdit_9.text())+"', LAST_UNIT_LOAD = '"+str(self.comboBox_2.currentText())+"', LAST_UNIT_DISP = '"+str(self.comboBox_3.currentText())+"'  WHERE  TEST_ID = '"+str(int(self.label_12.text()))+"'")                                        
                        connection.commit()
                        connection.close()
                                        
                else:        
                        ### INSERT 
                        connection = sqlite3.connect("tyr.db")              
                        with connection:        
                                cursor = connection.cursor()                                                
                                cursor.execute("INSERT INTO TEST_MST(TEST_ID,TEST_TYPE,SPECIMEN_NAME,JOB_NAME,BATCH_ID,MOTOR_SPEED,MOTOR_REV_SPEED,OPERATOR,GRAPH_SCAL_Y_LOAD,GRAPH_SCAL_X_LENGTH,LOAD_POINTS,LAST_UNIT_LOAD,LAST_UNIT_DISP) VALUES('"+str(int(self.label_12.text()))+"','RADIAL-TEST', '"+str(self.comboBox_4.currentText())+"', '"+str(self.lineEdit_15.text())+"', '"+str(self.lineEdit_16.text())+"', '"+str(self.lineEdit_9.text())+"','"+str(self.lineEdit_10.text())+"', '"+str(self.lineEdit_12.text())+"', '"+self.lineEdit_14.text()+"', '"+self.lineEdit_13.text()+"','"+str(self.comboBox.currentText())+"'),'"+str(self.comboBox_2.currentText())+"','"+str(self.comboBox_3.currentText())+"'")
                                
                                cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(int(self.label_12.text()))+"', NEW_TEST_SPECIMEN_NAME = '"+str(self.comboBox_4.currentText())+"', MAX_LOAD = '"+self.lineEdit_17.text()+"'")
                                cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_MAX_LOAD='"+str(self.lineEdit_17.text())+"', NEW_TEST_MAX_LENGTH='"+str(self.lineEdit_18.text())+"'") 
                                         
                        connection.commit()
                        connection.close()                              
        else:
              print("go ahead is no....")     
                   
                                
                                
    # Updating the graph scale into the SETTING_MST                                   
    def graph_scale_on_change(self):
        connection = sqlite3.connect("tyr.db") 
        cursor = connection.cursor()
        cursor.execute("UPDATE SETTING_MST SET GRAPH_SCALE_CELL_1='"+str(self.lineEdit_13.text())+"', GRAPH_SCALE_CELL_2 ='"+str(self.lineEdit_14.text())+"'") 
        connection.commit()
        connection.close()
        self.label_10.setText("Graph Scale Updated...") 
        self.label_10.show()  

    # Selecting the respected data to requested specimen name      
    def specimen_name_on_change(self):

        connection = sqlite3.connect("tyr.db") 
        results = connection.execute("SELECT LOAD_CELL, REV_MOTOR_SPEED, MOTOR_SPEED, MAX_DEFLECTION ,MAX_LOAD FROM SPECIMEN_MST WHERE SPECIMEN_NAME = '"+self.comboBox_4.currentText()+"'") 
        for column in results:
             self.lineEdit_19.setText(str(column[0]))
             self.lineEdit_10.setText(str(column[1])) 
             self.lineEdit_9.setText(str(column[2]))
             self.lineEdit_18.setText(str(column[3]))  
             self.lineEdit_17.setText(str(column[4]))     
        connection.close()
             
    def deflection_unit_on_change(self):
        deflec_unit = str(self.comboBox_3.currentText())
        unit_widgets = [self.label_34, self.label_20, self.label_37, self.label_25]
        if (deflec_unit == "Cm"):
             cunt = 0
             for label in unit_widgets:
                cunt += 1
                if cunt %2 == 0:
                        pass
                #       label.setText("(" + str(deflec_unit) + "/min)" )
                else:
                     label.setText("(" + str(deflec_unit) + ")")
        elif (deflec_unit == "Mm"):
             cunt = 0
             for label in unit_widgets:
                cunt += 1
                if cunt %2 == 0:
                        pass
                #       label.setText("(" + str(deflec_unit) + "/min)" )
                else:
                     label.setText("(" + str(deflec_unit) + ")")                        
        else:
             cunt = 0
             for label in unit_widgets:
                cunt += 1
                if cunt %2 == 0:
                        pass
                #       label.setText("(" + str(deflec_unit) + "/min)" )
                else:
                     label.setText("(" + str(deflec_unit) + ")")

    def load_unit_on_change(self):
        connection = sqlite3.connect("tyr.db")              
        with connection:
                cursor = connection.cursor() 
                results = cursor.execute("SELECT IFNULL(D1,0),IFNULL(D2,0),IFNULL(D3,0),IFNULL(D4,0),IFNULL(D5,0),IFNULL(D6,0),IFNULL(D7,0),IFNULL(D8,0) FROM TEST_DATA_RADIAL WHERE TEST_ID = '"+str(self.label_12.text())+"'")
                for row in results:
                        
                        for value in row:
                                self.initial_value_for_deflec.append(float(value))
                                print("initial deflec :", self.initial_value_for_deflec) 
        connection.commit()
        connection.close() 
           
            

        unit = str(self.comboBox_2.currentText())
        load_widgets = [self.lineEdit_17, self.lineEdit_14, self.lineEdit_37, self.lineEdit_38, self.lineEdit_39, self.lineEdit_40, self.lineEdit_41, self.lineEdit_42, self.lineEdit_43, self.lineEdit_44]
        
        if (self.initial_unit == "Kg" or self.initial_unit == "N" or self.initial_unit == "Gm"):
                for x in self.def_and_y_ax_value:
                        self.mm_to_inch.append(float(x) * 0.0393701)


                               
        else :
                for x in self.def_and_y_ax_value:
                        if x.strip():
                                self.inch_to_mm.append(float(x) * 25.4)
                             
        
        if unit == "Kg":
                self.current_unit = "Kg"
                for x in self.initial_values:
                        if x.strip():
                                self.kg_to_N.append(float(x) * 9.81)
                                self.kg_to_lb.append(float(x) * 2.20462)
                                self.kg_to_gm.append(float(x) * 1000)
                self.set_labels(unit)
                self.comboBox_3.setCurrentIndex(0)
                
                
        elif unit == "Lb":
                self.current_unit = "Lb"
                for x in self.initial_values:
                        if x.strip():
                                self.lb_to_N.append(float(x) * 4.4482189159)
                                self.lb_to_kg.append(float(x) * 0.453592)
                                self.lb_to_gm.append(float(x) * 453.592)
                                
                self.set_labels(unit)
                self.comboBox_3.setCurrentIndex(2)
                
                                
        elif unit == "N":
                self.current_unit = "N"
                for x in self.initial_values:
                        if x.strip():
                                self.N_to_kg.append(float(x) * 0.10197)
                                self.N_to_lb.append(float(x) * 0.2248090795)
                                self.N_to_gm.append(float(x) * 101.97162)
                self.set_labels(unit)
                self.comboBox_3.setCurrentIndex(0)
        else:
                self.current_unit = "Gm"
                for x in self.initial_values:
                        if x.strip():
                                self.gm_to_kg.append(float(x) * 0.001)
                                self.gm_to_lb.append(float(x) * 0.00220462)
                                self.gm_to_N.append(float(x) * 0.009806652)
                self.set_labels(unit)
                self.comboBox_3.setCurrentIndex(0)
        
        
        
        if (self.initial_unit == "Kg" and self.current_unit == "Lb"):
                self.update_line_edits(self.kg_to_lb, load_widgets)
                self.update_line_edits(self.mm_to_inch, self.def_and_y_ax_widget)
        elif (self.initial_unit == "Kg" and self.current_unit == "N"):
                self.update_line_edits(self.kg_to_N, load_widgets)
                self.update_line_edits(self.def_and_y_ax_value, self.def_and_y_ax_widget)
        elif (self.initial_unit == "Kg" and self.current_unit == "Gm"):
                self.update_line_edits(self.kg_to_gm, load_widgets)
                self.update_line_edits(self.def_and_y_ax_value, self.def_and_y_ax_widget)
        elif (self.initial_unit == "Kg" and self.current_unit == "Kg"):
                self.update_line_edits(self.initial_values, load_widgets)
                self.update_line_edits(self.def_and_y_ax_value, self.def_and_y_ax_widget)
        elif (self.initial_unit == "Lb" and self.current_unit == "Kg"):
                self.update_line_edits(self.lb_to_kg, load_widgets)
                self.update_line_edits(self.inch_to_mm, self.def_and_y_ax_widget) 
        elif (self.initial_unit == "Lb" and self.current_unit == "Gm"):
                self.update_line_edits(self.lb_to_gm, load_widgets)
                self.update_line_edits(self.inch_to_mm, self.def_and_y_ax_widget)
        elif (self.initial_unit == "Lb" and self.current_unit == "N"):
                self.update_line_edits(self.lb_to_N, load_widgets) 
                self.update_line_edits(self.inch_to_mm, self.def_and_y_ax_widget)
        elif (self.initial_unit == "Lb" and self.current_unit == "Lb"):
                self.update_line_edits(self.initial_values, load_widgets)
                self.update_line_edits(self.def_and_y_ax_value, self.def_and_y_ax_widget)   
        elif (self.initial_unit == "N" and self.current_unit == "Lb"):
                self.update_line_edits(self.N_to_lb, load_widgets) 
                self.update_line_edits(self.mm_to_inch, self.def_and_y_ax_widget)
        elif (self.initial_unit == "N" and self.current_unit == "Gm"):
                self.update_line_edits(self.N_to_gm, load_widgets) 
                self.update_line_edits(self.def_and_y_ax_value, self.def_and_y_ax_widget)
        elif (self.initial_unit == "N" and self.current_unit == "Kg"):
                self.update_line_edits(self.N_to_kg, load_widgets)
                self.update_line_edits(self.def_and_y_ax_value, self.def_and_y_ax_widget) 
        elif (self.initial_unit == "N" and self.current_unit == "N"):
                self.update_line_edits(self.initial_values, load_widgets) 
        elif (self.initial_unit == "Gm" and self.current_unit == "Kg"):
                self.update_line_edits(self.gm_to_kg, load_widgets)
                self.update_line_edits(self.def_and_y_ax_value, self.def_and_y_ax_widget) 
        elif (self.initial_unit == "Gm" and self.current_unit == "Lb"):
                self.update_line_edits(self.gm_to_lb, load_widgets)  
                self.update_line_edits(self.mm_to_inch, self.def_and_y_ax_widget)
        elif (self.initial_unit == "Gm" and self.current_unit == "N"):

                self.update_line_edits(self.gm_to_N, load_widgets)
        elif (self.initial_unit == "Gm" and self.current_unit == "Gm"):
                self.update_line_edits(self.initial_values, load_widgets)
                self.update_line_edits(self.def_and_y_ax_value, self.def_and_y_ax_widget)
        else:
                print("unit not in comboBox")


    def set_labels(self, unit):
        load_unit_widgets = [self.label_22, self.label_51, self.label_63, self.label_91, self.label_93, self.label_95, self.label_97, self.label_99,
                                self.label_101, self.label_103, self.label_105] 
        for label in load_unit_widgets:
                label.setText("(" + str(unit) + ")")


    def update_line_edits(self, values, widgets):
        for value, widget in zip(values, widgets):
                if (value != ""):
                        float_value = float(value)
                        formatted_value = "{:.2f}".format(float_value)
                        widget.setText(str(formatted_value))
                else:
                        print("Empty string in arrey")        

    # Setting the load points according to requirement 
    def load_points_on_change(self):
        set_load_points = str(self.comboBox.currentText())
        load_points = {
        "03": [self.label_94, self.lineEdit_39, self.label_95],
        "04": [self.label_94, self.lineEdit_39, self.label_95, self.label_96, self.lineEdit_40, self.label_97],
        "05": [self.label_94, self.lineEdit_39, self.label_95, self.label_96, self.lineEdit_40, self.label_97,
               self.label_98, self.lineEdit_41, self.label_99],
        "06": [self.label_94, self.lineEdit_39, self.label_95, self.label_96, self.lineEdit_40, self.label_97,
               self.label_98, self.lineEdit_41, self.label_99, self.label_100, self.lineEdit_42, self.label_101],
        "07": [self.label_94, self.lineEdit_39, self.label_95, self.label_96, self.lineEdit_40, self.label_97,
               self.label_98, self.lineEdit_41, self.label_99, self.label_97, self.label_100, self.lineEdit_42,
               self.label_101, self.label_100, self.lineEdit_42, self.label_101, self.label_102, self.lineEdit_43,
               self.label_103],
        "08": [self.label_94, self.lineEdit_39, self.label_95, self.label_96, self.lineEdit_40, self.label_97,
               self.label_98, self.lineEdit_41, self.label_99, self.label_97, self.label_100, self.lineEdit_42,
               self.label_101, self.label_100, self.lineEdit_42, self.label_101, self.label_102, self.lineEdit_43,
               self.label_103, self.label_104, self.lineEdit_44, self.label_105]
        }
      
        for widgets_list in load_points.values():
                for widget in widgets_list:
                        widget.hide()
                               
        if set_load_points in load_points:
                for widget in load_points[set_load_points]:
                        widget.show()
        else:
             print("set value is not valid")
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT L1, L2, L3, L4, L5, L6, L7, L8 FROM TEST_DATA_RADIAL WHERE TEST_ID = '"+str(self.label_12.text())+"'  ")  
        for x in results:
               if (str(set_load_points) == "02"):
                      self.lineEdit_37.setText(str(x[0]))
                      self.lineEdit_38.setText(str(x[1]))
               elif (str(set_load_points) == "03"):
                      self.lineEdit_37.setText(str(x[0]))
                      self.lineEdit_38.setText(str(x[1]) )
                      self.lineEdit_39.setText(str(x[2])  )   
               elif (str(set_load_points) == "04"):
                      self.lineEdit_37.setText(str(x[0]))
                      self.lineEdit_38.setText(str(x[1]) )
                      self.lineEdit_39.setText(str(x[2]) )
                      self.lineEdit_40.setText(str(x[3]))
               elif (str(set_load_points) == "05"):
                      self.lineEdit_37.setText(str(x[0]))
                      self.lineEdit_38.setText(str(x[1]) )
                      self.lineEdit_39.setText(str(x[2]) )
                      self.lineEdit_40.setText(str(x[3]))
                      self.lineEdit_41.setText(str(x[4]))
               elif (str(set_load_points) == "06"):
                      self.lineEdit_37.setText(str(x[0]))
                      self.lineEdit_38.setText(str(x[1]))
                      self.lineEdit_39.setText(str(x[2]))
                      self.lineEdit_40.setText(str(x[3]))
                      self.lineEdit_41.setText(str(x[4]) )
                      self.lineEdit_42.setText(str(x[5]) )
               elif (str(set_load_points) == "07"):
                      self.lineEdit_37.setText(str(x[0]))
                      self.lineEdit_38.setText(str(x[1]) )
                      self.lineEdit_39.setText(str(x[2]) )
                      self.lineEdit_40.setText(str(x[3]))
                      self.lineEdit_41.setText(str(x[4]))
                      self.lineEdit_42.setText(str(x[5]))
                      self.lineEdit_43.setText(str(x[6]))
               elif (str(set_load_points) == "08"):
                      self.lineEdit_37.setText(str(x[0]))
                      self.lineEdit_38.setText(str(x[1]) )
                      self.lineEdit_39.setText(str(x[2]) )
                      self.lineEdit_40.setText(str(x[3]))
                      self.lineEdit_41.setText(str(x[4]))
                      self.lineEdit_42.setText(str(x[5]))
                      self.lineEdit_43.setText(str(x[6]))
                      self.lineEdit_44.setText(str(x[7]))
               else:
                      print("Not Valid Set Load Point.")
        load_widgets = [self.lineEdit_17, self.lineEdit_14, self.lineEdit_37, self.lineEdit_38, self.lineEdit_39, self.lineEdit_40, self.lineEdit_41, self.lineEdit_42, self.lineEdit_43, self.lineEdit_44]
        
        # Get initial values from line edits
        self.initial_values = [line_Edit.text() for line_Edit in load_widgets]
        print("initial value :", self.initial_values)
    def load_data(self):

        self.pushButton_8.setDisabled(True)
        self.pushButton_17.setDisabled(True)
        self.pushButton_10.setDisabled(True)
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TEST_ID FROM GLOBAL_VAR")       
        for x in results:  
                self.test_id=str(x[0])         
                self.label_12.setText(str(x[0]).zfill(4))
        connection.close() 
        print("test id  :", str(self.label_12.text()))
        
        self.comboBox_4.clear()
        self.comboBox.clear()
        
        
        # Selecting the specimen name from SPECIMEN_MST
        # connection = sqlite3.connect("tyr.db") 
        # results = connection.execute("SELECT DISTINCT SPECIMEN_NAME FROM SPECIMEN_MST WHERE SPECIMEN_NAME IS NOT NULL")
        # for x in results:
        #     specimen_name = x[0]
        #     self.comboBox_4.addItem(specimen_name)
        # connection.close()    

        
        connection = sqlite3.connect("tyr.db") 
        results = connection.execute("SELECT SPECIMEN_NAME, JOB_NAME, BATCH_ID, MOTOR_SPEED, MOTOR_REV_SPEED, OPERATOR, GRAPH_SCAL_Y_LOAD, GRAPH_SCAL_X_LENGTH, LOAD_POINTS, NEW_TEST_MAX_LENGTH, NEW_TEST_MAX_LOAD, LAST_UNIT_LOAD, LAST_UNIT_DISP FROM TEST_MST WHERE TEST_ID = '"+str(self.label_12.text())+"'") 
        for column in results:
             self.comboBox_4.addItem(str(column[0]))
             self.lineEdit_15.setText(str(column[1])) 
             self.lineEdit_16.setText(str(column[2]))
             self.lineEdit_9.setText(str(column[3]))  
             self.lineEdit_10.setText(str(column[4]))
             self.lineEdit_12.setText(str(column[5]))
             self.lineEdit_14.setText(str(column[6]))
             self.lineEdit_13.setText(str(column[7])) 
             self.comboBox.addItem(str(column[8]).zfill(2)) 
             self.lineEdit_18.setText(str(column[9]))
             self.lineEdit_17.setText(str(column[10]))
             self.comboBox_2.setCurrentText(str(column[11]))
             self.comboBox_3.setCurrentText(str(column[12]))
            
        connection.close() 
        self.initial_unit = self.comboBox_2.currentText()
        print("initial unit :", self.initial_unit)
        self.def_and_y_ax_widget = [self.lineEdit_18, self.lineEdit_13]
        self.def_and_y_ax_value = [line_Edit.text() for line_Edit in self.def_and_y_ax_widget]

        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LOAD_CELL FROM SPECIMEN_MST WHERE SPECIMEN_NAME = '"+str(self.comboBox_4.currentText())+"'")       
        for x in results:         
                self.lineEdit_19.setText(str(x[0]))
        connection.close() 

        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT COUNT(*) FROM TEST_DATA_RADIAL WHERE TEST_ID = '"+str(self.label_12.text())+"'")       
        for x in results:         
                self.label_26.setText(str(x[0]).zfill(2))
        connection.close() 
        
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)    
        
    
    def show_grid_data(self):
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)        
        if(int(str(self.comboBox.currentText())) == 2):       
                self.tableWidget.setColumnCount(4)
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setColumnWidth(1, 100)
                self.tableWidget.setColumnWidth(2, 100)
                self.tableWidget.setColumnWidth(3, 100) 
                self.tableWidget.setHorizontalHeaderLabels(['Spec.','Stiffness'+'\n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')',' Def \n @ '+str(self.lineEdit_37.text())+' ('+str(self.comboBox_2.currentText())+') ',' Def \n @ '+str(self.lineEdit_38.text())+' ('+str(self.comboBox_2.currentText())+')'])
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID),printf(\"%.2f\",STIFFNESS),printf(\"%.2f\",D1) ,printf(\"%.2f\",D2) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
        elif(int(str(self.comboBox.currentText())) == 3):       
                self.tableWidget.setColumnCount(5)
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setColumnWidth(1, 100)
                self.tableWidget.setColumnWidth(2, 100)
                self.tableWidget.setColumnWidth(3, 100)
                self.tableWidget.setColumnWidth(4, 100) 
                self.tableWidget.setHorizontalHeaderLabels(['Spec.','Stiffness'+'\n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')',' Def \n @ '+str(self.lineEdit_37.text())+' ('+str(self.comboBox_2.currentText())+') ','Def \n @ '+str(self.lineEdit_38.text())+' ('+str(self.comboBox_2.currentText())+') ','Def \n @ '+str(self.lineEdit_39.text())+' ('+str(self.comboBox_2.currentText())+')'])
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID),printf(\"%.2f\",STIFFNESS),printf(\"%.2f\",D1) ,printf(\"%.2f\",D2),printf(\"%.2f\",D3) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
        elif(int(str(self.comboBox.currentText())) == 4):       
                self.tableWidget.setColumnCount(6)
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setColumnWidth(1, 100)
                self.tableWidget.setColumnWidth(2, 100)
                self.tableWidget.setColumnWidth(3, 100)
                self.tableWidget.setColumnWidth(4, 100)
                self.tableWidget.setColumnWidth(5, 100) 
                self.tableWidget.setHorizontalHeaderLabels(['Spec.','Stiffness'+'\n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')',' Def \n @ '+str(self.lineEdit_37.text())+' ('+str(self.comboBox_2.currentText())+') ','Def \n @ '+str(self.lineEdit_38.text())+' ('+str(self.comboBox_2.currentText())+') ','Def \n @ '+str(self.lineEdit_39.text())+' ('+str(self.comboBox_2.currentText())+')','Def \n @ '+str(self.lineEdit_40.text())+' ('+str(self.comboBox_2.currentText())+')'])
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID),printf(\"%.2f\",STIFFNESS),printf(\"%.2f\",D1) ,printf(\"%.2f\",D2),printf(\"%.2f\",D3),printf(\"%.2f\",D4) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
        
        elif(int(str(self.comboBox.currentText())) == 5):       
                self.tableWidget.setColumnCount(7)
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setColumnWidth(1, 100)
                self.tableWidget.setColumnWidth(2, 100)
                self.tableWidget.setColumnWidth(3, 100)
                self.tableWidget.setColumnWidth(4, 100)
                self.tableWidget.setColumnWidth(5, 100)
                self.tableWidget.setColumnWidth(6, 100)
                self.tableWidget.setHorizontalHeaderLabels(['Spec.','Stiffness'+'\n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')',' Def \n @ '+str(self.lineEdit_37.text())+' ('+str(self.comboBox_2.currentText())+') ','Def \n @ '+str(self.lineEdit_38.text())+' ('+str(self.comboBox_2.currentText())+') ','Def \n @ '+str(self.lineEdit_39.text())+' ('+str(self.comboBox_2.currentText())+')','Def \n @ '+str(self.lineEdit_40.text())+' ('+str(self.comboBox_2.currentText())+')','Def \n @ '+str(self.lineEdit_41.text())+' ('+str(self.comboBox_2.currentText())+')'])
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID),printf(\"%.2f\",STIFFNESS),printf(\"%.2f\",D1) ,printf(\"%.2f\",D2),printf(\"%.2f\",D3),printf(\"%.2f\",D4),printf(\"%.2f\",D5) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
        
        elif(int(str(self.comboBox.currentText())) == 6):       
                self.tableWidget.setColumnCount(8)
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setColumnWidth(1, 100)
                self.tableWidget.setColumnWidth(2, 100)
                self.tableWidget.setColumnWidth(3, 100)
                self.tableWidget.setColumnWidth(4, 100)
                self.tableWidget.setColumnWidth(5, 100)
                self.tableWidget.setColumnWidth(6, 100)
                self.tableWidget.setColumnWidth(7, 100)
                self.tableWidget.setHorizontalHeaderLabels(['Spec.','Stiffness'+'\n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')',' Def \n @ '+str(self.lineEdit_37.text())+' ('+str(self.comboBox_2.currentText())+') ','Def \n @ '+str(self.lineEdit_38.text())+' ('+str(self.comboBox_2.currentText())+') ','Def \n @ '+str(self.lineEdit_39.text())+' ('+str(self.comboBox_2.currentText())+')','Def \n @ '+str(self.lineEdit_40.text())+' ('+str(self.comboBox_2.currentText())+')','Def \n @ '+str(self.lineEdit_41.text())+' ('+str(self.comboBox_2.currentText())+')','Def \n @ '+str(self.lineEdit_42.text())+' ('+str(self.comboBox_2.currentText())+')'])
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID),printf(\"%.2f\",STIFFNESS),printf(\"%.2f\",D1) ,printf(\"%.2f\",D2),printf(\"%.2f\",D3),printf(\"%.2f\",D4),printf(\"%.2f\",D5),printf(\"%.2f\",D6) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
   
        elif(int(str(self.comboBox.currentText())) == 7):       
                self.tableWidget.setColumnCount(9)
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setColumnWidth(1, 100)
                self.tableWidget.setColumnWidth(2, 100)
                self.tableWidget.setColumnWidth(3, 100)
                self.tableWidget.setColumnWidth(4, 100)
                self.tableWidget.setColumnWidth(5, 100)
                self.tableWidget.setColumnWidth(6, 100)
                self.tableWidget.setColumnWidth(7, 100)
                self.tableWidget.setColumnWidth(8, 100)
                self.tableWidget.setHorizontalHeaderLabels(['Spec.','Stiffness'+'\n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')',' Def \n @ '+str(self.lineEdit_37.text())+' ('+str(self.comboBox_2.currentText())+') ','Def \n @ '+str(self.lineEdit_38.text())+' ('+str(self.comboBox_2.currentText())+') ','Def \n @ '+str(self.lineEdit_39.text())+' ('+str(self.comboBox_2.currentText())+')','Def \n @ '+str(self.lineEdit_40.text())+' ('+str(self.comboBox_2.currentText())+')','Def \n @ '+str(self.lineEdit_41.text())+' ('+str(self.comboBox_2.currentText())+')','Def \n @ '+str(self.lineEdit_42.text())+' ('+str(self.comboBox_2.currentText())+')','Def \n @ '+str(self.lineEdit_43.text())+' ('+str(self.comboBox_2.currentText())+')'])
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID),printf(\"%.2f\",STIFFNESS),printf(\"%.2f\",D1) ,printf(\"%.2f\",D2),printf(\"%.2f\",D3),printf(\"%.2f\",D4),printf(\"%.2f\",D5),printf(\"%.2f\",D6),printf(\"%.2f\",D7) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
        elif(int(str(self.comboBox.currentText())) == 8):       
                self.tableWidget.setColumnCount(10)
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setColumnWidth(1, 100)
                self.tableWidget.setColumnWidth(2, 100)
                self.tableWidget.setColumnWidth(3, 100)
                self.tableWidget.setColumnWidth(4, 100)
                self.tableWidget.setColumnWidth(5, 100)
                self.tableWidget.setColumnWidth(6, 100)
                self.tableWidget.setColumnWidth(7, 100)
                self.tableWidget.setColumnWidth(8, 100)
                self.tableWidget.setColumnWidth(9, 100)
                self.tableWidget.setHorizontalHeaderLabels(['Spec.','Stiffness'+'\n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')',' Def \n @ '+str(self.lineEdit_37.text())+' ('+str(self.comboBox_2.currentText())+') ','Def \n @ '+str(self.lineEdit_38.text())+' ('+str(self.comboBox_2.currentText())+') ','Def \n @ '+str(self.lineEdit_39.text())+' ('+str(self.comboBox_2.currentText())+')','Def \n @ '+str(self.lineEdit_40.text())+' ('+str(self.comboBox_2.currentText())+')','Def \n @ '+str(self.lineEdit_41.text())+' ('+str(self.comboBox_2.currentText())+')','Def \n @ '+str(self.lineEdit_42.text())+' ('+str(self.comboBox_2.currentText())+')','Def \n @ '+str(self.lineEdit_43.text())+' ('+str(self.comboBox_2.currentText())+')','Def \n @ '+str(self.lineEdit_44.text())+' ('+str(self.comboBox_2.currentText())+')'    ])
                
                connection = sqlite3.connect("tyr.db")
                #print("SELECT printf(\"%.2f\",SPEC_ID),printf(\"%.4f\",STIFFNESS),printf(\"%.2f\",D1) ,printf(\"%.2f\",D2),printf(\"%.2f\",D3),printf(\"%.2f\",D4),printf(\"%.2f\",D5),printf(\"%.2f\",D6),printf(\"%.2f\",D7) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID),printf(\"%.2f\",STIFFNESS),printf(\"%.2f\",D1) ,printf(\"%.2f\",D2),printf(\"%.2f\",D3),printf(\"%.2f\",D4),printf(\"%.2f\",D5),printf(\"%.2f\",D6),printf(\"%.2f\",D7),printf(\"%.2f\",D8) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                
        else:
                self.tableWidget.setColumnCount(4)
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setColumnWidth(1, 100)
                self.tableWidget.setColumnWidth(2, 100)
                self.tableWidget.setColumnWidth(3, 100) 
                self.tableWidget.setHorizontalHeaderLabels(['Spec.','Stiffness'+'\n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')',' Def \n @ '+str(self.lineEdit_37.text())+' ('+str(self.comboBox_2.currentText())+') ',' Def \n @ '+str(self.lineEdit_38.text())+' ('+str(self.comboBox_2.currentText())+')'])
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID),printf(\"%.2f\",STIFFNESS),printf(\"%.2f\",D1) ,printf(\"%.2f\",D2) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
  
            
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
                #self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close() 


  

    def open_pdf(self):
        self.sc_data = PlotCanvas(self, width=8, height=5, dpi=90) 
        #self.pushButton_4_2.setEnabled(True)
        #self.pushButton_4_3.setEnabled(True)
        self.create_pdf_Tear()
        
        if platform.system() == "Linux":
                os.system("xpdf ./reports/test_report.pdf")
                product_id = self.get_usb_storage_id()
                if product_id != "ERROR":
                        os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                        os.system("cp ./reports/test_report.pdf /media/usb/Report_of_test_"+str(self.test_id)+".pdf")
                        os.system("sudo umount /media/usb")
                else:
                        print("Please connect USB storage device")
                
        elif platform.system() == "Windows":
                os.system("start ./reports/test_report.pdf")
                product_id = self.get_usb_storage_id()
                if product_id != "ERROR":
                        shutil.copy("./reports/test_report.pdf", "E:/")  # Destination directory
                        print("Report copied to USB drive.")
                else:
                        print("Please connect USB storage device")
        else:
               print("platform is macOS....")

    def get_usb_storage_id(self):
        if platform.system() == "Linux":
               os.system("rm -rf lsusb_data.txt")  
               product_id = "ERROR"
               os.system("lsusb >> lsusb_data.txt")
               try:
                        f = open('lsusb_data.txt','r')
                        for line in f:
                                cnt=0                
                                cnt=int(line.find("SanDisk"))
                                if cnt > 0 :                   
                                        product_id = line[28:33]
                                        product_id = "0x"+str(product_id)
                                f.close()
               except:
                        product_id = "ERROR"
        elif platform.system() == "Windows":
                try:
                        subprocess.run(["Del", "connected_usb_device.txt"], shell=True, check=True)
                except subprocess.CalledProcessError as error:
                        print("file not deleted :", error)       
                try:
                        subprocess.run("wmic path Win32_USBControllerDevice get Dependent", stdout=open("connected_usb_device.txt", "w"), shell=True, check=True)
                        with open("connected_usb_device.txt", "r", encoding="utf-16") as usb_name_file:
                                print(usb_name_file)  # Just for debugging
                                product_id = 'ERROR'
                                for LINE in usb_name_file:
                                        # print(LINE)  # Just for debugging
                                        # print(LINE.strip())  # Remove leading/trailing whitespace and newlines
                                        if "SANDISK" in LINE:  
                                                product_id = 'SANDISK'
                                                # print(product_id, ": Found in LINE")
                                                break
                                        # else:
                                        #         print("SANDISK not found in : line")
                except subprocess.CalledProcessError as error:
                        print("unable to run the command :", error)
        else:
               print("platform is macOS....")
        return product_id
             
    def create_pdf_Tear(self):
        self.remark=""
        self.login_user_name=""
        self.unit_typex="Kg/Cm"
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LAST_UNIT_LOAD,LAST_UNIT_DISP,TEST_ID,TESTED_BY from TEST_MST  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) ") 
        for x in results:
              self.last_load_unit=str(x[0])
              self.last_disp_unit=str(x[1])
              self.test_id=str(x[2])
              self.tested_by=str(x[3])
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT A.CREATED_ON,A.TEST_ID,B.LOAD_CELL,A.BATCH_ID,A.SPECIMEN_NAME,A.HARDNESS,B.TEST_TYPE,A.MACHINE_NO,A.PARTY_NAME,A.MOTOR_REV_SPEED,A.MATERIAL,datetime(current_timestamp,'localtime'),A.COMMENTS,A.OPERATOR,A.MOTOR_SPEED   FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
        for x in results:
            summary_data=[["Tested Date-Time: ",str(x[0]),"Test No: ",str(x[1])],["Spec. Name:  ",str(x[4]),"Batch ID: ",str(x[3])],["Test Type:",str(x[6]),"Load Cell Cap. : ",str(x[2])],["Customer Name :",str(x[8]),"Report Date-Time: ",str(x[11])],["Test Speed (min/min) :",str(x[14]),"Rev. Speed (min/min) :",str(x[9])],["Operator :",str(x[13]), " ", " "]]
            self.remark=str(x[12]) 
        connection.close()
        
        
        if(int(str(self.comboBox.currentText())) == 2) :
                  connection = sqlite3.connect("tyr.db")
                  data2= [['Spec.','Stiffness'+' \n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')', ' Def \n @ '+str(self.lineEdit_37.text())+' ('+str(self.comboBox_2.currentText())+') ',' Def \n @ '+str(self.lineEdit_38.text())+' ('+str(self.comboBox_2.currentText())+')']]
                  print(data2)
                  results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID), printf(\"%.2f\",STIFFNESS), printf(\"%.2f\",D1), printf(\"%.2f\",D2) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for x in results:
                                data2.append(x)
                                print(data2)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Avg', printf(\"%.2f\",avg(STIFFNESS)), printf(\"%.2f\",avg(D1)) , printf(\"%.2f\",avg(D2)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for y in results:
                                data2.append(y)
                                print(data2)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Max', printf(\"%.2f\",Max(STIFFNESS)), printf(\"%.2f\",max(D1)) ,printf(\"%.2f\",max(D2)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for z in results:
                                data2.append(z)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Min', printf(\"%.2f\",Min(STIFFNESS)), printf(\"%.2f\",min(D1)) ,printf(\"%.2f\",min(D2)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for n in results:
                                data2.append(n)
                  connection.close()
        elif(int(str(self.comboBox.currentText())) == 3) :
                  connection = sqlite3.connect("tyr.db")
                  data2= [['Spec.','Stiffness'+' \n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')', ' Def \n @ '+str(self.lineEdit_37.text())+' ('+str(self.comboBox_2.currentText())+') ',' Def \n @ '+str(self.lineEdit_38.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_39.text())+' ('+str(self.comboBox_2.currentText())+') ']]
                  print(data2)
                  results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID), printf(\"%.2f\",STIFFNESS), printf(\"%.2f\",D1), printf(\"%.2f\",D2), printf(\"%.2f\",D3) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for x in results:
                                data2.append(x)
                                print(data2)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Avg', printf(\"%.2f\",avg(STIFFNESS)), printf(\"%.2f\",avg(D1)) ,printf(\"%.2f\",avg(D2)), printf(\"%.2f\",avg(D3)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for y in results:
                                data2.append(y)
                                print(data2)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Max', printf(\"%.2f\",Max(STIFFNESS)), printf(\"%.2f\",max(D1)), printf(\"%.2f\",max(D2)), printf(\"%.2f\",max(D3)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for z in results:
                                data2.append(z)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Min',printf(\"%.2f\",Min(STIFFNESS)), printf(\"%.2f\",min(D1)), printf(\"%.2f\",min(D2)), printf(\"%.2f\",min(D3)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for n in results:
                                data2.append(n)
                  connection.close()
        elif(int(str(self.comboBox.currentText())) == 4) :
                  connection = sqlite3.connect("tyr.db")
                  data2= [['Spec.','Stiffness'+' \n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')', ' Def \n @ '+str(self.lineEdit_37.text())+' ('+str(self.comboBox_2.currentText())+') ',' Def \n @ '+str(self.lineEdit_38.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_39.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_40.text())+' ('+str(self.comboBox_2.currentText())+')']]
                  print(data2)
                  results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID), printf(\"%.2f\",STIFFNESS), printf(\"%.2f\",D1) ,printf(\"%.2f\",D2), printf(\"%.2f\",D3), printf(\"%.2f\",D4) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for x in results:
                                data2.append(x)
                                print(data2)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Avg', printf(\"%.2f\",avg(STIFFNESS)), printf(\"%.2f\",avg(D1)) ,printf(\"%.2f\",avg(D2)), printf(\"%.2f\",avg(D3)), printf(\"%.2f\",avg(D4)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for y in results:
                                data2.append(y)
                                print(data2)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Max', printf(\"%.2f\",Max(STIFFNESS)), printf(\"%.2f\",max(D1)) ,printf(\"%.2f\",max(D2)), printf(\"%.2f\",max(D3)), printf(\"%.2f\",max(D4)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for z in results:
                                data2.append(z)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Min', printf(\"%.2f\",Min(STIFFNESS)), printf(\"%.2f\",min(D1)) ,printf(\"%.2f\",min(D2)), printf(\"%.2f\",min(D3)), printf(\"%.2f\",min(D4)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for n in results:
                                data2.append(n)
                  connection.close()
        elif(int(str(self.comboBox.currentText())) == 5) :
                  connection = sqlite3.connect("tyr.db")
                  data2= [['Spec.','Stiffness'+' \n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')', ' Def \n @ '+str(self.lineEdit_37.text())+' ('+str(self.comboBox_2.currentText())+') ',' Def \n @ '+str(self.lineEdit_38.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_39.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_40.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_41.text())+' ('+str(self.comboBox_2.currentText())+')']]
                  print(data2)
                  results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID), printf(\"%.2f\",STIFFNESS), printf(\"%.2f\",D1) ,printf(\"%.2f\",D2), printf(\"%.2f\",D3), printf(\"%.2f\",D4), printf(\"%.2f\",D5) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for x in results:
                                data2.append(x)
                                print(data2)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Avg', printf(\"%.2f\",avg(STIFFNESS)), printf(\"%.2f\",avg(D1)) ,printf(\"%.2f\",avg(D2)), printf(\"%.2f\",avg(D3)), printf(\"%.2f\",avg(D4)), printf(\"%.2f\",avg(D5)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for y in results:
                                data2.append(y)
                                print(data2)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Max',printf(\"%.2f\",Max(STIFFNESS)), printf(\"%.2f\",max(D1)) ,printf(\"%.2f\",max(D2)), printf(\"%.2f\",max(D3)), printf(\"%.2f\",max(D4)), printf(\"%.2f\",max(D5)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for z in results:
                                data2.append(z)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Min', printf(\"%.2f\",Min(STIFFNESS)), printf(\"%.2f\",min(D1)) ,printf(\"%.2f\",min(D2)), printf(\"%.2f\",min(D3)), printf(\"%.2f\",min(D4)), printf(\"%.2f\",min(D5)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for n in results:
                                data2.append(n)
                  connection.close()
        elif(int(str(self.comboBox.currentText())) == 6) :
                  connection = sqlite3.connect("tyr.db")
                  data2= [['Spec.','Stiffness'+' \n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')', ' Def \n @ '+str(self.lineEdit_37.text())+' ('+str(self.comboBox_2.currentText())+') ',' Def \n @ '+str(self.lineEdit_38.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_39.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_40.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_41.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_42.text())+' ('+str(self.comboBox_2.currentText())+')']]
                  print(data2)
                  results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID), printf(\"%.2f\",STIFFNESS), printf(\"%.2f\",D1) ,printf(\"%.2f\",D2), printf(\"%.2f\",D3), printf(\"%.2f\",D4), printf(\"%.2f\",D5), printf(\"%.2f\",D6) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for x in results:
                                data2.append(x)
                                print(data2)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Avg', printf(\"%.2f\",avg(STIFFNESS)), printf(\"%.2f\",avg(D1)) ,printf(\"%.2f\",avg(D2)), printf(\"%.2f\",avg(D3)), printf(\"%.2f\",avg(D4)), printf(\"%.2f\",avg(D5)), printf(\"%.2f\",avg(D6)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for y in results:
                                data2.append(y)
                                print(data2)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Max', printf(\"%.2f\",Max(STIFFNESS)), printf(\"%.2f\",max(D1)) ,printf(\"%.2f\",max(D2)), printf(\"%.2f\",max(D3)), printf(\"%.2f\",max(D4)), printf(\"%.2f\",max(D5)), printf(\"%.2f\",max(D6)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for z in results:
                                data2.append(z)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Min', printf(\"%.2f\",Min(STIFFNESS)), printf(\"%.2f\",min(D1)) ,printf(\"%.2f\",min(D2)), printf(\"%.2f\",min(D3)), printf(\"%.2f\",min(D4)), printf(\"%.2f\",min(D5)), printf(\"%.2f\",min(D6)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for n in results:
                                data2.append(n)
                  connection.close()
        elif(int(str(self.comboBox.currentText())) == 7) :
                  connection = sqlite3.connect("tyr.db")
                  data2= [['Spec.','Stiffness'+' \n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')', ' Def \n @ '+str(self.lineEdit_37.text())+' ('+str(self.comboBox_2.currentText())+') ',' Def \n @ '+str(self.lineEdit_38.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_39.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_40.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_41.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_42.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_43.text())+' ('+str(self.comboBox_2.currentText())+')']]
                  print(data2)
                  results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID), printf(\"%.2f\",STIFFNESS), printf(\"%.2f\",D1) ,printf(\"%.2f\",D2), printf(\"%.2f\",D3), printf(\"%.2f\",D4), printf(\"%.2f\",D5), printf(\"%.2f\",D6), printf(\"%.2f\",D7) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for x in results:
                                data2.append(x)
                                print(data2)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Avg', printf(\"%.2f\",avg(STIFFNESS)), printf(\"%.2f\",avg(D1)) ,printf(\"%.2f\",avg(D2)), printf(\"%.2f\",avg(D3)), printf(\"%.2f\",avg(D4)), printf(\"%.2f\",avg(D5)), printf(\"%.2f\",avg(D6)), printf(\"%.2f\",avg(D7)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for y in results:
                                data2.append(y)
                                print(data2)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Max', printf(\"%.2f\",Max(STIFFNESS)), printf(\"%.2f\",max(D1)) ,printf(\"%.2f\",max(D2)), printf(\"%.2f\",max(D3)), printf(\"%.2f\",max(D4)), printf(\"%.2f\",max(D5)), printf(\"%.2f\",max(D6)), printf(\"%.2f\",max(D7)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for z in results:
                                data2.append(z)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Min',printf(\"%.2f\",Min(STIFFNESS)), printf(\"%.2f\",min(D1)) ,printf(\"%.2f\",min(D2)), printf(\"%.2f\",min(D3)), printf(\"%.2f\",min(D4)), printf(\"%.2f\",min(D5)), printf(\"%.2f\",min(D6)), printf(\"%.2f\",min(D7)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for n in results:
                                data2.append(n)
                  connection.close()
        elif(int(str(self.comboBox.currentText())) == 8) :
                  connection = sqlite3.connect("tyr.db")
                  data2= [['Spec.','Stiffness'+' \n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')', ' Def \n @ '+str(self.lineEdit_37.text())+' ('+str(self.comboBox_2.currentText())+') ',' Def \n @ '+str(self.lineEdit_38.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_39.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_40.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_41.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_42.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_43.text())+' ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_44.text())+' ('+str(self.comboBox_2.currentText())+')']]
                  print(data2)
                  results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID), printf(\"%.2f\",STIFFNESS), printf(\"%.2f\",D1) ,printf(\"%.2f\",D2), printf(\"%.2f\",D3), printf(\"%.2f\",D4), printf(\"%.2f\",D5), printf(\"%.2f\",D6), printf(\"%.2f\",D7), printf(\"%.2f\",D8) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for x in results:
                                data2.append(x)
                                print(data2)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Avg',printf(\"%.2f\",avg(STIFFNESS)), printf(\"%.2f\",avg(D1)) ,printf(\"%.2f\",avg(D2)), printf(\"%.2f\",avg(D3)), printf(\"%.2f\",avg(D4)), printf(\"%.2f\",avg(D5)), printf(\"%.2f\",avg(D6)), printf(\"%.2f\",avg(D7)), printf(\"%.2f\",avg(D8)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for y in results:
                                data2.append(y)
                                print(data2)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Max', printf(\"%.2f\",Max(STIFFNESS)), printf(\"%.2f\",max(D1)) ,printf(\"%.2f\",max(D2)), printf(\"%.2f\",max(D3)), printf(\"%.2f\",max(D4)), printf(\"%.2f\",max(D5)), printf(\"%.2f\",max(D6)), printf(\"%.2f\",max(D7)), printf(\"%.2f\",max(D8)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for z in results:
                                data2.append(z)
                  connection.close()
                  
                  connection = sqlite3.connect("tyr.db")
                  results=connection.execute("SELECT 'Min', printf(\"%.2f\",Min(STIFFNESS)), printf(\"%.2f\",min(D1)) ,printf(\"%.2f\",min(D2)), printf(\"%.2f\",min(D3)), printf(\"%.2f\",min(D4)), printf(\"%.2f\",min(D5)), printf(\"%.2f\",min(D6)), printf(\"%.2f\",min(D7)), printf(\"%.2f\",min(D8)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for n in results:
                                data2.append(n)
                  connection.close()
        
        
        
               
        
        y=300
        Elements=[]
        
        
        
        
        PAGE_HEIGHT=defaultPageSize[1]
        styles = getSampleStyleSheet()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select COMPANY_NAME,ADDRESS1 from SETTING_MST ") 
        for x in results:            
            Title = Paragraph(str(x[0]), styles["Title"])
            #Title2 = Paragraph(str(x[1]), styles["Title"])
            ptext = "<font name=Helvetica size=11>"+str(x[1])+" </font>"            
            Title2 = Paragraph(str(ptext), styles["Title"])
        connection.close()
        blank=Paragraph("                                                                                          ", styles["Normal"])
        #comments = Paragraph("Remark : ______________________________________________________________________________", styles["Normal"])
        if(str(self.remark) == ""):
                comments = Paragraph("    Remark : ______________________________________________________________________________", styles["Normal"])
        else:
                comments = Paragraph("    Remark : "+str(self.remark), styles["Normal"])
        footer_2= Paragraph("Authorised and Signed By : _________________.", styles["Normal"])
        
        linea_firma = Line(2, 90, 670, 90)
        d = Drawing(50, 1)
        d.add(linea_firma)
       
        
        #f1=Table(data)
        #f1.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
        #
        #TEST_DETAILS = Paragraph("----------------------------------------------------------------------------------------------------------------------------------------------------", styles["Normal"])
        #TS_STR = Paragraph("Tensile Strength and Modulus Details :", styles["Normal"])
        
        f2=Table(data2)
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 1.00, colors.black), ('BACKGROUND', (0, 0), (-1, 0), colors.grey), ('INNERGRID', (0, 0), (-1, -1), 0.50, colors.red),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 1.00, colors.black), ('INNERGRID', (0, 0), (-1, -1), 0.50, colors.red),('FONT', (0, 0), (-1, -1), "Helvetica", 10),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
        #self.show_all_specimens()
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img,
                        6 * inch, 4* inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),Spacer(1,12),f2,Spacer(1,12),blank,comments,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        try:
               
                doc = SimpleDocTemplate('./reports/test_report.pdf', pagesize=A4,rightMargin=20,
                                        leftMargin=30,
                                        topMargin=10,
                                        bottomMargin=10)
                doc.build(Elements)
        except PermissionError as error:
               print("Alredy Report :", error)        
        #print("Done")    
               

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #fig.savefig('ssdsd.png')
        self.axes = fig.add_subplot(111)        
        FigureCanvas.__init__(self, fig)
        #FigureCanvas.setStyleSheet("background-color:red;")
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)       
        
        self.plot()
        self.last_load_unit=""
        self.last_disp_unit=""
        self.graph_type=""
        self.cs_area_mm="1"       
        self.guage_length_mm="1"
        
        
    def plot(self):
        ax = self.figure.add_subplot(111)
       
        ax.set_facecolor('#CCFFFF')   
        ax.minorticks_on()
        
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        
        self.s=[]
        self.t=[]
        self.graph_ids=[]    
        self.x_num=[0.0]
        self.y_num=[0.0]
        self.test_type="Tear"
        self.color=['b','r','g','y','k','c','m','b']
        #ax.set_title('Test Id=32         Samples=3       BreakLoad(Kg)=110        Length(mm)=3')         
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT DISTINCT GRAPH_ID FROM TEST_DATA_RADIAL WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID") 
        for x in results:
              self.graph_ids.append(x[0])            
              print("Grph IDs :"+str(x[0]))
        connection.close()
        

        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LAST_UNIT_LOAD,LAST_UNIT_DISP,GRAPH_SCAL_X_LENGTH,GRAPH_SCAL_Y_LOAD from TEST_MST  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) ") 
        for x in results:
              self.last_load_unit="Kg"
              self.last_disp_unit="Mm"
              ax.set_xlim(0,float(x[2]))
              ax.set_ylim(0,float(x[3]))  
        connection.close()
        
        
        
        
        
        self.graph_type="Load Vs Deflection"
        for g in range(len(self.graph_ids)):
            self.x_num=[0.0]
            self.y_num=[0.0]
            connection = sqlite3.connect("tyr.db")
            if(self.graph_type=="Load Vs Deflection"):
                    if(self.last_load_unit=="Kg" and self.last_disp_unit=="Mm"):
                                    results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Kg" and self.last_disp_unit=="Cm"):
                                    results=connection.execute("SELECT X_NUM_CM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Kg" and self.last_disp_unit=="Inch"):
                                    results=connection.execute("SELECT X_NUM_INCH,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Lb" and self.last_disp_unit=="Inch"):
                                    results=connection.execute("SELECT X_NUM_INCH,Y_NUM_LB FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Lb" and self.last_disp_unit=="Cm"):
                                    results=connection.execute("SELECT X_NUM_CM,Y_NUM_LB FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Lb" and self.last_disp_unit=="Mm"):
                                    results=connection.execute("SELECT X_NUM,Y_NUM_LB FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="N" and self.last_disp_unit=="Mm"):
                                    results=connection.execute("SELECT X_NUM,Y_NUM_N FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="N" and self.last_disp_unit=="Cm"):
                                    results=connection.execute("SELECT X_NUM_CM,Y_NUM_N FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="N" and self.last_disp_unit=="Inch"):
                                    results=connection.execute("SELECT X_NUM_INCH,Y_NUM_N FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="KN" and self.last_disp_unit=="Mm"):
                                    results=connection.execute("SELECT X_NUM,Y_NUM_KN FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="KN" and self.last_disp_unit=="Cm"):
                                    results=connection.execute("SELECT X_NUM_CM,Y_NUM_KN FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="KN" and self.last_disp_unit=="Inch"):
                                    results=connection.execute("SELECT X_NUM_INCH,Y_NUM_KN FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="gm" and self.last_disp_unit=="Mm"):
                                    results=connection.execute("SELECT X_NUM,Y_NUM_MPA FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    else:    
                                    results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
            
            elif(self.graph_type=="Load Vs Time"):                    
                    results=connection.execute("SELECT T_SEC,Y_NUM FROM GRAPH_MST WHERE T_SEC > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
         
            else:
                    results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
            for k in results:        
                self.x_num.append(k[0])
                self.y_num.append(k[1])
            connection.close()
           
            if(g < 8 ):
                ax.plot(self.x_num,self.y_num, self.color[g],label="Specimen_"+str(g+1))
        
        print("self.graph_type :"+str(self.graph_type))
        if(self.graph_type=="Load Vs Travel"):
                ax.set_xlabel('Deflection ('+str(self.last_disp_unit)+')')
                ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
        
        elif(self.graph_type=="Load Vs Time"):
                ax.set_xlabel('Time (sec)')
                ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
        else:
                ax.set_xlabel('Deflection ('+str(self.last_disp_unit)+')')
                ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
        #self.connect('motion_notify_event', mouse_move)
        ax.legend()        
        self.draw()
        self.figure.savefig('last_graph.png',dpi=100)
        
        #ax.connect('motion_notify_event', mouse_move)
    
            





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_74_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
