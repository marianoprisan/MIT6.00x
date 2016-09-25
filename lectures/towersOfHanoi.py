# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:47:36 2016

@author: lvl
Towers of Hanoi
Prints out a list of move we need to make in order to move a stack of size n
"""
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))
    
def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n - 1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n - 1, spare, to, fr)

print(Towers(4, 'P1', 'P2', 'P3'))