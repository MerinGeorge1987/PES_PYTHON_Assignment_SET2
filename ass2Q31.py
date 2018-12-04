#!/usr/bin/python

#Title: Assignment2---Question31
#Author:Merin
#Version:1
#DateTime:24/11/2018 4:30pm
#Summary:Write a program to search an element in the list.
#        i.e. Perform the binary search on the sorted list having integers as elements.
#        If the search is successful print "Success" else print "un successful search".
  
# Function Body for Binary Search
def binarySearch (list1, startIndx, stopIndx, search): 
   
    if stopIndx >= startIndx: 
  
        mid = (startIndx + stopIndx) /2
  
        # If element is present at the middle itself 
        if list1[mid] == search: 
            return mid
           
        # If element is smaller than mid then search in the left half
        elif list1[mid] > search: 
            return binarySearch(list1, startIndx, mid-1, search) 
  
        # Else search in the right half 
        else: 
            return binarySearch(list1, mid+1, stopIndx, search) 
  
    else: 
        # Element is not present in the list1ay 
        return -1
  
  
# User Input
list1 = [int(x) for x in raw_input('Enter a list of integers:').split()]
list1.sort()
search=input('Enter an Integer to search from above list:')

  
# Function call for Binary Search
result = binarySearch(list1, 0, len(list1)-1, search) 

#Print result  
if result >=0: 
    print "Sucess" 
else: 
    print "un successful search"
