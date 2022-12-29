from random import randint

#create a list of play options
l = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = l[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("Oops! You lose!", computer, "covers", player)
        else:
            print("Eyavl! You win!", player, "crushes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("Oops! You lost!", computer, "smashes", player)
        else:
            print("Yay! You win!", player, "cut", computer)
    else:
        print("Not Valid! Try Agian!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = l[randint(0,2)]
