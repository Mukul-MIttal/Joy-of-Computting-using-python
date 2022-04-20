# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:47:48 2022

@author: HP
"""

def binary_search(a,x):
    first_pos=0
    last_pos=len(a)-1
    flag=0
    count=0
    while(first_pos<=last_pos and flag==0):
        count+=1
        mid=(first_pos+last_pos)//2
        if(x==a[mid]):
            flag=1
            print("The element is present at position: ",mid)
            print("The number of itterations are: ",count)
            return
        else:
            if(x<a[mid]):
                last_pos=mid-1
            else:
                first_pos=mid+1
    print("The number is not present")
a=[]
for i in range(1,5001):
    a.append(i)
binary_search(a, 100)