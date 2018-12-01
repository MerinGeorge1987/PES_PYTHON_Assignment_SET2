#Title: Assignment2---Question33
#Author:Merin
#Version:1
#DateTime:26/11/2018 9:30am
#Summary:Create a list with 7 elements and perform following operations.
#        Let the list be initialized with List1 any 5 city names;
#        a) Append anew city name to the List
#        b) Insert a city name at 4th index position
#        c) Sort the list and print all elements
#        d) Sort the elements of the list in descending order.
#        e) delete last three elements using pop operation



    
    

#list be initialized with List1 any 5 city names
list1 =['Bangalore','Delhi','Kochi','Mumbai','Pune']
mainList=list1

print "List:",mainList

#a) Append anew city name to the List
mainList.append('Hyderabad')
print "Appended List:",mainList

#b) Insert a city name at 4th index position
mainList.insert(4,'Chennai')
print "List after inserting at 4th Index:",mainList

#c) Sort the list and print all elements
mainList.sort()
print "Sorted List:",mainList

#d) Sort the elements of the list in descending order.
mainList.sort(reverse=True)
print "Sorted List in descending order:",mainList

#e) delete last three elements using pop operation
mainList.pop()
mainList.pop()
mainList.pop()
print "Sorted List in descending order after deleting last 3 elements:",mainList



  

