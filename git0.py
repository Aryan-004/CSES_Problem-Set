#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 12:58:15 2022

@author: aryan
"""

def weird_algo(n):
    while n>1:
        if n%2==0:
            n=n/2
            n=int(n)
            print(n)
        else:
            n=(n*3)+1
            print(n)
n=int(input())
result=weird_algo(n)
print(result,end=' ')

print("hello git")