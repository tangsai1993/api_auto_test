#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 15:21
# @Author  : tangsai
# @Site    : 
# @File    : test_register.py
# @Software: PyCharm
from src import RequestsApi
import pytest
import allure
from common import ExcelRed
from common.Path import fileNma_register
from conf import setting
import os
@allure.epic('piner--史诗')
@allure.feature('注册模块')
class Test_register:
    # @pytest.mark('register')
    @allure.title('注册模块标题')
    @allure.story('注册模块的故事')
    @pytest.mark.parametrize('indata,re_reps',ExcelRed.Excel(fileNma_register).red_indata())
    def test_register(self,indata,re_reps):
        re_data=RequestsApi.api().requests_api(setting.PATH_register,indata)
        assert re_data['message'] == re_reps['message']



if __name__=='__main__':
    #-s:输出打印信息； -q  简化输出
    #--alluredir =../report/tmp---生成allure报告需要的源数据
    pytest.main(['test_register.py','-s','--alluredir','../report/tmp'])
    #allure generate---生成报告
    #方案二：allure serve---起服务----自动打开浏览器---一般设置默认浏览器
    os.system('allure serve ../report/tmp')
    #生成报告