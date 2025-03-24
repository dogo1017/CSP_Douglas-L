# Jared Lewis, Tick Tack Toe Python
import random


# Dictionary that holds the board
slot = {
    1: '1', 2: '2', 3: '3',
    4: '4', 5: '5', 6: '6',
    7: '7', 8: '8', 9: '9'
}


# Function that draws the board
def draw_board():
    return (f"{slot [1]} | {slot [2]} | {slot [3]}\n"
            f"{slot [4]} | {slot [5]} | {slot [6]}\n"
            f"{slot [7]} | {slot [8]} | {slot [9]}")


# Welcomes plawer and draws the board
print("\n")
print("Welcome to Tick Tack Toe!")
print("Your are X and the computer is O")
print(draw_board())


# Collects player input and stupid proofs answers
while True:
    try:
        player = int(input("Enter a slot (1-9):\n"))
        if player < 1 or player > 9:
            print("Invalid slot. Try again.")
            continue
        if slot[player] == 'X' or slot[player] == 'O':
            print("Slot already taken. Try again.")
            continue
    except ValueError:
        print("Invalid input. Enter a number between 1 and 9.")
        continue
    slot[player] = 'X'
    print("\n")


# Computer's turn
    while True:
        computer = random.randint(1, 9)
        if slot[computer] != 'X' and slot[computer] != 'O':
            slot[computer] = 'O'
            print(draw_board())
            break

# Checks for who wins
# Sorry if this is long, I couldn't figure out how to condense it
    if (slot[1] == slot[2] == slot[3] or slot[4] == slot[5] == slot[6] or slot[7] == slot[8] == slot[9] or
        slot[1] == slot[4] == slot[7] or slot[2] == slot[5] == slot[8] or slot[3] == slot[6] == slot[9] or
        slot[1] == slot[5] == slot[9] or slot[3] == slot[5] == slot[7]):
        # Check if the player won
        if (slot[1] == slot[2] == slot[3] == 'X' or slot[4] == slot[5] == slot[6] == 'X' or
            slot[7] == slot[8] == slot[9] == 'X' or slot[1] == slot[4] == slot[7] == 'X' or
            slot[2] == slot[5] == slot[8] == 'X' or slot[3] == slot[6] == slot[9] == 'X' or
            slot[1] == slot[5] == slot[9] == 'X' or slot[3] == slot[5] == slot[7] == 'X'):
            print("You win!\n")
            break
        # Check if the computer won
        elif (slot[1] == slot[2] == slot[3] == 'O' or slot[4] == slot[5] == slot[6] == 'O' or
              slot[7] == slot[8] == slot[9] == 'O' or slot[1] == slot[4] == slot[7] == 'O' or
              slot[2] == slot[5] == slot[8] == 'O' or slot[3] == slot[6] == slot[9] == 'O' or
              slot[1] == slot[5] == slot[9] == 'O' or slot[3] == slot[5] == slot[7] == 'O'):
            print("You lost!\n")
            break

# Checks for a tie
    if all(cell == 'X' or cell == 'O' for cell in slot.values()):
        print("It's a tie!")
        break