from PIL import Image
import random
end=100
def show_board():
    img=Image.open("slb.jpg")
    img.show()
Ladder={8:26,21:82,43:77,50:91,54:93,62:96,66:87,80:100}
Snake={44:22,46:5,48:9,52:11,55:7,59:17,64:36,69:33,73:1,83:19,92:51,95:24,98:28}
def check_ladder(points):
    if points in Ladder:
        print ("Ladder")
        return Ladder[points]
    else:
        return points
def check_snake(points):
    if points in Snake:
        print ("Snake")
        return Snake[points]
    else:
        return points
def reached_end(points):
    if(points==end):
        return True
    else:
        return False
def play():
    # Take input for both player names
    p1_name=input("Player one Enter your Name:")
    p2_Name=input("Player two Enter Your Name:")
    #initial poins of players
    pp1=0
    pp2=0
    turn=0
    while(1):
        if(turn%2==0):
            #player one plays
            print(p1_name," Your turn")
            c=input("Press 1 to continue , 0 to quit: ")
            if c==0:
                print(p1_name, " Score ", pp1)
                print(p2_Name, " Score ", pp2)
                print("Game is Quit, Thanks for playing.")
                break
            # to generate a rendom number1-6
            dice=random.randint(1,6)
            print("Dice Showed: ",dice)
            pp1+=dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            if pp1>end:
                pp1=end
            print (p1_name, "Your score: ", pp1)
            if(reached_end(pp1)):
                print(p1_name ," won the game")
                break
        else:
            #player two plays
            print(p2_Name," Your turn")
            c=input("Press 1 to continue , 0 to quit: ")
            if c==0:
                print(p1_name, " Score ", pp1)
                print(p2_Name, " Score ", pp2)
                print("Game is Quit, Thanks for playing.")
                break
            # to generate a rendom number1-6
            dice=random.randint(1,6)
            print("Dice Showed: ",dice)
            pp2+=dice
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            if pp2>end:
                pp2=end
            print (p2_Name, " Your score: ", pp2)
            if(reached_end(pp2)):
                print(p2_Name ," won the game")
                break
        turn=turn+1

show_board()
play()
