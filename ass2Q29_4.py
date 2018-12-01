#Title: Assignment2---Question29_4
#Author:Merin
#Version:1
#DateTime:28/11/2018 6:45pm
#Summary: Apply all built in functions on Strings in your program. Note:There are 40 string functions. Use Tutorial for the help.
#         Note: Each program should have 5 string built in functions

#User Input
string="this is PYTHON"
print "Original string:",string

#25.lower
print "LOWER cased string:",string.lower()

#26.lstrip
string1="     python"
print 'LSTRIP of "',string1,'":',string1.lstrip()

#27.maketrans
#dict1 = {"a": "123", "b": "456", "c": "789"}
#string = "abc"
#print(string.maketrans(dict1))

#28.partition
print"PARTITION --> substring 'is'",string.partition('is ')

#29.replace
print "REPLACE 'is' with 'at':",string.replace('is','at')

#30.rfind
print "RFIND Substring 'is':",string.rfind('is')
print "RFIND Substring 'IS':",string.rfind('IS')

#31.rindex
print "RINDEX-->Substring is searched in ' is PYTHON'",
print string.rindex('ON',5)

#32.rjust
print"Right JUSTified string:",string.rjust(20,'*')





