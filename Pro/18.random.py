#!/usr/bin/env python
# coding=utf-8
import random
#0~1之间的随机数
print(random.random())

#10~100之间的随机数
print(random.randint(10, 100))

#随机列表的一个值
list1 = [1, 2, 3, 5, 7, 9, 17]
print(random.choice(list1))

print(random.choice([120,110,119]))
