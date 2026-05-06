# Week 1 – Gap Day 2 Assignment Set B
# Student: Asma Umar | Institute: As-Sa’adah Institute
# Theme: Multiple Inputs + Real-World Logic

print("--- Assignment 4: Simple Interest Calculator ---")
principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate: "))
time = float(input("Enter Time: "))
si = (principal * rate * time) / 100
print(f"Simple Interest is: {si}")

print("\n--- Assignment 5: Basic Profit/Loss Calculator ---")
cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))
if selling_price > cost_price:
    print(f"Profit is: {selling_price - cost_price}")
elif cost_price > selling_price:
    print(f"Loss is: {cost_price - selling_price}")
else:
    print("No Profit, No Loss.")

print("\n--- Task: Retail Transaction Summary (Grocery Bill) ---")
print("Grocery Bill")
print("-" * 20)
item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))
total_bill = item1 + item2 + item3
print("-" * 20)
print(f"Total Amount Due: {total_bill}")

print("\n--- Task: Academic Performance Evaluator ---")
marks_obtained = float(input("Enter your numerical marks: "))
total_marks = 100  # Standard total
percentage = (marks_obtained / total_marks) * 100
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print("Status: Performance evaluated successfully.")
