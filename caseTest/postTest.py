# -*- encoding: utf-8 -*-
"""
@File    : postTest.py
@Time    : 2020-12-02 22:46
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""

'''测试请求接口----废弃'''

from common import ExcelRed
from src import RequestsApi
import json


def test_post():
    re_Indata = ExcelRed.Excel().red_Indata()
    # re_Indata = InData.InData()
    for one in re_Indata:
        if one[0] =='/pinter/com/userInfo':
            re_data = RequestsApi.api().requests_api_md5(one[1], one[0])
            re_quest = json.loads(one[2])['message']
            # assert re_data['message'] == re_quest
            if re_data['message'] == re_quest:
                print('--pass--')
            else:
                print('--fail--')
        elif one[0]=='/pinter/com/buy':
            re_data = RequestsApi.api().requests_api_param(one[1],one[0])
            re_quest=json.loads(one[2])['message']
            # assert re_data['message'] == re_quest
            if re_data['message']==re_quest:
                print('--pass--')
            else:
                print('--fail--')
        else:
            re_data=RequestsApi.api().requests_api(one[1],one[0])
            re_quest=json.loads(one[2])["message"]
            # assert re_data['message'] == re_quest
            if re_data['message'] ==re_quest:
                print('--pass--')
            else:
                print('--fail--')
