import string
import random

def Dobble():
    symbols=[]
    symbols=list(string.ascii_letters)
    card1=[0]*5
    card2=[0]*5
    pos1=random.randint(0,4)
    pos2=random.randint(0,4)
    samesymbol=random.choice(symbols)
    symbols.remove(samesymbol)
    if(pos1==pos2):
        card2[pos1]=samesymbol
        card1[pos1]=samesymbol
    else:
        card1[pos1]=samesymbol
        card2[pos2]=samesymbol
        card1[pos2]=random.choice(symbols)
        symbols.remove(card1[pos2])
        card2[pos1]=random.choice(symbols)
        symbols.remove(card2[pos1])
    for i in range(5):
        if(card1[i]==0):
            card1[i]=random.choice(symbols)
            symbols.remove(card1[i])
        if(card2[i]==0):
            card2[i]=random.choice(symbols)
            symbols.remove(card2[i])
    print(card1)
    print(card2)
    ch=input("Spot the smilar symbol")
    if(ch==samesymbol):
        print("Right")
    else:
        print("Wrong")