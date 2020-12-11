#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 19:13
# @Author  : tangsai
# @Site    : 
# @File    : test_token.py
# @Software: PyCharm

import pytest
import allure
import os
import requests
from src.Login_token import login
from common.ExcelRed import Excel
from common.Path import CASE_PATH
from src.Token import Token
from conf.setting import HOST

@allure.feature('查看余额')
class Test_token:
    #第一种方法
    def setup(self,): #每条用例执行之前调用一次--无法实现参数化
        print('每条用例执行之前都执行')
        self.token=login('userName=admin&password=1234')#'userName=admin&password=1234'
    # @pytest.mark('token')
    @pytest.mark.parametrize('indata,resdata',Excel(f'{CASE_PATH}/token&cookie.xls').red_indata())
    @allure.title('查看余额--token方法')
    def test_token(self,indata,resdata):
        resps_data = Token(self.token).query(indata)
        print('这个接口返回的：',resps_data['message'])
        # print('这个excel获取的：',resdata['message'])
        assert resps_data['message']==resdata['message']

    # # #第二种方法：
    # #获取excel文件返回的入参和预期响应结果
    # indata_logins=Excel(f'{CASE_PATH}/login.xls').red_indata()
    # #将入参放入列表
    # indata_login_list=[]
    # for indata_login in indata_logins:
    #     indata_login_list.append(indata_login[0])
    # # print(indata_logins)
    # # print(indata_login_list)
    # #前置函数
    # @pytest.fixture(params=indata_login_list)
    # #scope="function"--默认的  每次执行前都执行一次前置,function（测试函数级别），class（测试类级别），
    # # module（测试模块“.py”级别），session（多个文件级别）。默认是function级别。
    # #  params=indata_login_list
    # def re_token(self,request):
    #     URL = f'{HOST}/pinter/bank/api/login2'
    #     # indata='userName=admin&password=1234'
    #     res_data = requests.post(URL, data=request.param, headers={'content-type': 'application/x-www-form-urlencoded'})
    #     token = res_data.json()['data']
    #     print(res_data.request.body)
    #     print(token)
    #     return token
    #
    # @pytest.mark.parametrize('indata,resdata',Excel(f'{CASE_PATH}/token&cookie.xls').red_indata())
    # def test_token(self,re_token,indata,resdata):
    #     resps_data = Token(re_token).query(indata)
    #     # print('这个接口返回的：',resps_data['message'])
    #     # print('这个excel获取的：',resdata['message'])
    #     assert resps_data['message']==resdata['message']

if __name__=='__main__':
    pytest.main(['test_token.py','-s','--alluredir','../report/tmp5'])
    os.system('allure serve ../report/tmp5')


