# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 12:08:42 2016

@author: lvl
"""
def factorial(n):
    """
    Returns the factorial of n
    Uses recursion
    """
    if n == 1:
        return 1
    else:
        return(n * factorial(n - 1))
        
n = int(input("Enter the factorial you want me to compute: "))
print(factorial(n))