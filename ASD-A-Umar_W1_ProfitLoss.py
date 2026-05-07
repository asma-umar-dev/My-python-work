# Assignment 5: Basic Profit/Loss Calculator
# Student: Asma Umar | Institute: As-Sa’adah Institute

print("--- Profit/Loss Calculator ---")
cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

if selling_price > cost_price:
    print(f"Profit is: {selling_price - cost_price}")
elif cost_price > selling_price:
    print(f"Loss is: {cost_price - selling_price}")
else:
    print("No Profit, No Loss.")
