#Alan De Lara
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
    

    return stages[wrong_attempts]  
  
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
