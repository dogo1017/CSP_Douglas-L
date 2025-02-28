# Douglas London, Rock paper scisors python

import random
bot = random.randint(1,3)

player = input("rock paper or scissors:\n")

if (player == "rock"):
    if (bot == 1):
        print("you tied")
    elif (bot == 2):
        print("Paper!\n You lost")
    elif (bot == 3):
        print("Paper! \n You won")
elif (player == "paper"):
    if (bot == 2):
        print("you tied")
    elif (bot == 3):
        print("scissors!\n You lost")
    elif (bot == 1):
        print("rock! \n You won")
elif (player == "scissors"):
    if (bot == 3):
        print("you tied")
    elif (bot == 1):
        print("rock!\n You lost")
    elif (bot == 2):
        print("paper! \n You won")
