# i was bored

import random
number = random.randint(1,103)



done = 0
guess = 0


def asks(done, number, guess):
    if (done == 0):
        guess = int(input("number:\n"))
        if (guess > number):
            print("Higher\n")
        elif (guess < number):
            print("lower")
        else:
            print("You got It!")
            exit()
    else: 
        exit()

while(done == 0):
    asks(0, number, guess)



        
    




    