# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 20:35:16 2016

@author: lvl
"""

s = 'kheskxfqreaaydjaytxw'
string = s[0]
counter = 0
long = 0
temp = ''

for i in range((len(s) - 1)): 
    if s[i] <= s[i + 1]:
        temp += s[i]
        counter += 1
        
        if i == len(s) - 2:
            temp += s[i + 1]
            counter += 1

            if counter > long:
                string = temp
                long = counter
                counter = 0
    elif counter > 0:
        temp += s[i]
        counter += 1
        
        if counter > long:
            string = temp
            temp = ''
            long = counter
            counter = 0
        else:
            temp = ''
            counter = 0
    else:
        counter = 0
                
print ("Longest substring in alphabetical order is: " + string)