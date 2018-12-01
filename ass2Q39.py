#Title: Assignment2---Question39
#Author:Merin
#Version:1
#DateTime:27/11/2018 4:00pm
#Summary: Using Time and Calendar module,Print current date and time. Print current month calendar.


#import time & calendar module
import time
import calendar

#Current date & time
Dttm=time.asctime( time.localtime(time.time()) )
print "Current Date & Time:",Dttm


#Current month calendar
Dttm=time.localtime(time.time())
yy=Dttm.tm_year
mm=Dttm.tm_mon
print "Current month calendar:"
print calendar.month(yy, mm)
