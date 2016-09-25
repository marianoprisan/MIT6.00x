# -*- coding: utf-8 -*-
s = 'azcbobobegghakl'
numVowels = 0

for letter in s:
    if letter in 'aeiou':
        numVowels += 1

print ("Number of vowels: " + str(numVowels))