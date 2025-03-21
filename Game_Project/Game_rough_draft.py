import random  
  
low = 1  
high = 6  
guess = 0  
numbers = [random.randint(low, high) for _ in range(4)]  # Generate all numbers in one line  
  
while guess == 0:  
    user_input = input("Enter your guess:\n ")  
  
    if len(user_input) != 4:  
        print("Please enter exactly 4 characters.")  
        continue  # Skip to the next loop iteration  
  
    correct_count = 0  
    wrong_count = 0  
      
    for index in range(len(numbers)):  
        if user_input[index] == str(numbers[index]):  
            print("You have one correct in the right spot")  
            correct_count += 1  
        elif user_input[index] in [str(num) for num in numbers]:  
            print("You have one correct color in the wrong spot")  
            wrong_count += 1  
  
    print("Correct:", correct_count, "Wrong:", wrong_count)  