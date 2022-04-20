# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:20:55 2022

@author: HP
"""
def linear_search(n,x):
    element=[]
    for i in range(1,n):
        element.append(i)
    flag=0
    count=0
    for i in element:
        count+=1
        if(i==x):
            print("yes!! I found my number at position "+str(i))
            flag=1
            break
    if(flag==0):
        print("Number is not found")
