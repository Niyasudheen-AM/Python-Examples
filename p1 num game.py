# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 11:45:39 2026

@author: niyas
"""
import random
lower=int(input("Lower Range Number"))
higher=int(input("Higher Range Number"))
target=random.randint(lower,higher)
guess=int(input("enter a number"))
attempt=1
while True:
    if guess==target:
        print("congratulations you got the answer in",attempt,"attempts")
        break
    else:
        if guess<target:
            print('Try again your number is low')
        else:
            print('Try again your number is high')
        attempt+=1
        guess=int(input("enter a number"))
        
        
