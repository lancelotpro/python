#!/usr/bin/python3

class Human(object):
	sex = "";
	def __init__(self,sex):
		self.sex = sex

class Person(Human):
	name = "";
	def __init__(self,sex,name):
		self.sex = sex
		self.name = name

class Asia(Person):
	sikn = "";
	def __init__(self,sex,name,sikn):
		self.sex = sex
		self.name = name
		self.sikn = sikn

xiaoming = Asia("man","xiaoming","yellow");

print(xiaoming.sex);
print(xiaoming.name);
print(xiaoming.sikn);