#coding=utf-8

import os
import sys
import time
from PyQt4 import QtCore, QtGui

from common.configDB import MyDB
from common.configExcel import MyExcel
from common.configFile import Myfile
from common.otherFunction import getCompareId_list

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

class Ui_Form(QtGui.QMainWindow):

    JsonPath = ''
    ExcePath = ''
    DataPath = ''

    def __init__(self,JsonPath,ExcePath,DataPath,parent=None):
        super(Ui_Form, self).__init__(parent)
        self.JsonPath = JsonPath
        self.ExcePath = ExcePath
        self.DataPath = DataPath
        self.setupUi(self)
        # app = QtGui.QApplication(sys.argv)
        self.show()
        self.Thread = BigWorkThread(self.JsonPath,self.ExcePath,self.DataPath)
        self.Thread.start()
        self.connect(self.Thread,QtCore.SIGNAL('progressVal'),self.progressBar)
        self.connect(self.Thread,QtCore.SIGNAL('closesignal'),self.close_Progress)
        # app.exec_()

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(312, 62)
        self.progress = QtGui.QProgressBar(Form)
        self.progress.setGeometry(QtCore.QRect(10, 20, 301, 23))
        self.progress.setProperty("value", 0)
        self.progress.setObjectName(_fromUtf8("progressBar"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "progress", None))

    def progressBar(self,val):
        self.progress.setValue(val)

    def close_Progress(self):
        self.close()

class BigWorkThread(QtCore.QThread):
    """docstring for BigWorkThread"""
    JsonPath = ''
    ExcePath = ''
    DataPath = ''
    def __init__(self, JsonPath,ExcePath,DataPath,parent=None):
        super(BigWorkThread, self).__init__(parent)
        self.JsonPath = JsonPath
        self.ExcePath = ExcePath
        self.DataPath = DataPath

    #重写 run() 函数，在里面干大事。
    def run(self):
        success, fail = 0.0, 0.0

        path = os.path.abspath('Result')
        name = '//' + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + 'Result'
        type = 'txt'

        Exceloj = MyExcel(self.ExcePath)
        Exceloj.selectSheet('Param')

        DBoj = MyDB(self.DataPath)
        DBoj.connectDB()

        list = getCompareId_list(self.JsonPath)
        total = len(list) * 2
        writeStream = Myfile(path, name, type)
        writeStream.open_W()

        for id in list:
            writeStream.file.write('ID为  ' + id + '  的中英文比对如下\n')
            if Exceloj.get_cn(id) == DBoj.getalias_Cn(id):
                writeStream.file.write('中文比对结果：ID为' + id + ': pass' + '   ----------------------   ')
                success += 1.0
            else:
                writeStream.file.write(
                    '中文比对结果：ID为' + id + '；界面显示为：' + DBoj.getalias_Cn(id) + '   翻译与需求不符，需求为：' + Exceloj.get_cn(
                        id) + '   ----------------------   ')
                fail += 1.0

            if Exceloj.get_en(id) == DBoj.getalias_En(id):
                writeStream.file.write('英文比对结果：ID为' + id + ': pass' + '\n')
                success += 1.0
            else:
                writeStream.file.write(
                    '英文比对结果：ID为' + id + '；界面显示为：' + DBoj.getalias_En(id) + '   翻译与需求不符，需求为：' + Exceloj.get_en(
                        id) + '\n')
                fail += 1.0

            if (success + fail) / total >= 100:
                self.program.setText('completed')
            val = (success + fail) * 100 / total
            self.emit(QtCore.SIGNAL('progressVal'),val)

        writeStream.file.write(
            '结论：总数 ：' + str(total) + ' ； 成功数目 ：' + str(success) + '； 失败数目 ：' + str(fail) + '； 成功率 ：' + str(
                success / total))

        DBoj.closeDB()
        Exceloj.closeOp()
        self.emit(QtCore.SIGNAL('closesignal'))



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Ui_Form('C:\\Program Files (x86)\\Hytera\\MDM\\MDMAdminClient\\MDMAdminClient\\CPS\\addins\\G2_CPS_Public_V2.0.08.011.plug_G2CPS_Public\\RCDB\\Json\\Description.txt',
                  'C:\\Program Files (x86)\\Hytera\\MDM\\MDMAdminClient\\MDMAdminClient\\CPS\\addins\\G2_CPS_Public_V2.0.08.011.plug_G2CPS_Public\\Lang_uage.xlsx',
                  'C:\\Program Files (x86)\\Hytera\\MDM\\MDMAdminClient\\MDMAdminClient\\CPS\\addins\\G2_CPS_Public_V2.0.08.011.plug_G2CPS_Public\\XMLToolCompactData.sdf;')

    app.exec_()