# =====================================
# DAY 9: OOP ADVANCED
# INHERITANCE + ENCAPSULATION PROJECT
# =====================================

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # Encapsulation (private variable)

    def deposit(self, amount):
        self.__balance += amount
        print("Deposit successful ✅")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance ❌")
        else:
            self.__balance -= amount
            print("Withdrawal successful ✅")

    def get_balance(self):
        return self.__balance


# Inheritance
class SavingsAccount(BankAccount):

    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print("Interest added 💰")


# ===== Program Start =====

print("=== Savings Account System ===")

name = input("Enter account holder name: ")
balance = int(input("Enter initial balance: "))
interest = float(input("Enter interest rate (%): "))

account = SavingsAccount(name, balance, interest)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Add Interest")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        amount = int(input("Enter amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = int(input("Enter amount: "))
        account.withdraw(amount)

    elif choice == "3":
        print("Current balance:", account.get_balance())

    elif choice == "4":
        account.add_interest()

    elif choice == "5":
        print("Thank you 💳")
        break

    else:
        print("Invalid choice")