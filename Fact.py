# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 12:27:41 2022

@author: HP
"""

def fact(n):
    if n<=1:
        return 1
    else:
        return n * fact(n-1)
    