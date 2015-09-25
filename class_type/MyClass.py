#!/usr/bin/env python
# -*- coding=utf-8 -*-

class MyClass:
	""" simple   """
	i = 12
	def say(self):
		print "hello"
		return "hello,world"

class Pet(object):
	def __init__(self,name,species):
		self.name = name
		self.species = species

	def getName(self):
		return self.name

	def getSpecies(self):
		return species

	def __str__(self):
		return "%s is a %s" % (self.name,self.species)

if __name__ == "__main__":
	x = MyClass()
	x.say()
	print x.i

	print "========="

	polly = Pet("polly","cat")
	print polly
	harry = Pet("harry","dog")
	print harry.getName()