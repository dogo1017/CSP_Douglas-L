# Douglas london, finantial calculator Update Pyhton

print("Hello, this is my finantial calculator that calculates savings, spendins, and other finantial expenses.")

def collecting_data(type):
    return input(f"What is your monthly {type} cost:\n")
 
def info(cost, income, type):
    percent = cost/income*100
    print(f"Your {type} is ${cost:.2f}, which is {percent}% of your income.")


    
income = float(input("What is your monthly income:\n"))
rent = float(collecting_data("rent"))
utilities = float(collecting_data("utilities"))
groceries = float(collecting_data("groceries"))
transportation = float(collecting_data("transportation"))

savings = income*0.1
spendings = income-savings-rent-utilities-groceries-transportation

info(rent, income, "rent")
info(utilities, income, "utillities")
info(rent, income, "groceries")
info(rent, income, "transportation")
info(savings, income, "savings")
info(spendings, income, "spendings")




