# -*- coding: utf-8 -*-
import os
import re

def getCompareId_list(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    all_the_text = open(file_path).read()
    # match your target value
    pattern = re.compile(r'"Id":(\d+)')
    List = pattern.findall(all_the_text)
    return List


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print "---  new folder...  ---"
        print "---  OK  ---"

    else:
        print "---  There is this folder!  ---"

def mkfile(path,name):
    fullpath = path + name + '.txt'



    # if __name__ == '__main__':
#     print getCompareId_list('C:\\Program Files (x86)\\Hytera\\MDM\\MDMAdminClient\\MDMAdminClient\\CPS\\addins\\G2_CPS_Public_V2.0.08.011.plug_G2CPS_Public\\RCDB\\Json\\Description.txt')
