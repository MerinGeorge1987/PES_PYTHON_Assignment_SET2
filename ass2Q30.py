#!/usr/bin/python

#Title: Assignment2---Question30
#Author:Merin
#Version:1
#DateTime:29/11/2018 8:30am
#Summary: Write a program to Sort given N numbers (Use only loop structures and Conditions to sort the elements.
#         Use Bubble sort / Selection sort technique to sort the elements of List)Note: Don't use built in functions to sort.


#User Input
num=[int(x) for x in raw_input("Enter N numbers to be sorted (separated with space):").split()]

#Bubble Sort
for x in range(len(num)-1,0,-1):
    for i in range(x):
        if num[i]>num[i+1]:
            temp = num[i]
            num[i] = num[i+1]
            num[i+1] = temp
#Print result
print "Sorted List:",num
