# -*- coding: utf-8 -*-
import os
import sys

import time

from common.configDB import MyDB
from common.configExcel import MyExcel
from common.configFile import Myfile
from common.otherFunction import getCompareId_list

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
sys.setdefaultencoding('utf-8')

def programFunction(JsonFileDir,ExcelFile,DataBaseFileDir):

    # JsonFileDir = 'C:\\Program Files (x86)\\Hytera\\MDM\\MDMAdminClient\\MDMAdminClient\\CPS\\addins\\G2_CPS_Public_V2.0.08.011.plug_G2CPS_Public\\RCDB\\Json\\Description.txt'
    # DataBaseFileDir = 'C:\\Program Files (x86)\\Hytera\\MDM\\MDMAdminClient\\MDMAdminClient\\CPS\\addins\\G2_CPS_Public_V2.0.08.011.plug_G2CPS_Public\\XMLToolCompactData.sdf;'
    # ExcelFile = 'C:\\Program Files (x86)\\Hytera\\MDM\\MDMAdminClient\\MDMAdminClient\\CPS\\addins\\G2_CPS_Public_V2.0.08.011.plug_G2CPS_Public\\Lang_uage.xlsx'

    total, success, fail = 0, 0, 0

    # JsonFileDir =
    # DataBaseFileDir =
    # ExcelFile =

    path = os.path.abspath('Result')
    name = '//' + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + 'Result'
    type = 'txt'

    Exceloj = MyExcel(ExcelFile)
    Exceloj.selectSheet('Param')

    DBoj = MyDB(DataBaseFileDir)
    DBoj.connectDB()

    list = getCompareId_list(JsonFileDir)
    writeStream = Myfile(path,name,type)
    writeStream.open_W()

    for id in list:
        writeStream.file.write('ID为  ' + id + '  的中英文比对如下\n')
        total += 2.0
        if Exceloj.get_cn(id) == DBoj.getalias_Cn(id):
            writeStream.file.write( '中文比对结果：ID为' + id + ': pass' + '   ----------------------   ')
            success += 1.0
        else:
            writeStream.file.write( '中文比对结果：ID为' + id + '；界面显示为：' + DBoj.getalias_Cn(id) + '   翻译与需求不符，需求为：' + Exceloj.get_cn(id) + '   ----------------------   ')
            fail += 1.0

        if Exceloj.get_en(id) == DBoj.getalias_En(id):
            writeStream.file.write( '英文比对结果：ID为' + id + ': pass' + '\n')
            success += 1.0
        else:
            writeStream.file.write( '英文比对结果：ID为' + id + '；界面显示为：' + DBoj.getalias_En(id) + '   翻译与需求不符，需求为：' + Exceloj.get_en(id) + '\n')
            fail += 1.0

    writeStream.file.write( '结论：总数 ：' + str(total) + ' ； 成功数目 ：' + str(success) + '； 失败数目 ：' + str(fail) + '； 成功率 ：' + str(success/total))

    DBoj.closeDB()
    Exceloj.closeOp()

