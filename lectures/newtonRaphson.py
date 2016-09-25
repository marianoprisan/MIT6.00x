# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:55:25 2016

@author: lvl
This program uses the Newton Raphson algorithm to approximate a square root
This algorithm improves performance a lot
"""
num = int(input("Please enter a number: "))
epsilon = 0.01
guess = num / 2.0
numGuesses = 0

while abs(guess*guess - num) >= epsilon:
    numGuesses += 1
    
    guess = guess - (((guess**2) - num) / (2 * guess))

print("numGuesses = " + str(numGuesses))
print("Square root of " + str(num) + " is about " + str(guess))