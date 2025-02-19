# Douglas london, finantial calculator Update Pyhton

print("Hello, this is my finantial calculator that calculates savings, spendins, and other finantial expenses.")

def collecting_data(type):
    return input(f"What is your monthly {type} cost:\n")
    
    
income = float(input("What is your monthly income:\n"))
rent = collecting_data("rent")
utilities = collecting_data("utilities")
groceries = collecting_data("groceries")
transportation = collecting_data("transportation")

savings = income*0.1




