#!/usr/bin/python

def menu(list,question):
	for entry in list:
		print 1 + list.index(entry),
		print ")" + entry
	try:
		return input(question) - 1
	except NameError:
		print "Enter a corret Number"

answer = menu(['a','b','c'],\
'which letter is your favourite?')

print 'you picked answer ' + (answer + 1)
