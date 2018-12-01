#Title: Assignment2---Question27
#Author:Merin
#Version:1
#DateTime:28/11/2018 5:00pm
#Summary: Write a program to check given string is Palindrome or not.That is reverse the given string and check whether it is same as original string, if so then it is palindrome.
#         Example: String = "malayalam"  reverse string = "malayalam" hence given string is palindrome. Use built functions to check given string is palindrome or not.


#User Input
string=raw_input('Enter string to be checked as palindrome or not:')

#Finding reverse of string
reverse=string[::-1]

#Comparing the strings & printing the result
if cmp(string,reverse)==0:
    print "%s is a palindrome"%string
else:
    print "%s is not a palindrome"%string



