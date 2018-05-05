# -*- coding: UTF-8 -*-
import adodbapi

class MyDB:
    MyCursor = None
    constr = None

    def __init__(self,dir):
        """
        :param dir:将对应数据库文件的路径放入
        """
        self.constr = 'Provider=Microsoft.SQLSERVER.CE.OLEDB.4.0;Data Source='+ dir

    def connectDB(self):
        """
        connect to database
        :return:
        """
        conn = adodbapi.connect(self.constr)
        self.MyCursor = conn.cursor()

    def getalias_En(self,id):
        try:
            operation_queryen = 'select convert(ntext,alias_en)as a from param where id = '
            self.MyCursor.execute(operation_queryen+id)
            value = self.MyCursor.fetchone()[0]
            return value
        except:
            return ' no value about this id '

    def getalias_Cn(self,id):
        try:
            operation_queryen = 'select convert(ntext,alias_cn)as a from param where id = '
            self.MyCursor.execute(operation_queryen+id)
            value = self.MyCursor.fetchone()[0]
            return value
        except:
            return ' no value about this id '

    def closeDB(self):
        """
        close database
        :return:
        """
        self.MyCursor.close()
        print("Database closed!")

if __name__ == '__main__':
    Demo = MyDB('C:\\Program Files (x86)\\Hytera\\MDM\\MDMAdminClient\\MDMAdminClient\\CPS\\addins\\G2_CPS_Public_V2.0.08.011.plug_G2CPS_Public\\XMLToolCompactData.sdf;')
    Demo.connectDB()
    print Demo.getalias_En('1') + ' and ' + Demo.getalias_Cn('1')
    Demo.closeDB()
