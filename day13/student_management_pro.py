# =====================================
# DAY 13: PROFESSIONAL STUDENT MANAGEMENT SYSTEM
# With Validation + Error Handling
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
    try:
        name = input("Enter name: ").strip()
        if name == "":
            print("Name cannot be empty ❌")
            return

        age = int(input("Enter age: "))
        if age <= 0:
            print("Age must be positive ❌")
            return

        course = input("Enter course: ").strip()
        if course == "":
            print("Course cannot be empty ❌")
            return

        cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
                       (name, age, course))
        conn.commit()

        print("Student added successfully ✅")

    except ValueError:
        print("Invalid input! Age must be a number ❌")

    except Exception as e:
        print("Unexpected error:", e)


def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if not rows:
        print("No students found 📭")
        return

    print("\n=== Student List ===")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]}")


def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()

        if cursor.rowcount == 0:
            print("Student not found ❌")
        else:
            print("Student deleted successfully ✅")

    except ValueError:
        print("ID must be a number ❌")

    except Exception as e:
        print("Unexpected error:", e)


# ===== MAIN MENU =====

while True:
    print("\n===== Professional Student Management =====")
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
        print("Invalid choice ❌")

conn.close()