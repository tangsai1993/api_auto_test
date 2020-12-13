# -*- encoding: utf-8 -*-
"""
@File    : test_userIfo.py
@Time    : 2020-12-06 14:12
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
import pytest
import allure
import os
from src import userInfo
from common.ExcelRed import Excel
from common.Path import fileNma_userIfo
#获取参数
@allure.feature('用户登录')
class Test_UserIfo():
    @allure.story('测试用户登录')
    @allure.title('用户登录')
    @pytest.mark.parametrize('indata,redata', Excel(fileNma_userIfo).red_indata())
    def test_userIfo(self,indata,redata):
        #调用src包中userInfo接口请求函数
        resp_data=userInfo.userIfo(indata)
        #断言
        assert resp_data['message'] == redata['message']

if __name__ == '__main__':
    pytest.main(['test_userIfo.py','-s','--alluredir','../report/tmp1'])
    os.system('allure serve ../report/tmp1')