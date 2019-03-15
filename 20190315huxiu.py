#!/usr/bin/env python3      
# -*- coding: utf-8 -*-
import requests
from lxml import etree

if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}

    s = requests.session()

    response = s.get("https://www.huxiu.com/", headers=headers)

    response.encoding = "utf-8"
    res = response.text

    print(res)

    html = etree.HTML(res)

    with open("huxiu.csv", mode="w") as f:
        for i in html.xpath('//div[@class="mod-info-flow"]/div[@class="mod-b mod-art clearfix "]'):
            title = i.xpath('.//a[@class="transition msubstr-row2"]/text()')[0]
            title_url = i.xpath('.//a[@class="transition msubstr-row2"]/@href')[0]
            image_url = i.xpath('.//a[@class="transition"]/img[@class="lazy"]/@data-original')[0]
            author_img = i.xpath('.//div[@class="author-face"]/a/img/@src')[0]
            author_name = i.xpath('.//div[@class="mob-author"]/a/span[@class="author-name "]/text()')[0]
            time = i.xpath('.//div[@class="mob-author"]//span[@class="time"]/text()')[0]
            print((title, title_url, image_url, author_img, author_name, time))

            str = title + "," + title_url + "," + image_url + "," + author_img + "," + author_name + "," + time
            f.write(str)
            f.write("\n")
