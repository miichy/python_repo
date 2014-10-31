#!/usr/bin/python
import time;
import calendar

print time
ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks

localtime = time.localtime(time.time())
print "Local current time: ",localtime

localtime = time.asctime(time.localtime(time.time()))
print "Local current time: ",localtime

cal = calendar.month(2008,1)
print "here is calendar:"
print cal
