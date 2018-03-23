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

    matchObj = re.search(r'<td class="bg_5"></td>',data,re.M|re.I)
    print(matchObj)
