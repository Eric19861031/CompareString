# -*- coding: utf-8 -*-
import sys

from common.configDB import MyDB
from common.configExcel import MyExcel
from common.otherFunction import getCompareId_list

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    total , success , fail = 0 , 0 , 0

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
        total += 2
        if Exceloj.get_cn(id) == DBoj.getalias_Cn(id):
            print '中文比对结果：ID为' + id + ': pass' + '----------------------'
            success += 1
        else:
            print '中文比对结果：ID为' + id + DBoj.getalias_Cn(id) + ' 翻译与需求不符，需求为 ' + Exceloj.get_cn(id) + '----------------------'
            fail += 1

        if Exceloj.get_en(id) == DBoj.getalias_En(id):
            print '英文比对结果：ID为' + id + ': pass' + '\n'
            success += 1
        else:
            print '英文比对结果：ID为' + id + DBoj.getalias_En(id) + ' 翻译与需求不符，需求为 ' + Exceloj.get_en(id) + '\n'
            fail += 1

    print '总数 ：' + str(total) + ' ； 成功数目 ：' + str(success) + '； 失败数目 ：' + str(fail) + '； 成功率 ：' + str(success/total)

    DBoj.closeDB()
    Exceloj.closeOp()

