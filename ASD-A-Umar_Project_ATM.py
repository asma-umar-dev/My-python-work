# Project 1: Smart ATM Simulation
# Student: Asma Umar | Institute: As-Sa’adah Institute

balance = 5000  # Initial Balance

def check_balance():
    print(f"\nYour current balance is: {balance}")

def deposit_money():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Deposit successful.")
    else:
        print("Invalid amount.")

def withdraw_money():
    global balance
    amount = float(input("Enter withdrawal amount: "))
    if amount > balance:
        print("Withdrawal denied: insufficient balance.")
    elif amount <= 0:
        print("Invalid amount.")
    else:
        balance -= amount
        print("Withdrawal successful.")
        print(f"Remaining balance: {balance}")

def show_menu():
    print("\nWelcome to Smart ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

# Main Logic
while True:
    show_menu()
    choice = input("Enter choice: ")
    
    if choice == '1':
        check_balance()
    elif choice == '2':
        deposit_money()
    elif choice == '3':
        withdraw_money()
    elif choice == '4':
        print("Thank you for using Smart ATM. Goodbye!")
        break
    else:
        print("Invalid menu choice. Please try again.")
