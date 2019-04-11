#!/usr/bin/env python3      
# -*- coding: utf-8 -*-
import requests
from lxml import etree


def deal_list(data, index=0):
    if len(data) > 1:
        return data[index].replace("\n", "")
    return ""


if __name__ == '__main__':
    s = requests.session()

    h = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}

    res = s.get("https://sh.meituan.com/s/%E5%A1%98%E6%A1%A5/", headers=h)
    html = etree.HTML(res.text)

    print(res.text)

    for i in html.xpath('//div[@class="common-list-main"]/div'):
        # 每个item的id
        data_poiid = deal_list(i.xpath('./@data-poiid'))
        # 每个item的类型id
        data_cateid = deal_list(i.xpath('./@data-cateid'))
        # 文章的url
        action_url = deal_list(
            i.xpath('.//div[@class="default-list-item clearfix"]/a[@class="link list-item-pic backup-color"]/@href'))
        # data_bid
        data_bid = deal_list(
            i.xpath(
                './/div[@class="default-list-item clearfix"]/a[@class="link list-item-pic backup-color"]/@data-bid'))
        # data_lab 智能推荐
        data_lab = deal_list(
            i.xpath(
                './/div[@class="default-list-item clearfix"]/a[@class="link list-item-pic backup-color"]/@data-lab'))
        #
        image_url = deal_list(i.xpath(
            './/div[@class="default-list-item clearfix"]/a[@class="link list-item-pic"]/img[@class="image"]/@src'))
        title = deal_list(i.xpath(
            './/div[@class="list-item-desc"]/div[@class="list-item-desc-top"]/a[@class="link item-title"]/text()'))

        span_list = i.xpath(
            './/div[@class="list-item-desc"]/div[@class="list-item-desc-top"]/div[@class="item-eval-info clearfix"]/span/text()')

        print(span_list)

        pingjia = deal_list(span_list, 0)

        sorce = deal_list(span_list, index=1) + deal_list(span_list, index=2)

        num_people_pinglun = deal_list(span_list, index=3) + deal_list(span_list, index=4)



        print(data_poiid)
        print(data_cateid)
        print(action_url)
        print(data_bid)
        print(data_lab)
        print(image_url)
        print(title)
        print(pingjia)
        print(sorce)
        print(num_people_pinglun)

        print("------------------")
