# =====================================
# DAY 8: OOP PROJECT
# MINI PROJECT: BANK ACCOUNT SYSTEM
# =====================================

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful ✅")
        print("New balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance ❌")
        else:
            self.balance -= amount
            print("Withdrawal successful ✅")
            print("Remaining balance:", self.balance)

    def check_balance(self):
        print("Account holder:", self.name)
        print("Current balance:", self.balance)


# ===== Program Start =====

print("=== Welcome to Bank System ===")

name = input("Enter account holder name: ")
balance = int(input("Enter initial balance: "))

account = BankAccount(name, balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        amount = int(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = int(input("Enter withdraw amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank you for using Bank System 💳")
        break

    else:
        print("Invalid choice")