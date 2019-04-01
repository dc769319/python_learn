#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print('Name is %s' %(self.name))

    def getAge(self):
        print('Age is %d' %(self.age))



charles = Person('Charles', 28)
charles.getName()
charles.getAge()
