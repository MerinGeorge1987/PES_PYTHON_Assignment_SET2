#Title: Assignment2---Question21
#Author:Merin
#Version:1
#DateTime:27/11/2018 11:00am
#Summary: Using the built-in functions on Numbers perform following operations
#         a) Round of the given floating point number. Example:  n=0.543 then round it next decimal number,
#            i.e n=1.0 Use round() function
#         b) Find out the square root of a given number. (Use sqrt(x) function)
#         c) Generate random number between 0, and 1 ( use  random() function)
#         d) Generate random number between 10 and  500. (Use uniform() function)
#         e) Explore all Math and Random module functions  on a given number/ List.



#a) Round of the given floating point number. Example:  n=0.543 then round it next decimal number i.e n=1.0 Use round() function
n=input("Enter a floating point number:")
print "%f is rounded to"%n,round(n)

#b) Find out the square root of a given number. (Use sqrt(x) function)
import math
n=input("Enter a number:")
print "Square root of %d is "%n,math.sqrt(n)

#c) Generate random number between 0, and 1 ( use  random() function)
import random
print "Random number between 0 & 1:",random.random()

#d) Generate random number between 10 and  500. (Use uniform() function)
print "Random number between 10 & 500:",random.uniform(10,500)

#e) Explore all Math and Random module functions  on a given number/ List
#Math module
n=23
#Trignometrical functions
print "Inverse cosine of 0.5 is ",math.acos(0.5)
print "Inverse hyperbolic cosine of %d is "%n,math.acosh(n)
print "Inverse sine of 0.5 is ",math.asin(0.5)
print "Inverse hyperbolic sine of %d is "%n,math.asinh(n)
print "Inverse tangent of %d is "%n,math.atan(n)
print "Inverse hyperbolic tangent of 0.5 is ",math.atanh(0.5)
print "Inverse hyperbolic tangent of 0.1 & 0.2 is ",math.atan2(0.1,0.2)
print "Tangent of %d is "%n,math.tan(n)
print "Cosine of %d is "%n,math.cos(n)
print "Sine of %d is "%n,math.sin(n)
print "Hyperbolic Tangent of %d is "%n,math.tanh(n)
print "Hyperbolic Cosine of %d is "%n,math.cosh(n)
print "Hyperbolic Sine of %d is "%n,math.sinh(n)

n=-5.432
print "Floor value of %f is "%n,math.floor(n)
print "Ceilng value of %f is "%n,math.ceil(n)
print "Absolute value of %f is "%n,math.fabs(n)

n = 0.0002
print('e^%f is :'%n, math.exp(n)-1)
print('e^%f is :'%n, math.expm1(n))
print('log(fabs(%f), base) is :'%n, math.log(math.fabs(n), 10))

print "Square root of 99",math.sqrt(99)
print "Pi =",math.pi
print "Factorial of 4:",math.factorial(4),math.pow(4,2)
print "4^2 is",math.pow(4,2)

#Random Module
print "Integer random number between 10 & 20",random.randint(10,20)
print "Random number between 0 & 1",random.random()
list1 = [4,324,"python","&&",2123]
print "Random choice out of ",list1,"is",random.choice(list1)
print "Randomly shuffled list of",list1,"is",random.shuffle(list1)






