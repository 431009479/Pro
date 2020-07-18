#!/usr/bin/env python
# coding=utf-8

#a = 5
#if a % 2 == 0:
#    print("a is even!")
#else:
#    pass

a = [
        ["1", 18, "河南"],
        ["2", 20, "北极"],
        ["3", 22, "黑龙江"]
]
for m in range(3):
    for n in range(3):
        print(a[m][n],end="\t")
    print()
