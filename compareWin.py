from PyQt4 import QtGui
from compareGui import Ui_MainWindow

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    app.exec_()