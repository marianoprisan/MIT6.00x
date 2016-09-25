# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:15:54 2016

@author: lvl
"""

def fib(x):
    """
    assumes x an int >= 0
    returns Fibonacci of x
    """
    
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x -1) + fib(x - 2)