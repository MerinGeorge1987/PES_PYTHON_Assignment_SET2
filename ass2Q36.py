#Title: Assignment2---Question36
#Author:Merin
#Version:1
#DateTime:29/11/2018 8:45am
#Summary: Create two tuples tup1 & tup2 and apply all built in functions on tuples. ( Refer Tutorial for the Built in functions list)


#Tuple Creation
tup1=(10,20,30,40,50)
tup2=('sun','mon','tue','wed','thurs','fri','sat')
print "Tup1:",tup1
print "Tup2:",tup2


#1.all
print "ALL value in tup1 True?",all(tup1)

#2.any
print "ANY value in tup2 True?",any(tup2)

#3.enumerate
print "ENUMERATEd tup2 from 10:",list(enumerate(tup2,10))

#4.len
print "LENgth of tup1:",len(tup1)

#5.max
print "MAX of tup1:",max(tup1)

#6.min
print "MIN of tup2:",min(tup2)

#7.sorted
print "tup2 SORTED in ascending order:",sorted(tup2)
print "tup1 SORTED in descending order:",sorted(tup1,reverse=True)

#8.sum
print "SUM of tup1:",sum(tup1)
