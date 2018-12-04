#!/usr/bin/python

#Title: Assignment2---Question29_3
#Author:Merin
#Version:1
#DateTime:28/11/2018 6:45pm
#Summary: Apply all built in functions on Strings in your program. Note:There are 40 string functions. Use Tutorial for the help.
#         Note: Each program should have 5 string built in functions

#User Input
string="this is PYTHON"
print "Original string:",string

#17.islower
print "ISLOWER -->",string.islower()

#18.isnumeric
#print "ISNUMERIC -->",string.isnumeric()

#19.isprintable
#print "ISPRINTABLE -->",string.isprintable()

#20.isspace
print "ISSPACE -->",string.isspace()

#21.istitle
print "ISTITLE -->",string.istitle()

#22.isupper
print "ISUPPER -->",string.isupper()

#23.join
List1 = ['1', '2', '3', '4']
s = ', '
print "JOIN-->",List1, "&",s,
print s.join(List1)

#24.ljust
print"Left JUSTified string:",string.ljust(20,'*')





