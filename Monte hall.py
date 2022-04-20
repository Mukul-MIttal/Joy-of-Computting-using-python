import random as Rd
doors=[0]*3
goatdoors=[0]*3
swap=0 # no of swap wins
dont_swap=0 # no of dont swap wins
x= Rd.randint(0,2) # x th doo0r will comprise of of aword
doors[x]="BMW"
j=10
for j in range(j):
    for i in range(0,3):
        if(i==x):
            continue
        else:
            doors[i]="Goat"
            goatdoors.append(i)
    choice= int(input("Enter your choice"))
    door_open=Rd.choice(goatdoors)
    while(door_open==choice):
        door_open=Rd.choice(goatdoors)
    ch=input("Do you want to swap? y/n")
    if(ch=="y"):
        if(doors[choice]=="Goat"):
            print("Player wins")
            swap=swap+1
        else:
            print("Player lost")
    else:
        if(doors[choice]!="Goat"):
            print("Player wins")
            dont_swap=dont_swap+1
        else:
            print("Player lost")
    print("Swap wins ", swap)
    print("Dont swap wins ", dont_swap)