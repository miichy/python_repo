#!/usr/bin/python
#string operate
### wrong
#v = '2' - '1'
#print v
#a = 'eggs'/'easy'
#print a
#b = 'third' * 'a charm'
#print b
###

f = 'hello'
b = 'world'
print f + b

var1 = 'hello world'
var2 = 'python programming'

print "var1[0]: ",var1[0]
print "var2[1:5]: ",var2[1:5] 

print "updated string :- ",var1[:6] + "python"

print "My name is %s and weight is %d kg!" % ('Zara', 21)

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print para_str; 
