#Title: Assignment2---Question34
#Author:Merin
#Version:1
#DateTime:26/11/2018 9:45am
#Summary:Create 3 Lists (list1,list2,list3) with integer and
#        perform following operations
#        a) Create Maxlist by taking 2 maximum elements from each list.
#        b) Find average value from all the elements of Maxlist.
#        c) Create a MinlIst by taking 2 minimum elements from each list 
#        d) Find the average value from all the elements of Minlist



#List Creation
list1 =[10,20,30,40,50]
list2 =[200,20,300,40,500,900]
list3 =[11,22,33,44,55,66,77,88,99]

print "List1:",list1
print "List2:",list2
print "List3:",list3



#a) Create Maxlist by taking 2 maximum elements from each list
maxList=[]
templist1=list1
templist2=list2
templist3=list3
templist1.sort(reverse=True)
templist2.sort(reverse=True)
templist3.sort(reverse=True)

maxList.append(templist1[0])
maxList.append(templist1[1])
maxList.append(templist2[0])
maxList.append(templist2[1])
maxList.append(templist3[0])
maxList.append(templist3[1])
print "MaxList:",maxList

#b) Find average value from all the elements of Maxlist.
avg=sum(maxList)/len(maxList)
print "Average of MaxList:",avg

#c) Create a MinlIst by taking 2 minimum elements from each list 
minList=[]
templist1.sort()
templist2.sort()
templist3.sort()

minList.append(templist1[0])
minList.append(templist1[1])
minList.append(templist2[0])
minList.append(templist2[1])
minList.append(templist3[0])
minList.append(templist3[1])
print "MinList:",minList

#d) Find the average value from all the elements of Minlist
avg=sum(minList)/len(minList)
print "Average of MinList:",avg


  

