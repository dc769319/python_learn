#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class Animal:

    def eat(self):
        print('%s eat' %(self.name))

    def run(self):
        print('%s run' %(self.name))


class Cat(Animal):

    def __init__(self, voice):
        self.name = 'Cat'
        self.voice = voice

    def cry(self):
        print(self.voice)


class Dog(Animal):

    def __init__(self, voice):
        self.name = 'Dog'
        self.voice = voice

    def cry(self):
        print(self.voice)

catA = Cat('喵喵喵')
catA.eat()
catA.run()
catA.cry()

dogB = Dog('汪汪汪')
dogB.eat()
dogB.run()
dogB.cry()

