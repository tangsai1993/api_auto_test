# -*- encoding: utf-8 -*-
"""
@File    : Token.py
@Time    : 2020-12-06 20:47
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
import requests
from conf.setting import HOST
from src.Login_token import login
class Token():
    # #第三种方法
    def __init__(self,token):
        self.token=token
    def query(self,indata):
        URL=f'{HOST}/pinter/bank/api/query2'
        re_header={'testfan-token':self.token}
        res_data = requests.get(URL,params=indata,headers=re_header)
        print(res_data.json())
        return res_data.json()
    #第一种方法
    # def __init__(self,indata):
    #     URL=f'{HOST}/pinter/bank/api/login2'
    #     res_data=requests.post(URL,data=indata,headers={'content-type': 'application/x-www-form-urlencoded'})
    #
    #     self.token=res_data.json()['data']
    #
    # def query(self,indata):
    #     URL=f'{HOST}/pinter/bank/api/query2'
    #     re_header={'testfan-token':self.token}
    #     res_data=requests.get(URL,params=indata,headers=re_header)
    #     print(res_data.json())
    #第二种方法
    # def login(self,indata):
    #     URL=f'{HOST}/pinter/bank/api/login2'
    #     res_data=requests.post(URL,data=indata,headers={'content-type': 'application/x-www-form-urlencoded'})
    #     print(res_data.json())
    #     return res_data.json()['data']
    #
    # def query(self,indata):
    #     URL=f'{HOST}/pinter/bank/api/query2'
    #     token=Token().login('userName=admin&password=1234')
    #     print(token)
    #     re_header={'testfan-token':token}
    #     res_data=requests.get(URL,params=indata,headers=re_header)
    #     print(res_data.json())



if __name__=='__main__':
    Token('userName=admin&password=1234').query('userName=admin')