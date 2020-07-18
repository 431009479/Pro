#!/usr/bin/env python
# coding=utf-8
import math
def eare(r):
     return math.pi * r * r

r = float(input("圆的半径:"))
print("半径: " , r , "面积 ：" ,eare(r))

resu = lambda r : math.pi * r * r
print("半径: " , r , "面积 ：" ,resu(r))

print("半径: " , r , "面积 ：" ,(lambda r : math.pi * r * r)(r))

