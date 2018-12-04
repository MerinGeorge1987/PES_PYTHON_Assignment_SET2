#!/usr/bin/python

#Title: Assignment2---Question35
#Author:Merin
#Version:1
#DateTime:26/11/2018 2:45pm
#Summary:Create Tuple as specified below;
#        a) Create a Tuple tup1 with days in a week & print the tuple elements
#        b) Create a Tuple tup2  with months in a year and concatenate it with tup1
#        c) Create 3 tuples( tup1,tup2,tup3) with numbers and determine which is greater.
#        d) Try to delete an individual element in tup1 and try deleting complete Tuple -tup1 notice the error type you get.
#        e) Insert new element in to tuple by typecasting it to List



#a)Create a Tuple tup1 with days in a week
tup1 =('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')

print "Tuple 1:",tup1

#b)Create a Tuple tup2  with months in a year and concatenate it with tup1
tup2=('January','February','March','April','May','June','July','August','September','October','November','December')

print "Tuple 2:",tup2
print "Concatenation of Tuple 1 & 2:",tup1+tup2

#c)Create 3 tuples( tup1,tup2,tup3) with numbers and determine which is greater.
tup1=(1,2,3,4,5,6,7,8,9,10)
tup2=(10,2,30,4,50,6,70,8,90,10)
tup3=(1,20,3,40,5,60,7,80,9,100)
print "tup1:",tup1
print "tup2:",tup2
print "tup3:",tup3
if cmp(tup1,tup2)>0 and cmp(tup1,tup3)>0:
    print tup1," is the greatest"
elif cmp(tup2,tup1)>0 and cmp(tup2,tup3)>0:
    print tup2," is the greatest"
elif cmp(tup3,tup1)>0 and cmp(tup3,tup1)>0:
    print tup3," is the greatest"
else:
    print "All are equal"
#d)Try to delete an individual element in tup1 and try deleting complete Tuple -tup1 notice the error type you get.

#tup1.pop(2)
#print tup1
#      Error Message:
#           Traceback (most recent call last):
#           File "C:/Users/deepu/Desktop/MERIN/PYTHON/ass2Q35.py", line 41, in <module>
#           tup1.pop(2)
#           AttributeError: 'tuple' object has no attribute 'pop'

del tup1
#print "tup1:",tup1
#     Error Messgae:
#           Traceback (most recent call last):
#           File "C:/Users/deepu/Desktop/MERIN/PYTHON/ass2Q35.py", line 49, in <module>
#           print "tup1:",tup1
#           NameError: name 'tup1' is not defined

#e) Insert new element in to tuple by typecasting it to List

tempList=list(tup2)
tempList.insert(2,'Inserted Element')
tup2=tuple(tempList)
print "tup2 with an inserted element( by typecasting it to List):",tup2

   
