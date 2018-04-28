# -*- coding: UTF-8 -*-
import os

import adodbapi
import sys

import time

from common.configFile import Myfile

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
sys.setdefaultencoding('utf-8')

# path = os.path.abspath('XMLToolCompactData.sdf')
# connstr = 'Provider=Microsoft.SQLSERVER.CE.OLEDB.4.0;' \
#           'Data Source=C:\\Program Files (x86)\\Hytera\\MDM\\MDMAdminClient\\MDMAdminClient\\CPS\\addins\\G2_CPS_Public_V2.0.08.011.plug_G2CPS_Public\\XMLToolCompactData.sdf;'
#
# conn = adodbapi.connect(connstr)
# myCurser = conn.cursor()
# myCurser.execute('select convert(ntext,alias_cn)as a from param where id = 4')
# value = myCurser.fetchone()[0]
# print value
# myCurser.close()

if __name__ == '__main__':
    path = os.path.abspath('Result')
    name = '//' + time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())) + 'Result'
    type = 'txt'
    Demo = Myfile(path,name,type)
    Demo.open_W()
    Demo.file.write("123")