import random  

low = 1  
high = 6  
guess = 0  
num1 = random.randint(low, high)
num2 = random.randint(low, high)
num3 = random.randint(low, high)
num4 = random.randint(low, high)


correct_answer = [str(num1), str(num2), str(num3), str(num4)]

correct_count = 0  
wrong_count = 0  

while guess == 0:  
    if correct_count == 4:
        print("You got all of them correct!")
        guess = 1
        break

    user_input = input("Enter your guess (4 digits between 1 and 6):\n ")  
    
    if len(user_input) != 4:  
        print("Please enter exactly 4 characters.")  
        continue
    

    correct_count = 0
    wrong_count = 0

 
    correct_positions = [False, False, False, False]
    wrong_positions = [False, False, False, False]  
    temp_correct_answer = correct_answer.copy()

  
    for index in range(4):
        if user_input[index] == correct_answer[index]:  
            correct_count += 1
            correct_positions[index] = True  
            temp_correct_answer[index] = None  
    for index in range(4):
        if not correct_positions[index]:  
            for compare_index in range(4):
                if not correct_positions[compare_index] and user_input[index] == str(temp_correct_answer[compare_index]) and temp_correct_answer[compare_index] is not None:
                    wrong_count += 1
                    temp_correct_answer[compare_index] = None  

    print(f"Correct: {correct_count}, Wrong: {wrong_count}")
