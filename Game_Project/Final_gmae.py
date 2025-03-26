# Jared Lewis, Text Based Adventure Storyline
import time
import sys
import threading
import os
import random

#Game Functions

# Tick Tack Toe - Jared Lewis
def tic_tac_toe():
    import random

    # Dictionary that holds the board
    slot = {
        1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6',
        7: '7', 8: '8', 9: '9'
    }

    # Function that draws the board
    def draw_board():
        return (f"{slot[1]} | {slot[2]} | {slot[3]}\n"
                f"{slot[4]} | {slot[5]} | {slot[6]}\n"
                f"{slot[7]} | {slot[8]} | {slot[9]}")

    # Welcomes player and draws the board
    print("\n")
    print("Welcome to Tic-Tac-Toe!")
    print("You are X and the computer is O")
    print(draw_board())

    # Main game loop
    while True:
        # Player's turn
        while True:
            try:
                player = int(input("Enter a slot (1-9):\n"))
                if player < 1 or player > 9:
                    print("Invalid slot. Try again.")
                    continue
                if slot[player] == 'X' or slot[player] == 'O':
                    print("Slot already taken. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Enter a number between 1 and 9.")
                continue
        slot[player] = 'X'
        print(draw_board())

        # Check for a win or tie
        if (slot[1] == slot[2] == slot[3] or slot[4] == slot[5] == slot[6] or slot[7] == slot[8] == slot[9] or
            slot[1] == slot[4] == slot[7] or slot[2] == slot[5] == slot[8] or slot[3] == slot[6] == slot[9] or
            slot[1] == slot[5] == slot[9] or slot[3] == slot[5] == slot[7]):
            if (slot[1] == slot[2] == slot[3] == 'X' or slot[4] == slot[5] == slot[6] == 'X' or
                slot[7] == slot[8] == slot[9] == 'X' or slot[1] == slot[4] == slot[7] == 'X' or
                slot[2] == slot[5] == slot[8] == 'X' or slot[3] == slot[6] == slot[9] == 'X' or
                slot[1] == slot[5] == slot[9] == 'X' or slot[3] == slot[5] == slot[7] == 'X'):
                print("You win!\n")
                break
            elif (slot[1] == slot[2] == slot[3] == 'O' or slot[4] == slot[5] == slot[6] == 'O' or
                  slot[7] == slot[8] == slot[9] == 'O' or slot[1] == slot[4] == slot[7] == 'O' or
                  slot[2] == slot[5] == slot[8] == 'O' or slot[3] == slot[6] == slot[9] == 'O' or
                  slot[1] == slot[5] == slot[9] == 'O' or slot[3] == slot[5] == slot[7] == 'O'):
                print("You lost!\n")
                break

        if all(cell == 'X' or cell == 'O' for cell in slot.values()):
            print("It's a tie!")
            break

        # Computer's turn
        while True:
            computer = random.randint(1, 9)
            if slot[computer] != 'X' and slot[computer] != 'O':
                slot[computer] = 'O'
                print(draw_board())
                break

#Alan De Lara
def hangman():
    import random  
    import time  
    # word list  
    words = ["pattern", "hay", "overview", "anniversary", "flourish", "remember", "experiment","arrange", "stadium", "domestic", "demonstration", "conversation", ]  
    
    def display_hangman(wrong_attempts):  
        if wrong_attempts == 0:  
            return """  
              ------  
              |      |  
              |        
              |        
              |        
              |        
            __|_________  
            """  
        elif wrong_attempts == 1:  
            return """  
              ------  
              |      |  
              |      O  
              |        
              |        
              |        
            __|_________  
            """  
        elif wrong_attempts == 2:  
            return """  
              ------  
              |      |  
              |      O  
              |      |  
              |        
              |        
            __|_________  
            """  
        elif wrong_attempts == 3:  
            return """  
              ------  
              |      |  
              |      O  
              |     /|
              |        
              |        
            __|_________
            """  
        elif wrong_attempts == 4:  
            return """  
              ------  
              |      |  
              |      O  
              |     /|\\
              |      |  
              |        
            __|_________ 
            """  
        elif wrong_attempts == 5:  
            return """  
              ------  
              |      |  
              |      O  
              |     /|\\
              |      |  
              |     / \\
            __|_________ 
            """  


        return [wrong_attempts]  
    
    def check_guess(letter, chosen_word, guessed_letters):  
        if letter in chosen_word:  
            guessed_letters.append(letter)  
            return True  
        else:  
            return False  
    
    # Main game loop  
    while True:  
        guessed_letters = []  # Reset guessed letters  
        wrong_attempts = 0    # Reset wrong attempts  
        max_attempts = 6      # max attempts  
        chosen_word = random.choice(words)  # Choose a new word  
    
        while wrong_attempts < max_attempts:  # Inner loop for guessing  
            print(display_hangman(wrong_attempts))  # Display hangman  
            display = ''.join(letter if letter in guessed_letters else '_' for letter in chosen_word)  
            print(display)  # Show the current state of the word  
    
            letter = input("Guess a letter: ")  
    
            if len(letter) == 1 and letter.isalpha():  # Validate input  
                if letter in guessed_letters:  
                    print("You've already guessed that letter.")  
                else:  
                    if check_guess(letter, chosen_word, guessed_letters):  
                        print("Good guess!")  
                    else:  
                        wrong_attempts += 1  
                        print("Wrong guess!")  
    
            if set(chosen_word).issubset(set(guessed_letters)):  # Win condition  
                print("Congratulations! You've guessed the word:", chosen_word)  
                break  
            
        if wrong_attempts == max_attempts:  # Loss condition  
            print("Game over! The word was:", chosen_word)  
    
        # ask if they want to play again  
        play_again = input("Do you want to play again? (yes/no) ")  
        if play_again.lower() != "yes":  
            break  

