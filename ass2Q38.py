#Title: Assignment2---Question38
#Author:Merin
#Version:1
#DateTime:26/11/2018 4:00pm
#Summary:Create 2 dictionaries as follows;
#        dict1 ={'Name':'Ramakrishna','Age':25}
#        dict2={'EmpId':1234,'Salary':5000}
#        Perform following operations   
#           a) Create single dictionary by merging dict1 and dict2
#           b) Update the salary to 10%
#           c) Update the age to 26
#           d) Insert the new element with key "grade" and assign value as "B1"
#           e) Extract and print all values and keys separately.
#           f) delete the element with key 'Age' and print dictionary elements.



#Dictionary Creation
dict1 ={'Name':'Ramakrishna','Age':25}
dict2={'EmpId':1234,'Salary':5000}
print "dict1:",dict1
print "dict2:",dict2

#a) Create single dictionary by merging dict1 and dict2
dict1.update(dict2)
print "Merged dictionary:",dict1

#b) Update the salary to 10%
sal=dict1['Salary']
sal=sal*1.1
dict1['Salary']=sal
print "New Salary of employee ",dict1['EmpId'],"is",dict1['Salary']

#c) Update the age to 26
dict1['Age']=26
print "Age of ",dict1['Name'],"changed to",dict1['Age']

#d) Insert the new element with key "grade" and assign value as "B1"
dict1['grade']='B1'
print "Updated dictionary:",dict1

#e) Extract and print all values and keys separately.
print "Keys of the dictionary:",
for x in dict1:
    print x,",",
print "\nValues of the dictionary:",
for x in dict1.values():
    print x,",",

#f) delete the element with key 'Age' and print dictionary elements.
del dict1["Age"]
print "Updated dictionary:",dict1


