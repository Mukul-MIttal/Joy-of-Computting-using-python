# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:21:28 2022

@author: HP
"""

import random


def lootery(account):
    bet= int(input("Your bet from 1 to 10."))
    lucky_draw=random.randint(1,10)
    print(lucky_draw)
    if bet==lucky_draw:
        account=account+900-100
    else:
        account=account-100
    print(account)
    return account
account=0
for i in range(7):
    account=lootery(account)
