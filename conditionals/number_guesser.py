# I got bored

import random

number = random.randint(1, 103)
done = 0

def asks(done, number):
    if done == 0:
        guess = int(input("Enter your guess (between 1 and 103):\n"))
        if guess > number:
            print("Lower\n")
        elif guess < number:
            print("Higher\n")
        else:
            print("You got it!")
            done = 1
        return done
    else:
        return done

while done == 0:
    done = asks(done, number)