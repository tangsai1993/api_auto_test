#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 16:50
# @Author  : tangsai
# @Site    : 
# @File    : ExcelRed.py
# @Software: PyCharm
'''获取excel文件中数据'''

import xlrd
import json
from common.Path import CASE_PATH
# class open():
#     def open_case(self):
#         sheetdata_list=[]
#         filenames=CasePath.red_case_path()
#         for filename in filenames:
#             # 打开excel文件
#             data = xlrd.open_workbook(f'{CASE_PATH}\{filename}')
#             # 获取第一sheet表数据
#             sheetdata = data.sheet_by_index(0)
#             #加入列表sheetdata_list
#             sheetdata_list.append(sheetdata)
#         return sheetdata_list

from common import Path

class Excel():
    def __init__(self,fileName):
        self.data = xlrd.open_workbook(fileName)
        # 获取第一sheet表数据
        self.sheetdata = self.data.sheet_by_index(0)
        #获取行数
        self.snows=self.sheetdata.nrows

    #读取接口入参路径、数据和期望响应数据
    def red_indata(self):
        res_list=[]
        #继承open中获取多个表sheet1的数据
        # sheetdatas = open().open_case()
        #循环取每个表中sheet1数据
        # for sheetdata in sheetdatas:
            #获取第2行开始第9列的数据
        for  i in range(1,self.snows):
            #获取请求路径
            # re_path=self.sheetdata.cell_value(i,7)
                #获取入参数据
            re_indata=self.sheetdata.cell_value(i,8)
                #获取期望响应数据
            re_data=self.sheetdata.cell_value(i,9)
                #加入列表res_list
            # res_list.append((re_indata,re_data))
            res_list.append((json.loads(re_indata),json.loads(re_data)))
        # print(res_list)
        # for re_list in res_list:
        #     print(re_list)
        return res_list

    def red_indata2(self):
        res_list=[]
        #继承open中获取多个表sheet1的数据
        # sheetdatas = open().open_case()
        #循环取每个表中sheet1数据
        # for sheetdata in sheetdatas:
            #获取第2行开始第9列的数据
        for  i in range(1,14):
            #获取请求路径
            # re_path=self.sheetdata.cell_value(i,7)
                #获取入参数据
            re_indata=self.sheetdata.cell_value(i,8)
                #获取期望响应数据
            re_data=self.sheetdata.cell_value(i,9)
                #加入列表res_list
            res_list.append((json.loads(re_indata),json.loads(re_data)))

            # res_list.append((json.loads(re_indata),json.loads(re_data)))
        # print(res_list)
        # for re_list in res_list:
        #     print(re_list)
        return res_list


    # def red_path(self):
    #     #继承open中获取sheetdata_list数据
    #     path_list=[]
    #     sheetdatas = open().open_case()
    #     for sheetdata in sheetdatas:
    #         for i in range(1,13):
    #          #获取第2行第8列的数据
    #          path=sheetdata.cell_value(i,7)
    #          path_list.append(path)
    #     return  path_list

if __name__=='__main__':
    data=Excel(f'{CASE_PATH}/token&cookie.xls').red_indata()
    # for one in data:
    print(data)


