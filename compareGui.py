#coding=utf-8
# Form implementation generated from reading ui file 'compareGui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import os
import sys

import time
from PyQt4 import QtCore, QtGui
from progam import Ui_Form

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
sys.setdefaultencoding('utf-8')

class Ui_MainWindow(QtGui.QMainWindow):
    JsonPath,ExcePath,DataPath = '','',''
    threadNum = 0
    thread = []

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowIcon(QtGui.QIcon('logo.png'))
        MainWindow.resize(300, 250)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.JsonButton = QtGui.QPushButton(self.centralwidget)
        self.JsonButton.setGeometry(QtCore.QRect(100, 40, 101, 23))
        self.JsonButton.setObjectName(_fromUtf8("JsonButton"))
        self.JsonButton.clicked[bool].connect(self.Jsonfile)
        self.JsonDirLable = QtGui.QLabel("insert Jsonfile",self)
        self.JsonDirLable.move(100,20)

        self.ExcelButton = QtGui.QPushButton(self.centralwidget)
        self.ExcelButton.setGeometry(QtCore.QRect(100, 80, 101, 23))
        self.ExcelButton.setObjectName(_fromUtf8("ExcelButton"))
        self.ExcelButton.clicked[bool].connect(self.Excelfile)
        self.ExcelDirLable = QtGui.QLabel("insert Excelfile", self)
        self.ExcelDirLable.move(100,60)

        self.DataBaseButton = QtGui.QPushButton(self.centralwidget)
        self.DataBaseButton.setGeometry(QtCore.QRect(100, 120, 101, 23))
        self.DataBaseButton.setObjectName(_fromUtf8("DataBaseButton"))
        self.DataBaseButton.clicked[bool].connect(self.DataBasefile)
        self.DataBaseDirLable = QtGui.QLabel("insert DBfile", self)
        self.DataBaseDirLable.move(100, 100)

        self.program = QtGui.QPushButton(self.centralwidget)
        self.program.setGeometry(QtCore.QRect(25, 180, 101, 23))
        self.program.setObjectName(_fromUtf8("program"))
        self.program.clicked[bool].connect(self.confirmprogram)
        # self.programStatusLable = QtGui.QLabel("none", self)
        # self.programStatusLable.move(25, 160)

        self.openResult = QtGui.QPushButton(self.centralwidget)
        self.openResult.setGeometry(QtCore.QRect(170, 180, 101, 23))
        self.openResult.setObjectName(_fromUtf8("openResult"))
        self.openResult.clicked[bool].connect(self.open_Result)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        # self.progress = QtGui.QProgressBar(self)
        # self.progress.setGeometry(26,210,130,20)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_Result(self):
        os.system("start explorer "+os.path.abspath('Result'))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CompareWin", None))
        self.JsonButton.setText(_translate("MainWindow", "JsonFile", None))
        self.ExcelButton.setText(_translate("MainWindow", "ExcenlFile", None))
        self.DataBaseButton.setText(_translate("MainWindow", "DataBaseFile", None))
        self.program.setText(_translate("MainWindow", "start", None))
        self.openResult.setText(_translate("MainWindow", "Result", None))

    def Jsonfile(self):
        self.JsonPath = str(QtGui.QFileDialog.getOpenFileName(self,'open file',"*.txt"))
        self.JsonDirLable.setText(self.JsonPath)
        print self.JsonPath

    def Excelfile(self):
        self.ExcePath = str(QtGui.QFileDialog.getOpenFileName(self,'open file',"*.xlsx"))
        self.ExcelDirLable.setText(self.ExcePath)
        print self.ExcePath

    def DataBasefile(self):
        self.DataPath= str(QtGui.QFileDialog.getOpenFileName(self,'open file',"*.sdf"))
        self.DataBaseDirLable.setText(self.DataPath)
        print self.DataPath

    def confirmprogram(self):
        self.thread.append(Ui_Form(self.JsonPath, self.ExcePath, self.DataPath))
        self.Ui_Form = self.thread[self.threadNum]
        self.threadNum += 1