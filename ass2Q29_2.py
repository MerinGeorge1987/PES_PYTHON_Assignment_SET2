#!/usr/bin/python

#Title: Assignment2---Question29_2
#Author:Merin
#Version:1
#DateTime:28/11/2018 6:45pm
#Summary: Apply all built in functions on Strings in your program. Note:There are 40 string functions. Use Tutorial for the help.
#         Note: Each program should have 5 string built in functions

#User Input
string="this is PYTHON"
print "Original string:",string


#9.format
print "FORMAT --> This is {}.".format("Python")

#10.format_map
#dict1 = {'x':4,'y':-5}
#print "FORMAT_MAP-->",'{x} {y}'.format_map(dict1)

#11.index
print "INDEX-->Substring is searched in ' is PYTHON'",
print string.index('ON',5)

#12.isalnum
print "ISALNUM-->",string.isalnum()

#13.isalpha
print "ISALPHA-->",string.isalpha()

#14.isdecimal
#print "ISDECIMAL -->",string.isdecimal()

#15.isdigit
print "ISDIGIT -->",string.isdigit()

#16.isidentifier
#print "ISIDENTIFIER -->",string.isidentifier()


