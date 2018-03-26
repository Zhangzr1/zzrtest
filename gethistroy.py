# -*- coding: UTF-8 -*-
import urllib.request
import numpy
import pandas
import re

class Gethistroydate:
    url = "http://tc.gooooal.com/chartDltSt.action?n1=2016140&n2=2018032"
    # 请求
    request = urllib.request.Request(url)

    # 爬取结果
    response = urllib.request.urlopen(request)

    data = response.read()

    # 设置解码方式
    data = data.decode('utf-8')
    # 打印结果
    print(data)
    print("————————————————————————————")
    # abc1 = re.findall(r'<td class="bg_5">(.*)</td>',data,re.M|re.I)
    # df1 = {'期号':None,'红球':None,'蓝球':None}
    # a1 = []
    # for matchObj in abc1:
    #     a1.append(matchObj)
    #     df1 = {'期号':a1}
    #     print(matchObj)
    # print(a1)
    # print(df1)
    abc2 = re.findall(r'ball_red\'>()</td>',data,re.I|re.M)
    print(abc2)
    df1 = {'期号':None,'红球':None,'蓝球':None}
    a2 = []
    # for matchObj in abc2:
    #     a2.append(matchObj)
    #     df1 = {'红球':a2}
    #     print(matchObj)
    # print(a2)
    # print(df1)




