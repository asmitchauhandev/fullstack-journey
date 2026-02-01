# ================================
# DAY 3: CONDITIONALS + LOOPS
# ================================

print("=== CONDITIONAL STATEMENTS ===")

# 1. Check age category
age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor")
elif age >= 18 and age < 60:
    print("You are an adult")
else:
    print("You are a senior citizen")


# 2. Even or Odd number
num = int(input("\nEnter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


print("\n=== LOOPS ===")

# 3. Print numbers from 1 to 10
print("\nNumbers from 1 to 10:")
for i in range(1, 11):
    print(i)


# 4. Table of a number
table_num = int(input("\nEnter number for table: "))

for i in range(1, 11):
    print(table_num, "x", i, "=", table_num * i)


# 5. While loop example
print("\nWhile loop output:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1


print("\n=== BASIC LOGIC ===")

# 6. Simple login check
username = input("\nEnter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

print("\n=== DAY 3 COMPLETE ===")