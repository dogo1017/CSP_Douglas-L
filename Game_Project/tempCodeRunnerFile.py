
# waits for the user to press enter - Douglas
stop_event = threading.Event()
thread = threading.Thread(target=flashing_text, args=(stop_event,))
thread.start()


input()
stop_event.set()
thread.join()
clear_terminal()


# Introduction to Chapter 2 - Jared
message4 = "Chapter 2:\n"\
"THE DARK ROOM\n"\
"\n"\


# function to print the message slowly.
for char in message4:
    print(char, end="", flush=True)
    time.sleep(delay)


# waits for the user to press enter - Douglas
stop_event = threading.Event()
thread = threading.Thread(target=flashing_text, args=(stop_event,))
thread.start()


input()
stop_event.set()
thread.join()
clear_terminal()


# Chapter 2 - Jared
message5 = "As you feel around the room, you catch hold of a door handle.\n"\
"\n"\
"Press Enter to Open Door\n"\


# function to print the message slowly.
for char in message5:
    print(char, end="")
    time.sleep(delay)


# waits for the user to press enter
while True:
    if input() == "":
        break
    else:
        print("Only Press ENTER")
clear_terminal()


message6 = "As the door slowly creaks open, you peer out into a long hallway.\n"\
"The hallway is dimly lit and has wallpaper that looks as though it is from an old orphanage.\n"\
"You walk down the hall and find a door with the words “too late” scribbled on it.\n"\
"\n"\
"Press Enter to Open Door\n"


# function to print the message slowly.
for char in message6:
    print(char, end="")
    time.sleep(delay)


# waits for the user to press enter
while True:
    if input() == "":
        break
    else:
        print("Only Press ENTER")
clear_terminal()



#Chapter 2
message7 = "The door scrapes loudly across the floor,\n"\
"and you find yourself in a small room.\n"\
"However, as you step inside, a metal sheet slides down in front of the door you just came from.\n"\
"Right next to the metal sheet, you notice a keypad.\n"\
"You try guessing the code on the keypad, but to no avail, you need a 3-digit code.\n"\
"You are trapped in the room!\n"\
"On the far wall, you see a map:\n"


# function to print the message slowly.
for char in message7:
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






def keypad():
    global code  # Ensure we are using the generated code
    print("Please enter the 3-digit code, enter q to return to map")
    input_code = input()

    if input_code == "q":
        clear_terminal()
        game_selection()
    elif input_code == code:
        print("Correct code!")
        clear_terminal()  # Clear the screen and move to the next stage
        message = "The door opens, and you find a new room awaiting you.\n"
        for char in message:
            print(char, end="")
            time.sleep(delay)
        # Continue with next stage of the game, for example:
        # proceed_to_next_stage() or next_chapter()
        return True
    else:
        print("Incorrect code. Try again.")
        return keypad()  # Re-call function to retry


    if input_code == "q":
        clear_terminal()
        game_selection()
    elif input_code == code:
        print("Correct code!")  # Give feedback
        return True  # This can be used to trigger the next part of the game
    else:
        print("Incorrect code. Try again.")
        return keypad()  # Re-call function to retry



#function for game selection
def game_selection():
    # prints the map
    print(map)


    # Game Selection
    message8 = "You are located where it says 'Map'.\n"\
    "Where do you choose to go?\n"\
    "HINT: The selections may have an. answer to the code.\n"\
    "1. Tic-Tac-Toe\n"\
    "2. Hangman\n"\
    "3. Memory\n"\
    "4. Keypad\n"\
    "Enter the number you choose:\n"


    # function to print the message slowly.
    for char in message8:
        print(char, end="")
        time.sleep(delay)

