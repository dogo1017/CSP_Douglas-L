# Jared Lewis, Text Based Adventure Storyline
import time


# sets the delay between each character printed
delay = 0.035

# The Introduction
message1 = "Welcome user...\n"\
"The game you are about to play is a text based adventure game.\n"\
"This game will test your skills through a series of minigames.\n"\
"May I welcome you to...\n"\
"\n"\
"THE UNDERWORLD\n"\
"created by:\n"\
"Alan De Lara\n"\
"Anthony Petersen\n"\
"Douglas London\n"\
"Jared Lewis\n"\
"\n"\
"Press Enter to continue\n"

# function to print the message slowly.
for char in message1:
    print(char, end="")
    time.sleep(delay)

# waits for the user to press enter
while True:
    if input() == "":
        break
    else:
        continue


# Backstory
message2 = "You are a retired militry agent who served with the Navy Seals.\n"\
"It has been 5 years since your retirement and you currently live in a little nieghborhood in Colorado.\n"\
"So far, your life has seemed pretty normal.\n"\
"However, one day you were driving home from a car trip when everything darkened.\n"\
"You wake up in a dark room with no windows and no doors.\n"\
"The only thing you remember is a terrifying feeling of dread that you seemed to feel, just hours before.\n"\
"Suddenly you hear a distant\n\n"


# function to print the message slowly.
for char in message2:
    print(char, end="")
    time.sleep(delay)

# dramatic end of Backstory
time.sleep(1)
print("Scream...\n")
time.sleep(1)
print("Press Enter to continue")


# waits for the user to press enter
while True:
    if input() == "":
        break
    else:
        continue

# The end for now
print("THE DARK ROOM\n")