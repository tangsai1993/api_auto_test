# -*- encoding: utf-8 -*-
"""
@File    : conftest.py
@Time    : 2020-12-05 16:30
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""

import pytest

@pytest.fixture(scope='session',autouse=True)
#function 每次执行清除数据 session 执行一次
def start_demo(request):
    print('---开始运行自动化接口---')
    def fin():
        print('---自动化测试---结束')
    request.addfinalizer(fin)