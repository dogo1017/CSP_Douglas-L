import random  
  
low = 1  
high = 6  
guess = 0  
num1 = random.randint(low,high)
num2 = random.randint(low,high)
num3 = random.randint(low,high)
num4 = random.randint(low,high)


correct_count = 0  
wrong_count = 0  

while guess == 0:  
    if correct_count == 4:
        print("You got all of them correct!")
        guess = 1
    user_input = input("Enter your guess:\n ")  
  
    if len(user_input) != 4:  
        print("Please enter exactly 4 characters.")  
        continue 
    
    for index in range(4):
        if str(eval(f'num{index + 1}')) == user_input[index]:  
            correct_count += 1      
        elif user_input[index] in [str(num1), str(num2), str(num3), str(num4)]:  
            wrong_count += 1  

  

    print("Correct:", correct_count, "Wrong:", wrong_count)  