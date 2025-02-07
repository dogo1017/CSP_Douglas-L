# Douglas london, finantial calculator

# print statement that welcomes user and tells what the program does
print("Hello, this is my finantial calculator that calculates savings, spendins, and other finantial expenses.")
# ask user what their income is (wariable and input)
income = float(input("what is your monthly income?\n"))
# ask user what their rent is (wariable and input)
rent = float(input("what is your mothly cost of rent?\n"))
# ask user what their utilities is (wariable and input)
utilities = float(input("what is your monthly cost of utilities?\n"))
# ask user what their groceries is (wariable and input)
groceries = float(input("what is your monthly cost of groceries?\n"))
# ask user what their transportation is (wariable and input)
transportation = float(input("what is your monthly spend on transportation?\n"))
# calculate savinggs as 10% of income (income*.1) (variable)
savings = income*.1
# calculate spending as income-savings-rent-untilities-groveries-transportation (variable)
spendings = income-savings-rent-utilities-groceries-transportation
# calculate percent income of rent  (rent/income*100) (variable)
rent_percent = rent/income*100
# calculate percent income of utilities  (utilities/income*100) (variable)
utilities_percent = utilities/income*100
# calculate percent income of groceries (groceries/income*100) (variable)
groceries_percent = groceries/income*100
# calculate percent income of transportation (transportation/income*100) (variable)
transportation_percent = transportation/income*100
# calculate percent income of spending (spending/income*100) (variable)
spending_percent = spendings/income*100
#  your rent is $XX.XX which is XX% of your income. (print)
print("your rent is $",rent, "which is", rent_percent, "% of your income")
#  your utilities is $XX.XX which is XX% of your income. (print)
print("your utilities is $",utilities, "which is", utilities_percent, "% of your income")
#  your groceries is $XX.XX which is XX% of your income. (print)
print("your groceries is $",groceries, "which is", groceries_percent, "% of your income")
#  your transportation is $XX.XX which is XX% of your income. (print)
print("your tramsportation is $",transportation, "which is", transportation_percent, "% of your income")
#  your savings is $XX.XX which is XX% of your income. (print)
print("your savings is $",savings, "which is 10% of your income.")
# #  your spending is $XX.XX which is XX% of your income. (print)
print("your spendings is $",spendings, "which is", spending_percent, "% of your income")