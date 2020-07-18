#!/usr/bin/env python
# coding=utf-8

num = [0 for i in range(101)]

for i in  range(2, 100):
    if num[i] == 0:
        num[0] += 1
        num[num[0]] = i
    
    for j in range(1,num[0] + 1):
        if i * num[j] > 100:
            break
        num[i * num[j]] = 1
        if i % num[j] == 0:
            break;

for i in range(1, num[0] + 1):
    print(num[i])
