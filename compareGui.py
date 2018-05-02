# Form implementation generated from reading ui file 'compareGui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui

from progam import programFunction

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

class Ui_MainWindow(QtGui.QMainWindow):
    JsonPath = ''
    ExcePath = ''
    DataPath = ''

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(300, 250)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.JsonButton = QtGui.QPushButton(self.centralwidget)
        self.JsonButton.setGeometry(QtCore.QRect(100, 30, 101, 23))
        self.JsonButton.setObjectName(_fromUtf8("JsonButton"))
        self.JsonButton.clicked[bool].connect(self.Jsonfile)


        self.ExcelButton = QtGui.QPushButton(self.centralwidget)
        self.ExcelButton.setGeometry(QtCore.QRect(100, 60, 101, 23))
        self.ExcelButton.setObjectName(_fromUtf8("ExcelButton"))
        self.ExcelButton.clicked[bool].connect(self.Excelfile)

        self.DataBaseButton = QtGui.QPushButton(self.centralwidget)
        self.DataBaseButton.setGeometry(QtCore.QRect(100, 90, 101, 23))
        self.DataBaseButton.setObjectName(_fromUtf8("DataBaseButton"))
        self.DataBaseButton.clicked[bool].connect(self.DataBasefile)

        self.program = QtGui.QPushButton(self.centralwidget)
        self.program.setGeometry(QtCore.QRect(100, 190, 101, 23))
        self.program.setObjectName(_fromUtf8("program"))
        self.program.clicked[bool].connect(self.confirmprogram)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CompareWin", None))
        self.JsonButton.setText(_translate("MainWindow", "JsonFile", None))
        self.ExcelButton.setText(_translate("MainWindow", "ExcenlFile", None))
        self.DataBaseButton.setText(_translate("MainWindow", "DataBaseFile", None))
        self.program.setText(_translate("MainWindow", "comfirm", None))

    def Jsonfile(self):
        self.JsonPath = str(QtGui.QFileDialog.getOpenFileName(self,'open file'))
        print self.JsonPath

    def Excelfile(self):
        self.ExcePath = str(QtGui.QFileDialog.getOpenFileName(self,'open file'))
        print self.ExcePath

    def DataBasefile(self):
        self.DataPath= str(QtGui.QFileDialog.getOpenFileName(self,'open file'))
        print self.DataPath

    def confirmprogram(self):
        programFunction(self.JsonPath, self.ExcePath, self.DataPath)

def Run_Gui():
    app = QtGui.QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    app.exec_()

Run_Gui()
