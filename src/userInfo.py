# -*- encoding: utf-8 -*-
"""
@File    : userInfo.py
@Time    : 2020-12-06 14:01
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
import requests
import time
import random
from common import Common
from conf.setting import HOST
from common.get_random import random_20char
from common.Log import logger

log=logger()
def userIfo(inData):
    Num_random=random_20char(8)

    URL = f'{HOST}/pinter/com/userInfo'
    # 获取需要加密的字段值
    phoneNum = '138' + Num_random
    optCode = inData['optCode']
    timestamp = str(int(time.time()*1000))
    # 把加密的字段合并成一个字段
    md5_str = phoneNum + optCode + timestamp
    # print(type(md5_str))
    sign_result = Common.get_md5(md5_str)
    dict_inData = inData
    # 字典增加数据{'sign':sign_result}
    dict_inData['timestamp'] = timestamp
    dict_inData['sign'] = sign_result
    dict_inData['phoneNum']=phoneNum
    # print(dict_inData)
    data = requests.post(URL, json=dict_inData, headers={'content-type': "application/json"})
    re_url = data.request.url
    log.info(f'用户登录请求地址为；{re_url}')
    log.info(f'用户登录请求参数为：{data.request.body}')
    log.info(f'用户登录返回响应为：{data.json()}')
    print(data.request.url)
    print(data.request.body)
    print(data.json())
    return data.json()

if __name__=='__main__':
    userIfo({'phoneNum':'15346653457','optCode':'testfan'})

