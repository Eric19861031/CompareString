# -*- coding: UTF-8 -*-
import adodbapi
import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
sys.setdefaultencoding('utf-8')

# path = os.path.abspath('XMLToolCompactData.sdf')
connstr = 'Provider=Microsoft.SQLSERVER.CE.OLEDB.4.0;' \
          'Data Source=C:\\Program Files (x86)\\Hytera\\MDM\\MDMAdminClient\\MDMAdminClient\\CPS\\addins\\G2_CPS_Public_V2.0.08.011.plug_G2CPS_Public\\XMLToolCompactData.sdf;'

conn = adodbapi.connect(connstr)
myCurser = conn.cursor()
myCurser.execute('select convert(ntext,alias_cn)as a from param where id = 4')
value = myCurser.fetchone()[0]
print value
myCurser.close()