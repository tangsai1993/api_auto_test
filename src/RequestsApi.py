#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 18:26
# @Author  : tangsai
# @Site    : 
# @File    : RequestsApi.py
# @Software: PyCharm

import requests
from conf.setting import HOST
from common import Common

import json
import time
class api():
    def requests_api(self,path,inData):
        # path_list = Excel().red_path()
        # for path in path_list:
        #     print(path_list)
        URL = f'{HOST}{path}'
        data=requests.post(URL,json=inData,headers = {'content-type': "application/json"})
        print(data.request.url)
        print(data.request.body)
        print(data.json())
        return data.json()

    def requests_api_param(self,inData,path):
        # path_list = Excel().red_path()
        # for path in path_list:
        #     print(path_list)
        URL = f'{HOST}{path}'
        data=requests.post(URL,data=inData)
        print(data.request.url)
        print(data.request.body)
        print(data.json())
        return data.json()

    def requests_api_md5(self,inData,path):
        URL =f'{HOST}{path}'
        #获取需要加密的字段值
        phoneNum=json.loads(inData)['phoneNum']
        optCode=json.loads(inData)['optCode']
        timestamp=str(int(time.time()))
        # timestamp = str(time.time())
        #把加密的字段合并成一个字段
        md5_str=phoneNum+optCode+timestamp
        sign_result=Common.get_md5(md5_str)
        sign_new={'sign':sign_result}
        #把字符串转换为字典
        dict_inData=eval(inData)
        #字典增加数据{'sign':sign_result}
        dict_inData['sign']=sign_result
        dict_inData['timestamp']=timestamp
        # print(type(dict_inData))
        data = requests.post(URL, data=dict_inData,headers={'content-type':"application/json"})
        print(data.request.url)
        print(data.request.body)
        print(data.json())
        return data.json()


    def post(self,in_data):
        data=requests.post('http://localhost:8080/pinter/com/register',data=in_data,headers = {'content-type':"application/json"})

        print(data.text)
        print(data.request.url)
        print(data.request.body)
        print(data.request.headers)




