#Title: Assignment2---Question22
#Author:Merin
#Version:1
#DateTime:27/11/2018 3:30pm
#Summary: Read the value x and y from the user and apply all trigonometric functions on these numbers. 


#import MATH module
import math

#User Input
x=input("Enter a value for 'x'(between -1 & 1):")
y=input("Enter a value for 'y':")

#Trignometrical functions
print "Inverse cosine of %f is "%x,math.acos(x)
print "Inverse hyperbolic cosine of %d is "%y,math.acosh(y)
print "Inverse sine of %f is "%x,math.asin(x)
print "Inverse hyperbolic sine of %d is "%y,math.asinh(y)
print "Inverse tangent of %d is "%y,math.atan(y)
print "Inverse hyperbolic tangent of %f is "%x,math.atanh(x)
print "Inverse hyperbolic tangent(atan2) of %f & %f is "%(x,y),math.atan2(x,y)
print "Tangent of %d is "%y,math.tan(y)
print "Cosine of %d is "%y,math.cos(y)
print "Sine of %d is "%y,math.sin(y)
print "Hyperbolic Tangent of %d is "%y,math.tanh(y)
print "Hyperbolic Cosine of %d is "%y,math.cosh(y)
print "Hyperbolic Sine of %d is "%y,math.sinh(y)








