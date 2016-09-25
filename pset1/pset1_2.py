# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 20:33:57 2016

@author: lvl
"""

s = 'azcbobobegghakl'
counter = 0

for i in range(len(s) - 2):
    if s[i] == "b":
        if s[i + 1] == "o":
            if s[i + 2] == "b":
                counter += 1
    
print ("Number of times bob occurs is: " + str(counter))