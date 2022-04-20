# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 15:05:49 2022

@author: HP
"""
def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Please enter a positive number."))
if n<0:
    print("undefined for negative number")
else:
    print("Fibonacci number at position ",n," is ",fibonacci(n))