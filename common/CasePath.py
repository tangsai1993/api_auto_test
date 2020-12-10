#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 10:00
# @Author  : tangsai
# @Site    : 
# @File    : CasePath.py
# @Software: PyCharm
'''获取测试用例名称'''
import os
from common.Path import CASE_PATH
def red_case_path():
    filenames =os.listdir(CASE_PATH)
    return filenames
