# Douglas London, Functions notes Python

# hold actions to be reused

#number = int(input("give me a number:\n"))
#number2 = int(input("give me another number:\n"))

def add(numOne, numTwo):
    return numOne+numTwo

#print(add(number, number2))


def values(type):
    return input(f"please give me a {type}:\n")

name = values("name")
place = values("place")
verb = values("verb (Past tense)")

print(f"{name} was really fast getting to {place} because they {verb} the whole way there.")