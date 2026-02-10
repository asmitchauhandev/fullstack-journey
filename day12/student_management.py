# =====================================
# DAY 12: STUDENT MANAGEMENT SYSTEM
# Python + SQLite + User Input
# =====================================

import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL
)
""")

conn.commit()

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
                   (name, age, course))
    conn.commit()
    print("Student added successfully ✅")


def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\n=== Student List ===")
    for row in rows:
        print(row)


def delete_student():
    student_id = int(input("Enter student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print("Student deleted successfully ❌")


# ===== MAIN MENU =====

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        print("Exiting program 👋")
        break

    else:
        print("Invalid choice")

conn.close()