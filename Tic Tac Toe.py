# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 10:56:00 2022

@author: HP
"""

import numpy
board=numpy.array([["-","-","-"],["-","-","-"],["-","-","-"]])
p1s="X"
p2s="O"
def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_digonal(symbol)
    
def check_rows(symbol):
    for r in range (3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol, " Won")
            return True
    return False
def check_digonal(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]== symbol:
        print (symbol, " Won")
        return True
    if board[0][0]== board[1][1] and board[1][1]==board[2][2] and board[1][1]== symbol:
        print (symbol, " Won")
        return True
    return False
def check_cols(symbol):
    for c in range (3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol, " Won")
            return True
    return False
def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("Enter your row position -1 or 2 or 3 : "))
        row=row-1
        col=int(input("Enter coloumn -1 or 2 or 3 :"))
        col=col-1
        if(row>=0 and row<=2 and col>=0 and col<=2 and board[row][col]=="-"):
            break
        else:
            print("Invalid input. Please enter again.")
    board[row][col]=symbol
    
def play():
    for turn in range(9):
        if(turn%2==0):
            print("X turn")
            place(p1s)
            if won(p1s):
                print("Player x wins.")
                break
        else:
            print("O turn")
            place(p2s)
            if won(p2s):
                print("Player o wins")
                break
    if not(won(p1s)) and not(won(p2s)):
        print("Draw")
    
play()