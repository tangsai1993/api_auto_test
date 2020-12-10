# -*- encoding: utf-8 -*-
"""
@File    : Login_cookie.py
@Time    : 2020-12-06 21:19
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
import requests
from conf.setting import HOST

def login(indata):
    URL = f'{HOST}/pinter/bank/api/login'
    res_data = requests.post(URL, data=indata, headers={'content-type': 'application/x-www-form-urlencoded'})
    # print(res_data.request.headers)
    print(res_data.request.url)
    print(res_data.request.body)
    # print(res_data.headers,res_data.json())
    # re_cookie=res_data.headers['Set-Cookie']
    # re_cookie=str(re_cookie).split(';')[0]
    re_cookie = res_data.cookies
    return re_cookie

if __name__=='__main__':
    cookies=login('userName=admin&password=1234')
    print(cookies)