# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:04:45 2016

@author: lvl
This program converts its input(a decimal number) to binary.
"""
num = int(input("Enter the number to be converted to binary: "))
result = ''
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

if num == 0:
    result = '0'
    
while(num > 0):
    #for each iteration we want to get the remainder of num // 2
    #and prepend to the result
    result = str(num%2) + result
    #// is integer division in python 3, / would return a float
    num = num // 2

if isNeg:
    result = '-' + result
    
print(str(num) + " converted to binary is: " + result)