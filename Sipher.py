# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 13:30:58 2022

@author: HP
"""

import string
dict={}
data=""
file=open("New.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
    
with open("Text.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print("end of file")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)
        print (str(data))
file.close()