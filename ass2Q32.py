#Title: Assignment2---Question32
#Author:Merin
#Version:1
#DateTime:24/11/2018 4:30pm
#Summary:Write a program to perform following operations on List. Create three lists as List1,List2 and List3 having 5 city names each list.
#        a. Find the length city of each list element and print city and length
#        b. Find the maximum and minimum string length element of each list
#        c. Compare each list and determine which city is biggest & smallest with length.
#        d. Delete first and last element of each list and print list contents.

#Function Body for 'findLength'
def findLength(listL):
    for x in range(5):
        print listL[x],"\t\t\t",len(listL[x])
        
#Function Body for 'findMinMax'
def findMinMax(listL,y):
    length = []
    for x in range(5):
        length.append(len(listL[x]))
    for x in range(5):
        if length[x]==min(length):
            print listL[x],"has minimum length in List",y
        elif length[x]==max(length):
            print listL[x],"has maximum length in List",y
            
#Function Body for 'findMinMaxinAll'
def findMinMaxinAll(list1,list2,list3):
    minLen=100;maxLen=0
    for y in range(3):
        if y==0:
            listL=list1
        elif y==1:
            listL=list2
        else:
            listL=list3
            
        length = []
        for x in range(5):
            length.append(len(listL[x]))
        for x in range(5):
            if length[x]==min(length)and length[x]<minLen:
                minLen=length[x];minElement=listL[x]
            elif length[x]==max(length)and length[x]>maxLen:
                maxLen=length[x];maxElement=listL[x]
    print "\nCity with smallest length among 3 lists:",minElement
    print "City with biggest length among 3 lists:",maxElement
    
    

# List Creation
list1 =['Zurich','Lucern','Interlaken','Lauterbrunnen','Lugano']
list2=['Bangalore','Delhi','Kochi','Mumbai','Pune']
list3=['London','Leeds','Manchester','Southampton','Watford']

#a.Find the length city of each list element and print city and length
print "City Name\t\tLength"
findLength(list1)
findLength(list2)
findLength(list3)

#b.Find the maximum and minimum string length element of each list
print "\nthe maximum and minimum string length element of each list:"
findMinMax(list1,1)
findMinMax(list2,2)
findMinMax(list3,3)

#c.Compare each list and determine which city is biggest & smallest with length.

findMinMaxinAll(list1,list2,list3)

#d.Delete first and last element of each list and print list contents
list1.pop(0);list1.pop()
list2.pop(0);list2.pop()
list3.pop(0);list3.pop()
print "\nLists after deleting first & last element:"
print "List1-->",list1
print "List2-->",list2
print "List3-->",list3

  

