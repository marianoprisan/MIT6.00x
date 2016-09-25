# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 10:20:43 2016

@author: lvl
"""
# bisection search for searching an approximate square root
x = int(input("Please enter the number to compute: "))
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low) / 2.0

while abs(ans**2 - x ) >= epsilon:
    print ('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    
    if ans**2 < x:
        low = ans
    else:
        high = ans
    
    ans = (high + low) / 2.0

print ('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to the square root of ' + str(x))