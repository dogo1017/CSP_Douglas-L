# Douglas london, Loops Notes Python


# What is a loop? 
    # section of code that repeats multiple times
# What are the two types of loops?
    #for loop
nums = [12,3,66,7,3,3,2]

for num in nums:
    print(num)

    # While loop
x = 0

while x < 10:
    print(x)
    x+= 1
# What is iteration
    # That specific instance of the loop
    # iteration is the amount of times you are looping through
# What are lists? 
    # A variable that holds multiple values
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
siblings = ["Sara", "Bennett", "Rosalie", "Brielle"]
print(nums)
print(siblings[3])

siblings[2] = "Douglas"
siblings.pop(2)
siblings.insert(1, "Douglas")
# How do you make lists in python? 
    # use brackets, add items with correct data types, comma between each item
# How do you make for loops in python? 
for sibling in siblings:
    print(sibling)

for x in range(0,999999, 1):
    print (x)
# How do you make while loops in python?
import random

x = 1 # variable to keep count of iteration
goose = random.randint(1,20)


while x <= 20:
    if x == goose:
        print("Goose!")
        break
    else:
        print("Duck")
        x==1

#continue moves to next itteration 
    