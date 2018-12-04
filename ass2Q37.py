#!/usr/bin/python

#Title: Assignment2---Question37
#Author:Merin
#Version:1
#DateTime:26/11/2018 3:30pm
#Summary:Create 3 dictionaries(dict1,dict2, dict3) with 3 elements each. Perform following operations
#        a) Compare dictionaries to determine the biggest.
#        b) Add new elements in to the dictionaries dict1, dict2
#        c) print the length of dict1,dict2,dict3.
#        d) Convert dict1, dict2, and dict3 dictionaries as string and concatenate all strings together.


#Dictionary Creation
dict1={'Year':'yy','Month':'mm','Date':'dd'}
dict2={'Hour':'hh','Minute':'mm','Second':'ss'}
dict3={'Country':'C','State':'S','District':'D'}

#a) Compare dictionaries to determine the biggest.
print "dict1:",dict1
print "dict2:",dict2
print "dict3:",dict3
if cmp(dict1,dict2)>0 and cmp(dict1,dict3)>0:
    print dict1," is the greatest"
elif cmp(dict2,dict1)>0 and cmp(dict2,dict3)>0:
    print dict2," is the greatest"
elif cmp(dict3,dict1)>0 and cmp(dict3,dict1)>0:
    print dict3," is the greatest"
else:
    print "All are equal"

#b) Add new elements in to the dictionaries dict1, dict2
dict1['None']='N'
print "New dict1:",dict1

dict2['None']='N'
print "New dict2:",dict2

#c) print the length of dict1,dict2,dict3.
print "Length of dict1:",len(dict1)
print "Length of dict2:",len(dict2)
print "Length of dict3:",len(dict3)

#d) Convert dict1, dict2, and dict3 dictionaries as string and concatenate all strings together.
str1=str(dict1)
str2=str(dict2)
str3=str(dict3)
print "Concatenate of dict1,dict2 & dict3:",str1+str2+str3

