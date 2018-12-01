#Title: Assignment2---Question29_5
#Author:Merin
#Version:1
#DateTime:28/11/2018 6:45pm
#Summary: Apply all built in functions on Strings in your program. Note:There are 40 string functions. Use Tutorial for the help.
#         Note: Each program should have 5 string built in functions

#User Input
string="this is PYTHON"
print "Original string:",string

#33.partition
print"RPARTITION --> substring 'is'",string.rpartition('is ')

#34.rsplit
print "RSPLIT at 1 space",string.rsplit(' ',1)

#35.rstrip
string2 = ' this is good'
print "RSTRIP of ",string2,"is",string2.rstrip()

#36.split
print "SPLIT at 1 space",string.split(' ',1)

#37.splitlines
string3="This\nis\rpython"
print "SPLITLINES of",string3,"is",string3.splitlines()

#38.startswith
print"STARTSWITH 'is' from position 5 to  26?:",string.startswith('is', 5, 26)
print"STARTSWITH 'is'from position 3 to 7?:",string.startswith('is', 3, 7)

#39.strip
string2 = ' this is good'
print "STRIP of ",string2,":",string2.strip()

#40.swapcase
print "SWAPCASE:",string.swapcase()

#41.title
print "TITLE:",string.title()

#42.translate
#String1 = "abc"
#String2 = "ghi"
#String3 = "ab"
#string4 = "abcdef"
#print("Original string:", string4)
#translation = string4.maketrans(String1, String2, String3)
# translate string
#print("TRANSLATEd string:", string4.translate(translation))

#43.upper
print "UPPER cased string:",string.upper()

#44.zfill
print "ZFILL-->",string.zfill(25)





