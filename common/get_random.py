# -*- encoding: utf-8 -*-
"""
@File    : get_random.py
@Time    : 2020-12-08 23:15
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
'''生成指定长度的随机值'''
import random
def random_20char(length):
    #定义一个空列表
    string=[]
    for i in range(length):
        #生成一个随机值需要转换成字符串
        x = str(random.randint(0, 9))
        #包含数字和字符
        # if x == 1:
        #     y = str(random.randint(0, 9))
        # else:
        #     y = chr(random.randint(97, 122))
        #添加到列表里
        string.append(x)
    #将列表转换成字符串
    string = ''.join(string)
    return string


if __name__ == '__main__':
    length = 20
    qqq = random_20char(length)
    print(qqq)