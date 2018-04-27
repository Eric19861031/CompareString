from Excel import FindExcel
from common.configDB import MyDB
from common.otherFunction import getCompareId_list


if __name__ == '__main__':
    JsonFileDir = 'C:\\Program Files (x86)\\Hytera\\MDM\\MDMAdminClient\\MDMAdminClient\\CPS\\addins\\G2_CPS_Public_V2.0.08.011.plug_G2CPS_Public\\RCDB\\Json\\Description.txt'
    DataBaseFileDir = 'C:\\Program Files (x86)\\Hytera\\MDM\\MDMAdminClient\\MDMAdminClient\\CPS\\addins\\G2_CPS_Public_V2.0.08.011.plug_G2CPS_Public\\XMLToolCompactData.sdf;'
    Demo = MyDB(DataBaseFileDir)
    Demo.connectDB()
    list = getCompareId_list(JsonFileDir)
    for id in list:
        # print Demo.getalias_Cn(id) + ' and ' + Demo.getalias_En(id) + '\n'
        print FindExcel(int(id),'Lang_uage.xlsx')[0]