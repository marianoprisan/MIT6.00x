# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:37:38 2016

@author: lvl
"""
def isPalindrome(s):
    
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            #recursively comparing the first and last characters
            #dividing the problem with each step
            return s[0] == s[-1] and isPal(s[1:-1])
    
    return isPal(toChars(s))