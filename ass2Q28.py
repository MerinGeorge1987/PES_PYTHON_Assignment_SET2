#Title: Assignment2---Question28
#Author:Merin
#Version:1
#DateTime:28/11/2018 5:15pm
#Summary: Write a program to check how many vowels present in the given string.
#         That is, count the number of " a e i o u" in the given string and print the numbers against each vowel.
#         Example:- "This is Python" Number of total vowels = 3, i = 2, o =1


#User Input
string=input('Enter a string(within quotes):')

#Count the vowels
vowels={'a':0,'e':0,'i':0,'o':0,'u':0}
for x in range(len(string)):
    if cmp(string[x],'a')==0 or cmp(string[x],'A')==0:
        vowels['a']=vowels['a']+1
    elif cmp(string[x],'e')==0 or cmp(string[x],'E')==0:
        vowels['e']=vowels['e']+1
    elif cmp(string[x],'i')==0 or cmp(string[x],'I')==0:
        vowels['i']=vowels['i']+1
    elif cmp(string[x],'o')==0 or cmp(string[x],'O')==0:
        vowels['o']=vowels['o']+1
    elif cmp(string[x],'u')==0 or cmp(string[x],'U')==0:
        vowels['u']=vowels['u']+1

#Print result
print "Number of total vowels:",vowels['a']+vowels['e']+vowels['i']+vowels['o']+vowels['u'],
if vowels['a']!=0:
    print ", a=",vowels['a'],
if vowels['e']!=0:
    print ", e=",vowels['e'],
if vowels['i']!=0:
    print ", i=",vowels['i'],
if vowels['o']!=0:
    print ", o=",vowels['o'],
if vowels['u']!=0:
    print ", u=",vowels['u'],
    



