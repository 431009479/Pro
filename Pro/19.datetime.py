#!/usr/bin/env python
# coding=utf-8
'''datetime模块'''
from datetime import datetime
now = datetime.now()
print(now)

#创建指定日期对象
date1 = datetime(2015, 7, 17, 11, 30, 20)
print(date1)

#当前时间转时间戳
print(now.timestamp())

print(now.strftime('%Y-%m-%d'))

date2 = datetime.strptime('2018-10-20 10:15:40', '%Y-%m-%d %H:%M:%S')
print(type(date2))
print(date2)
