# =====================================
# DAY 4: PYTHON FUNCTIONS + MINI PROJECT
# PROJECT: ATM SYSTEM (BASIC)
# =====================================

# Global balance
balance = 10000


# -------- FUNCTIONS --------

def check_balance():
    print("\nYour current balance is:", balance)


def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Deposit successful!")
    else:
        print("Invalid amount")


def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print("Please collect your cash")


def show_menu():
    print("\n=== ATM MENU ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


# -------- MAIN LOGIC --------

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you for using ATM. Goodbye 👋")
        break
    else:
        print("Invalid choice, try again")