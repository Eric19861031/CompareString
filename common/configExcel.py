#!/usr/bin/python
#!coding:utf8

import openpyxl as op

class MyExcel:
    wb = None
    sheet = None

    def __init__(self,filename):
        self.wb =  op.load_workbook(filename)

    def selectSheet(self,sheet):
        self.sheet = self.wb[sheet]

    def get_en(self,id):
        str1 = ''
        maxValue = self.sheet.max_row
        for i in range(1, maxValue, 1):
            if self.sheet.cell(row=i, column=4).value == int(id):
                if self.sheet.cell(row=i, column=8).value is None:
                    str1 = self.sheet.cell(row=i, column=5).value
                else:
                    str1 = self.sheet.cell(row=i, column=8).value
        return str1

    def get_cn(self,id):
        str2 = ''
        maxValue = self.sheet.max_row
        for i in range(1, maxValue, 1):
            if self.sheet.cell(row=i, column=4).value == int(id):
                if self.sheet.cell(row=i, column=9).value is None:
                    str2 = self.sheet.cell(row=i, column=6).value
                else:
                    str2 = self.sheet.cell(row=i, column=9).value
        return str2

    def closeOp(self):
        self.wb.close()

if __name__ == '__main__':
    ExcelFile = 'C:\\Program Files (x86)\\Hytera\\MDM\\MDMAdminClient\\MDMAdminClient\\CPS\\addins\\G2_CPS_Public_V2.0.08.011.plug_G2CPS_Public\\Lang_uage.xlsx'
    Demo = MyExcel(ExcelFile)
    Demo.selectSheet('Param')
    print Demo.get_cn('1') + ' and ' + Demo.get_en('1')
    Demo.closeOp()