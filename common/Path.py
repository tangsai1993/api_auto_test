#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 15:54
# @Author  : tangsai
# @Site    : 
# @File    : Path.py
# @Software: PyCharm

import os

BASE_PATH = os.path.dirname(
    os.path.dirname(__file__)
)

REPORT_PATH = os.path.join(
    BASE_PATH,'report'
)

CASE_PATH= os.path.join(
    BASE_PATH,'case'
)

fileNma_userIfo=f'{CASE_PATH}/userIfo.xls'
fileNma_register=f'{CASE_PATH}/register.xls'
fileNma_buy=f'{CASE_PATH}/buy.xls'
fileNma_cookie=f'{CASE_PATH}/token&cookie.xls'



