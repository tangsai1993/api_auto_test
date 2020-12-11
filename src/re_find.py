# -*- encoding: utf-8 -*-
"""
@File    : re_find.py
@Time    : 2020-12-08 23:20
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
'''学习正则表示法获取参数'''

import re
import requests
Host='http://ws.webxml.com.cn'
url=f'{Host}/WebServices/MobileCodeWS.asmx/getMobileCodeInfo'
data='mobileCode=13524564335&userID='
data=requests.post(url,data=data,headers={'Content-Type':'application/x-www-form-urlencoded'})
print(re.findall(data,'上海移动神州行卡'))
print(data.text)