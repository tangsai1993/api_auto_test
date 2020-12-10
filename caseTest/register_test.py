#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 13:57
# @Author  : tangsai
# @Site    : 
# @File    : register_test.py
# @Software: PyCharm

from common import ExcelRed
from common.Path import fileNma_register
from src import RequestsApi
from conf import setting
import json



def register_test():
    data = ExcelRed.Excel(fileNma_register).red_indata()
    for body_data in data:
        re_data=RequestsApi.api().requests_api(setting.PATH_register,body_data[0])
        re_reps=json.loads(body_data[1])['message']
        if re_data['message']==re_reps:
            print('----->pass---->')
        else:
             print('----->fail---->')



# if __name__ == '__main__':
#         register_test()
