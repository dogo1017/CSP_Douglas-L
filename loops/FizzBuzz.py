#Douglas London, FizzBuzz python

number = 0

while (number <= 50):
    if (number == 0):
        print(0)
        number += 1
    elif(number%3==0 and number%5==0):
        print("FizzBuzz")
        number += 1
    elif(number%5==0):
        print("buzz")
        number += 1
    elif (number%3==0):
        print("fizz")
        number += 1
    else:
        print(number)
        number += 1
else:
    exit
