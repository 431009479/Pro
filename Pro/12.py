#!/usr/bin/env python
# coding=utf-8

#父类
class Animal:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("{} run...".format(self.name))
#子类
class Cat(Animal):

    #重写父类的方法
    def __init__(self, name, color):
        #调用父类的方法
        super().__init__(name)
        self.color = color
    def show(self):
        print("name = {}, color = {}".format(self.name, self.color))

#子类
class Dog(Animal):
    #重写父类的方法
    def run(self):
        print("{} run speed fast...".format(self.name))
#创建对象
cat = Cat("mi", "black")
dog = Dog("K")
#调用方法
cat.show()
cat.run()
dog.run()

