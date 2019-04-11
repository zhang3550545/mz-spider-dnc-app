#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import random
import time

import requests
from requests.cookies import RequestsCookieJar


def get_data(cookie, offset):
    """
    递归获取数据
    :param cookie: cookie信息，需要拼接url，uuid=cookie
    :param offset: offset值
    """
    # 真正获取数据的接口
    url = "https://apimobile.meituan.com/group/v4/poi/pcsearch/10?uuid=%s&userid=-1&limit=32&offset=%s&cateId=-1&q=塘桥" % (
        cookie, offset)
    print("真正获取数据的url：%s" % url)
    cookie_jar = RequestsCookieJar()
    cookie_jar.set("uuid", cookie)
    # 将cookie数据放入请求中
    res2 = s.get(url, headers=headers, cookies=cookie_jar)
    # 将返回的数据解析成字典类型。
    dicts = json.loads(res2.text)
    # 获取的数据结构，searchResult表示真正展示的数据，通过searchResult结果做判断
    search_result = dicts["data"]["searchResult"]
    if search_result != [] and len(search_result) > 0:
        with open("result.json", mode="a") as f:
            # 将结果数据写入文件
            f.write(res2.text)
            f.write("\n")
            # 随机休息3-12秒，模拟用户的正常行为，可以随意
            time.sleep(random.randint(3, 12))
            # 递归调用，offset以32递增
            get_data(cookie, offset + 32)
    else:
        print("数据请求结束...")


pass

if __name__ == '__main__':
    """
    通过美团的PC端网站，获取美团塘桥地区的数据（该数据包含所有数据，如果需要区分类型，需要研究获取的数据当中的字段包含的含义）
    
    代码请求策略：
    
        1.请求美团塘桥地区的url，如：https://sh.meituan.com/s/%E5%A1%98%E6%A1%A5/
        2.获取该页面返回的cookies信息
        3.通过递归的方式，请求真正返回数据的接口。详见get_data()
    """

    s = requests.session()

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3759.4 Safari/537.36",
        "Connection": "keep-alive",
        "Origin": "https://sh.meituan.com",
        "Referer": "https://sh.meituan.com/s/%E5%A1%98%E6%A1%A5/",
        "Accept": "*/*"}

    # 第一步
    res = s.get(url="https://sh.meituan.com/s/%E5%A1%98%E6%A1%A5/", headers=headers)
    # 第二步
    cookie = res.cookies.get("uuid")
    print("从请求页面获取cookies：%s" % cookie)
    # 第三步
    get_data(cookie, 0)
