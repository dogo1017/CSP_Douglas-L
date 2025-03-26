import time
import sys
import threading
import os

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

delay = 0.035

clear_terminal()  # Clear the terminal here

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
"\n"

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

message2 = "You are a retired military agent who served with the Navy Seals.\n"\
"It has been 5 years since your retirement and you currently live in a little neighborhood in Colorado.\n"\
"So far, your life has seemed pretty normal.\n"\
"However, one day you were driving home from a car trip when everything darkened.\n"\
"You wake up in a dark room with no windows and no doors.\n"\
"The only thing you remember is a terrifying feeling of dread that you seemed to feel, just hours before.\n"\
"Suddenly you hear a distant\n\n"

for char in message2:
    print(char, end="", flush=True)
    time.sleep(delay)

time.sleep(1)
print("Scream...\n")
time.sleep(1)

stop_event = threading.Event()
thread = threading.Thread(target=flashing_text, args=(stop_event,))
thread.start()

input()
stop_event.set()
thread.join()

clear_terminal()  # Clear the terminal again before printing the final message

print("THE DARK ROOM\n")

#k