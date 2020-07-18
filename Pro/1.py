#!/usr/bin/env python
# coding=utf-8
import requests
import re
w = 0
name = input('关键字:')
l = int(input('起始页：'))
r = int(input('终止页:'))
for i in range(l, r + 1):
    url = 'https://tieba.baidu.com/f?ie=utf-8&kw='+name+'&ie=utf-8&pn' + str(i * 50)
    r = requests.get(url)
    r.encoding = 'utf-8'
    p = "http.*?\.jpg"
    pic_urls = re.findall(p, r.text);
   # print (pic_urls)
    for pic_url in pic_urls:
        string = './data/tieba/images/'+str(w + 1)+'.jpg'
        pic = requests.get(pic_url)
        with open(string, 'wb') as f:#保存至根目录下
            f.write(pic.content)
            print('成功下载第%s张图片: %s' % (str(w + 1), str(pic_url)))
            w += 1
