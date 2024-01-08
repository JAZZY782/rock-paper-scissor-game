import random
repeat="yes"
while repeat=="yes":
    rps=["rock", "paper", "scissor"]
    p1=input("Please select rock, paper or scissor:")
    p2=random.choice(rps)
    print("Player 1 =", p1)
    print("Player 2 =", p2)
    if p1=="rock":
        if p2=="rock":
            print("it is a tie")
        elif p2=="scissor":
            print("congrats player 1 is a winner")
        else:
            print("dmn...player 2 is a winner")
    if p1=="paper":
        if p2=="paper":
            print("It is a tie")
        elif p2=="rock":
            print("congrats player 1 is a winner")
        else:
            print("dmn...player 2 is a winner")
    if p1=="scissor":
        if p2=="scissor":
            print("It is a tie")
        elif p2=="paper":
            print("Congrats player 1 is a winner")
        else:
            print("dmn...player 2 is a winner")
    repeat=input("do you want to continue yes or no?:")
print("Good bye")
    
