# Week 1 – Day 3 Assignment Set C
# Student: Asma Umar | Institute: As-Sa’adah Institute

print("--- 1. Grade Percentage Calculator ---")
sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
total = sub1 + sub2 + sub3
percentage = (total / 300) * 100
print(f"Total: {total}, Percentage: {percentage:.2f}%")

print("\n--- 2. Mini Custom Calculator ---")
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
print(f"Addition: {n1+n2}, Subtraction: {n1-n2}, Multiplication: {n1*n2}")
if n2 != 0: print(f"Division: {n1/n2}")

print("\n--- 3. Zakat Threshold Checker ---")
wealth = float(input("Enter total wealth: "))
if wealth >= 532000:
    print("Zakat is applicable.")
else:
    print("Zakat is not applicable.")
