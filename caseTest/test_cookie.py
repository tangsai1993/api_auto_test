# -*- encoding: utf-8 -*-
"""
@File    : test_cookie.py
@Time    : 2020-12-06 21:44
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
import pytest
import allure
import os
from src.Login_cookie import login
from common.ExcelRed import Excel
from common.Path import CASE_PATH
from src.Cookie import cookie


@allure.epic('查看余额的史诗级别')
@allure.feature('查看余额模块')
class Test_cookie:
    def setup_class(self): #此方法调用一次
        self.cookie=login('userName=admin&password=1234')
    # @pytest.mark('cookie')
    @allure.story('查看余额')
    @pytest.mark.parametrize('indata,resdata',Excel(f'{CASE_PATH}/token&cookie.xls').red_indata())
    @allure.title('查看余额--cookie方法')
    def test_cookie(self,indata,resdata):
        resp_data=cookie(self.cookie).query(indata)
        assert resp_data['message']==resdata['message']


if __name__=='__main__':
    pytest.main(['test_cookie.py','-s','--alluredir','../report/tmp4'])
    os.system('allure serve ../report/tmp4')
