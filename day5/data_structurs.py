# ============================================
# DAY 5: PYTHON DATA STRUCTURES
# LIST | TUPLE | SET | DICTIONARY
# ============================================

print("=== LIST EXAMPLE ===")

# List (Ordered, Changeable, Allows Duplicates)
numbers = [10, 20, 30, 40, 20]

print("Original list:", numbers)

numbers.append(50)
print("After append:", numbers)

numbers.remove(20)
print("After remove:", numbers)

print("Looping through list:")
for num in numbers:
    print(num)


print("\n=== TUPLE EXAMPLE ===")

# Tuple (Ordered, Not Changeable, Allows Duplicates)
colors = ("red", "blue", "green", "red")

print("Tuple:", colors)
print("First element:", colors[0])
print("Length of tuple:", len(colors))

print("Looping through tuple:")
for color in colors:
    print(color)


print("\n=== SET EXAMPLE ===")

# Set (Unordered, No Duplicates)
fruits = {"apple", "banana", "mango", "apple"}

print("Set (duplicates removed automatically):", fruits)

fruits.add("orange")
print("After adding orange:", fruits)

fruits.remove("banana")
print("After removing banana:", fruits)

print("Looping through set:")
for fruit in fruits:
    print(fruit)


print("\n=== DICTIONARY EXAMPLE ===")

# Dictionary (Key-Value pairs)
student = {
    "name": "Asmit",
    "age": 21,
    "course": "BTech"
}

print("Original dictionary:", student)

print("Student name:", student["name"])

student["age"] = 22
print("After updating age:", student)

student["college"] = "Uttaranchal University"
print("After adding new key:", student)

print("Looping through dictionary:")
for key, value in student.items():
    print(key, ":", value)


print("\n=== DATA STRUCTURES PRACTICE COMPLETE ✅ ===")