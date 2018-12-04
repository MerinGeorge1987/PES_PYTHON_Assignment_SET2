#!/usr/bin/python

#Title: Assignment2---Question29_1
#Author:Merin
#Version:1
#DateTime:28/11/2018 6:45pm
#Summary: Apply all built in functions on Strings in your program. Note:There are 40 string functions. Use Tutorial for the help.
#         Note: Each program should have 5 string built in functions

#User Input
string="this is PYTHON"
print "Original string:",string

#1.Capitalize-First character capitalised
print"CAPITALIZE function:",string.capitalize()

#2.Casefold-lowercase
#print"Casefold function:",string.casefold()

#3.center-padded with specified fillchar
print "CENTERed String: ",string.center(24,'*')

#4.count-the number of occurrences of the substring in the given string
print "The COUNT of 'is':", string.count('is',1,10)

#5.encode
# unicode string
#string = 'python!'
# print string
print 'The string is:', string
# ignore error
print 'The ENCODEd version (with ignore) is:', string.encode("ascii", "ignore")

#6.endswith
print"ENDSWITH 'is' from position 7 to  26?:",string.endswith('is', 7, 26)
print"ENDSWITH 'is'from position 3 to 7?:",string.endswith('is', 3, 7)

#7.expandtabs
string = "this\tis\tPYTHON"
print 'Original String:', string
print 'EXPANDTABS --> Tabsize 10:', string.expandtabs(10)

#8.find
string="this is PYTHON"
print "FIND Substring 'is':",string.find('is')
print "FIND Substring 'IS':",string.find('IS')





