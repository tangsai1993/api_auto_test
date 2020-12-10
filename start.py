#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 15:54
# @Author  : tangsai
# @Site    : 
# @File    : start.py
# @Software: PyCharm

import pytest
import os
import allure
from common.Path import REPORT_PATH


if __name__=='__main__':
    #定义报告地址
    report_path=os.path.join(
        REPORT_PATH,'tmp'
    )
    #-s:输出打印信息； -q  简化输出
    #--alluredir =../report/tmp---生成allure报告需要的源数据
    pytest.main(['-s','--alluredir',report_path])
    #allure generate---生成报告
    #方案二：allure serve---起服务----自动打开浏览器---一般设置默认浏览器
    os.system(f'allure serve {report_path}')
    #生成报告
