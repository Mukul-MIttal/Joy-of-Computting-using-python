# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 13:19:46 2022

@author: HP
"""

def binary_search(l,x,start,end):
    if start==end:
        if l[start]==x:
            return start
        else:
            return -1
    else:
        mid=(start+end)//2
        if(l[mid]==x):
            return mid
        elif(l[mid]<x):
            return binary_search(l, x, mid+1, end)
        else:
            return binary_search(l, x, start , mid+1)
    
    