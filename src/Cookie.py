# -*- encoding: utf-8 -*-
"""
@File    : Cookie.py
@Time    : 2020-12-06 14:33
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
import requests
from conf.setting import HOST
class cookie:
    def __init__(self,cookie):
        self.cookie=cookie

    def query(self,indata):
        URL = f'{HOST}/pinter/bank/api/query'
        # re_headers={'cookie':re_cookie}
        res_data=requests.get(URL,params=indata,cookies=self.cookie)
        # print(res_data.request.url)
        # print(res_data.request.body)
        # print(res_data.request.headers)
        # print(res_data.text)
        return res_data.json()
    # def login(self,indata):
    #     URL=f'{HOST}/pinter/bank/api/login'
    #     res_data=requests.post(URL,data=indata,headers={'content-type': 'application/x-www-form-urlencoded'})
    #     # print(res_data.request.headers)
    #     print(res_data.request.url)
    #     print(res_data.request.body)
    #     # print(res_data.headers,res_data.json())
    #     # re_cookie=res_data.headers['Set-Cookie']
    #     # re_cookie=str(re_cookie).split(';')[0]
    #     re_cookie=res_data.cookies
    #     return re_cookie
    #
    # def query(self,indata):
    #     URL = f'{HOST}/pinter/bank/api/query'
    #     re_cookie=cookie().login('userName=admin&password=1234')
    #     print(re_cookie)
    #     # re_headers={'cookie':re_cookie}
    #     res_data=requests.get(URL,params=indata,cookies=re_cookie)
    #     print(res_data.request.url)
    #     print(res_data.request.body)
    #     print(res_data.request.headers)
    #     print(res_data.text)





if __name__=='__main__':
        # cookie().login('userName=admin&password=1234')
        cookie().query({"userName":"admin"})# "userName": "admin"       userName=admin
