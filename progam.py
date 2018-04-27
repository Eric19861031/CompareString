# -*- coding: utf-8 -*-
import sys

from common.configDB import MyDB
from common.configExcel import MyExcel
from common.otherFunction import getCompareId_list

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    JsonFileDir = 'C:\\Program Files (x86)\\Hytera\\MDM\\MDMAdminClient\\MDMAdminClient\\CPS\\addins\\G2_CPS_Public_V2.0.08.011.plug_G2CPS_Public\\RCDB\\Json\\Description.txt'
    DataBaseFileDir = 'C:\\Program Files (x86)\\Hytera\\MDM\\MDMAdminClient\\MDMAdminClient\\CPS\\addins\\G2_CPS_Public_V2.0.08.011.plug_G2CPS_Public\\XMLToolCompactData.sdf;'
    ExcelFile = 'C:\\Program Files (x86)\\Hytera\\MDM\\MDMAdminClient\\MDMAdminClient\\CPS\\addins\\G2_CPS_Public_V2.0.08.011.plug_G2CPS_Public\\Lang_uage.xlsx'

    Exceloj = MyExcel(ExcelFile)
    Exceloj.selectSheet('Param')

    DBoj = MyDB(DataBaseFileDir)
    DBoj.connectDB()

    list = getCompareId_list(JsonFileDir)

    for id in list:
        # print Demo.getalias_Cn(id) + ' and ' + Demo.getalias_En(id) + '\n'
        print 'ID为' + id + '的中英文比对如下\n'

        if Exceloj.get_cn(id) == DBoj.getalias_Cn(id):
            print '中文比对结果：ID为' + id + ': pass' + '\n'
        else:
            print '中文比对结果：ID为' + id + DBoj.getalias_Cn(id) + ' 翻译与需求不符，需求为 ' + Exceloj.get_cn(id) + '\n'

        if Exceloj.get_en(id) == DBoj.getalias_En(id):
            print '英文比对结果：ID为' + id + ': pass' + '\n'
        else:
            print '英文比对结果：ID为' + id + DBoj.getalias_En(id) + ' 翻译与需求不符，需求为 ' + Exceloj.get_en(id) + '\n'


    DBoj.closeDB()
    Exceloj.closeOp()

