# -*- encoding: utf-8 -*-
"""
@File    : Login_token.py
@Time    : 2020-12-06 21:31
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
import requests
from conf.setting import HOST

def login(indata):
    URL = f'{HOST}/pinter/bank/api/login2'
    res_data = requests.post(URL, data=indata, headers={'content-type': 'application/x-www-form-urlencoded'})
    token = res_data.json()['data']
    print(token)
    return token

if __name__=='__main__':
    login('userName=admin&password=1234')