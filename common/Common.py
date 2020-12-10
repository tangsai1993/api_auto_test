#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 13:54
# @Author  : tangsai
# @Site    : 
# @File    : common.py
# @Software: PyCharm


import hashlib
import time
'''md5加密'''
def get_md5(password):
    md5_obj = hashlib.md5()
    md5_obj.update(password.encode('utf-8'))
    return md5_obj.hexdigest()

'''生成时间戳'''
def time_tmp():
    timestamp=time.time()
    print(timestamp)



