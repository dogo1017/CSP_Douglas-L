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
rent = rent/income*100
# calculate percent income of utilities  (utilities/income*100) (variable)
utilities = utilities/income
# calculate percent income of groceries (groceries/income*100) (variable)

# calculate percent income of transportation (transportation/income*100) (variable)

# calculate percent income of spending (spending/income*100) (variable)

#  your rent is $XX.XX which is XX% of your income. (print)

#  your utilities is $XX.XX which is XX% of your income. (print)

#  your groceries is $XX.XX which is XX% of your income. (print)

#  your transportation is $XX.XX which is XX% of your income. (print)

#  your savings is $XX.XX which is XX% of your income. (print)

# #  your spending is $XX.XX which is XX% of your income. (print)