#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 18:47
# @Author  : tangsai
# @Site    : 
# @File    : Log.py
# @Software: PyCharm
import logging.config
from conf import setting

# 添加日志功能: (日志功能在接口层 使用)
def get_logger(log_type):  # log_type ---> user
    '''
    :param log_type: 比如是 user日志，bank日志，购物商城日志
    :return:
    '''
    # 1、加载日志配置信息
    logging.config.dictConfig(
        setting.LOGGING_DIC
    )

    # 2、获取日志对象
    logger = logging.getLogger(log_type)

    return logger