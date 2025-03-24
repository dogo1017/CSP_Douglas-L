import random  
  
low = 1  
high = 6  
guess = 0  
numbers = [random.randint(low, high) for _ in range(4)]  
  
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
  
    correct_count = 0  
    wrong_count = 0  
      
    for index in range(len(numbers)):  
        if user_input[index] == str(numbers[index]):  
            correct_count += 1  
        elif user_input[index] in [str(num) for num in numbers]:  
            wrong_count += 1  
  
    print("Correct:", correct_count, "Wrong:", wrong_count)  