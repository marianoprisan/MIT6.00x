# -*- coding: utf-8 -*-
x = int(input("Please enter an integer: "))
ans = 0

while ans**3 < abs(x):
    ans += 1

if ans**3 != abs(x):
    print(str(x) + " is not a perfect cube!")
else:
    if x < 0:
        ans = - ans
    print("The cube root of " + str(x) + " is " + str(ans))