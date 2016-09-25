# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 17:08:05 2016

@author: lvl
"""

import math

def polysum(n, s):
    """
    n = number of sides, s = side length, both positive integers
    this function returns the sum of the area and square perimeter of the
    polygon described by n and s
    """
    area = 0
    
    #avoiding division by zero
    if n != 0:        
        area = (0.25 * n * (s**2)) / math.tan(math.pi / n)
    perimeter = n * s
    
    return (round(area + perimeter**2, 4))