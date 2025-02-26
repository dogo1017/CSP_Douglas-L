# Douglas London, Old enough python

print("Welcome to my old enough program that tells you whether you are old enough to vote, drive, get a learners permit, and go to school.")

age = int(input("What is your age:\n"))

if(age >= 18):
    print("You can vote\n")
elif(age >= 17):
    print("you can drive\n")
elif(age >= 15):
    print("You can get a learners permit\n")
elif(age >= 4):
    print("You can go to school")
else:
    print("How the frick is a todler working this program!!! You should not be able to even read! Go back to watching cocomelon little nerd.")