#Anthony Petersen
def memory():
    import time
    import os
    import random
    delay = 0.035
    ANuser_input = "nothing"
    ANinstructions = "This is a memory game that will flash the numbers and you have to repeat them.\n" \
    "Press enter to begin"
    ANinstructions2 = "Please enter your answer, and remember to add spaces in between each number: \n"
    def start_game():
        ANmemory_1 = random.randint(1,9)
        ANmemory_2 = random.randint(1,9)
        ANmemory_3 = random.randint(1,9)
        ANframes = [  
        """  
        [ x ] [ x ]
        [ x ] [ x ]  
        [ x ] [ x ]""",  
    
        f"""  
        [ {ANmemory_2} ] [ {ANmemory_3} ]   
        [ {ANmemory_3} ] [ {ANmemory_1} ]  
        [ {ANmemory_1} ] [ {ANmemory_2} ]""",  
    
        """  
        [ x ] [ x ]    
        [ x ] [ x ]    
        [ x ] [ x ]""",  
        ]  

        for frame in ANframes:  
            print(frame)  
            time.sleep(1)  # Pause for a moment to show the frame
            os.system("cls" if os.name == "nt" else "clear")  # Clear the screen
        return [ANmemory_2, ANmemory_3, ANmemory_3, ANmemory_1, ANmemory_1, ANmemory_2]
    def check_guess(ANuser_input, ANcorrect_guess):
        if ANuser_input == ANcorrect_guess:
            print("Well done!")
            return("Well done!")
        else:
            print("Try again!")

    for char in ANinstructions:
        print(char, end="")
        time.sleep(delay)
    for char in ANinstructions2:
        print(char, end="")
        time.sleep(delay)
    if ANinstructions2 == "":
        while True:  # Loop until the user guesses correctly
            ANcorrect_sequence = start_game()  # Display the frames and get the correct sequence
            ANuser_input = input("Please enter your answer, and remember to add spaces in between each number: ").split()  

            try:  
                ANuser_input = [int(num) for num in ANuser_input]  # Convert input to integers
                if check_guess(ANuser_input, ANcorrect_sequence) == "Well done!":  # Check if the guess is correct
                    break  # Exit the loop if correct
            except ValueError:  
                print("Please enter numbers only!")  #If someone enters letters


