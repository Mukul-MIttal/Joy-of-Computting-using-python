import random
def Choose():
    words=["python", "jumble", "easy", "difficult", "answer",  "xylophone"]
    ch=random.choice(words)
    return ch
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
def thank(p1,p2,ps1,ps2):
    if ps1>ps2:
        print(p1," Win from ",p2)
    else:
        if ps1==ps2:
            print("Game is Draw")
        else:
            print(p2," Win from ",p1)
def play():
    p1Name=input("Please enter player 1 name.")
    p2Name=input("Please enter player 2 name.")
    pp1=0
    pp2=0
    turn=0
    while(1):
        #computer task
        picked_word=Choose()
        qn=jumble(picked_word)
        if(turn%2==0):
            print(p1Name,"Your jumble word is",qn)
            ans=input()
            if(ans==picked_word):
                pp1=pp1+1
                print("Right answer")
            else:
                print("Batter luck nex time. I thoughr :",picked_word)
            print("Your score is ",pp1)
            
        else:
            print(p2Name,"Your jumble word is",qn)
            ans=input()
            if(ans==picked_word):
                pp2=pp2+1
                print("Right answer")
            else:
                print("Batter luck nex time. I thoughr :",picked_word)
            print("Your score is ",pp2)
            c=input("press 1 to continue and 0 to exit")
            if c=="0":
                thank(p1Name,p2Name,pp1,pp2)
                break;
        turn=turn+1
