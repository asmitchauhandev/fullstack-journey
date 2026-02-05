# =====================================
# DAY 7: EXCEPTION HANDLING PROJECT
# MINI PROJECT: SECURE LOGIN + CALCULATOR
# =====================================

PASSWORD = "1234"
attempts = 3

# ===== LOGIN SYSTEM =====
while attempts > 0:
    entered_password = input("Enter password: ")

    if entered_password == PASSWORD:
        print("Login successful ✅")
        break
    else:
        attempts -= 1
        print("Wrong password ❌")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Account locked 🚫")
    exit()

# ===== CALCULATOR =====
print("\n=== SIMPLE CALCULATOR ===")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b)
    else:
        print("Invalid operation")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Please enter valid numbers")

finally:
    print("Program ended safely ✅")