# Where the story starts
# Fancy text functions
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def flashing_text(stop_event):
    sys.stdout.write("\033[?25l")  # Hide the cursor
    sys.stdout.flush()
    while not stop_event.is_set():
        sys.stdout.write("\rPress ENTER to continue   ")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\r                                ")  # Ensure the line is cleared properly
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\033[?25h")  # Show the cursor again
    sys.stdout.flush()

# sets the delay between each character printed
delay = 0.01

# The Introduction
message1 = "Welcome user...\n"\
"The game you are about to play is a text based adventure game.\n"\
"This game will test your skills through a series of minigames.\n"\
"This game includes certain experiances that may cause anxiety or fear.\n"\
"This game is meant to possibly raise the heart rate\n"\
"and levels of adrenaline.\n"\
"Please be aware of this before you continue.\n"\
"\n"\
"May I welcome you to...\n"\
"\n"\
"THE UNDERWORLD\n"\
"created by:\n"\
"Alan De Lara\n"\
"Anthony Petersen\n"\
"Douglas London\n"\
"Jared Lewis\n"\
"\n"

# function to make text fancy.
for char in message1:
    print(char, end="", flush=True)
    time.sleep(delay)

stop_event = threading.Event()
thread = threading.Thread(target=flashing_text, args=(stop_event,))
thread.start()

input()
stop_event.set()
thread.join()

clear_terminal()  # Clear the terminal again before the next message

# Itroduction to Backstory
message2 = "Chapter 1:\n"\
"A NORMAL CAR TRIP\n"\
"\n"\
"Press Enter to Continue\n"

# function to print the message slowly.
for char in message2:
    print(char, end="")
    time.sleep(delay)

# waits for the user to press enter
while True:
    if input() == "":
        break
    else:
        continue

# Backstory
message3 = "You are a retired militry agent who served with the Navy Seals.\n"\
"It has been 5 years since your retirement and you currently live in a little nieghborhood in Colorado.\n"\
"So far, your life has seemed pretty normal.\n"\
"However, one day you were driving home from a car trip when everything darkened.\n"\
"You wake up in a dark room with no windows and no doors.\n"\
"The only thing you remember is a terrifying feeling of dread that you seemed to feel, just hours before.\n"\
"Suddenly you hear a distant\n\n"


# function to print the message slowly.
for char in message3:
    print(char, end="")
    time.sleep(delay)

# dramatic end of Backstory
time.sleep(1)
print("Scream...\n")
time.sleep(1)
print("Press Enter to Continue")


# waits for the user to press enter
while True:
    if input() == "":
        break
    else:
        continue

# Introduction to Chapter 2
message4 = "Chapter 2:\n"\
"THE DARK ROOM\n"\
"\n"\
"Press Enter to Continue\n"

# function to print the message slowly.
for char in message4:
    print(char, end="")
    time.sleep(delay)

# waits for the user to press enter
while True:
    if input() == "":
        break
    else:
        continue

# Chapter 2
message5 = "As you feel around the room, you catch hold of a door handle.\n"\
"Press Enter to Open Door\n"\
"As the door slowly creaks open, you peer out into a long hallway.\n"\
"The hallway is dimly lit and has wallpaper that looks as though it is from an old orphanage.\n"\
"You walk down the hall and find a door with the words “too late” scribbled on it.\n"\
"\n"\
"Press Enter to Open Door\n"

# function to print the message slowly.
for char in message5:
    print(char, end="")
    time.sleep(delay)

# waits for the user to press enter
while True:
    if input() == "":
        break
    else:
        continue

#Chapter 2
message6 = "The door scrapes loudly across the floor.\n"\
"You find yourself in a small room.\n"\
"However, as you step inside, a metal sheet slides down in front of the door you just came from.\n"\
"Right next to the metal sheet, you notice a keypad.\n"\
"You try guessing the code on the keypad, but to no avail, you need a 3-digit code.\n"\
"You are trapped in the room!\n"\
"On the far wall, you see a map:\n"

# function to print the message slowly.
for char in message6:
    print(char, end="")
    time.sleep(delay)

# variable to store the map
map = " __________________________________\n"\
"|            Tic-Tac-Toe           |\n"\
"|               |   |              |\n"\
"|            ___|   |___           |\n"\
"|        ___| Map       |___       |\n"\
"| Hangman___             ___Memory |\n"\
"|           |___     ___|          |\n"\
"|            /  |___|              |\n"\
"|     Keypad    |   |              |\n"\
"|                Exit              |\n"\
"|__________________________________|\n"

#function for game selection
def game_selection():
    # prints the map
    print(map)

    # Game Selection
    message7 = "You are located where it says 'Map'.\n"\
    "Where do you choose to go?\n"\
    "1. Tic-Tac-Toe\n"\
    "2. Hangman\n"\
    "3. Memory\n"\
    "4. Keypad\n"\
    "Enter the number you choose:\n"

    # function to print the message slowly.
    for char in message7:
        print(char, end="")
        time.sleep(delay)

    # Stupid Proofs input
    while True:
        try:
            user_input = int(input())
            if user_input in [1, 2, 3, 4]:
                break
            else:
                print("Invalid Input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 4.")


    # Collects the user's input
    if user_input == 1:
        tic_tac_toe()
    elif user_input == 2:
        hangman()
    elif user_input == 3:
        memory()
    elif user_input == 4:
        print("Please enter the 3-digit code, enter q to return to map")
        code = input()
        if code == "q":
            game_selection()
        elif code != "826":
            print("Incorrect code. Please try again.")
        elif code == "826":
            False
# Calls The game_selection Funtion
game_selection()

