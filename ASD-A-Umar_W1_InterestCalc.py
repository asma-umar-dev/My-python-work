# Assignment 4: Simple Interest Calculator
# Student: Asma Umar | Institute: As-Sa’adah Institute

print("--- Simple Interest Calculator ---")
principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate: "))
time = float(input("Enter Time: "))

# Formula: (P * R * T) / 100
si = (principal * rate * time) / 100

print(f"Simple Interest is: {si}")
