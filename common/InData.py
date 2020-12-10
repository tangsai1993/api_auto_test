#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 12:32
# @Author  : tangsai
# @Site    : 
# @File    : InData.py
# @Software: PyCharm
'''获取excel文件中返回的 请求地址、参数和逾期响应数据存在-----废弃'''
from common.ExcelRed import Excel
def InData():
    Indatas=Excel().red_Indata()
    return Indatas