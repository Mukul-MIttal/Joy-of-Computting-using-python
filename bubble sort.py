# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:18:53 2022

@author: HP
"""

def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                tmp=a[j]
                a[j]=a[j+1]
                a[j+1]=tmp
    print(a)
bubble([9,7,8,6,4,5,3,1,2])
            