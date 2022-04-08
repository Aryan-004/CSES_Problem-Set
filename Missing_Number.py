#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 06:02:51 2022

@author: aryan
"""
value=int(input())
result=(value*(value+1))//2 - sum([int(i) for i in input().split()])
print(result)


#TLE
"""
value=int(input())
list=[int(i) for i in input().split()]
for i in range (1,value+1):
    if i in list:
        None
    else:
        print(i)
        break
"""