# Project: Personal Budget Management System
# Student: Asma Umar | Institute: As-Sa’adah Institute

print("--- Welcome to Budget Manager ---")

# User se total budget lena
total_budget = float(input("Enter your total monthly budget: "))

print(f"\nInitial Budget: {total_budget}")
print("-" * 30)

# Kharchon (Expenses) ki details lena
food_expense = float(input("Enter food expenses: "))
rent_expense = float(input("Enter rent/bills expenses: "))
other_expense = float(input("Enter other miscellaneous expenses: "))

# Total kharcha calculate karna
total_spent = food_expense + rent_expense + other_expense

# Baqi bachi hui raqam (Remaining Balance)
remaining_balance = total_budget - total_spent

print("-" * 30)
print(f"Total Expenses: {total_spent}")

# Check karna ke budget khatam to nahi ho gaya
if remaining_balance < 0:
    print(f"Warning! You are over budget by: {abs(remaining_balance)}")
else:
    print(f"Remaining Balance: {remaining_balance}")

print("--- Thank you for using Budget Manager ---")
