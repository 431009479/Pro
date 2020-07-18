#!/usr/bin/env python
# coding=utf-8
class Struden(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print("{%s} : {%5d}"% (self.name, self.age))

stu1 = Struden('jack', 22)
stu1.show()
stu2 = Struden('bob', 11)
stu2.show()

