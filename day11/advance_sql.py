# =====================================
# DAY 11: ADVANCED SQL (RELATIONSHIP + JOIN)
# =====================================

import sqlite3

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# Enable foreign key
cursor.execute("PRAGMA foreign_keys = ON")

# Create Course table
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL UNIQUE
)
""")

# Create Students table with Foreign Key
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course_id INTEGER,
    FOREIGN KEY (course_id) REFERENCES courses(id)
)
""")

conn.commit()

# Insert Courses
cursor.execute("INSERT OR IGNORE INTO courses (course_name) VALUES (?)", ("BCA",))
cursor.execute("INSERT OR IGNORE INTO courses (course_name) VALUES (?)", ("MCA",))

conn.commit()

# Insert Students
cursor.execute("INSERT INTO students (name, age, course_id) VALUES (?, ?, ?)", ("Asmit", 20, 1))
cursor.execute("INSERT INTO students (name, age, course_id) VALUES (?, ?, ?)", ("Rahul", 22, 2))

conn.commit()

# JOIN Query
print("=== Student Details with Course ===")

cursor.execute("""
SELECT students.name, students.age, courses.course_name
FROM students
JOIN courses ON students.course_id = courses.id
""")

rows = cursor.fetchall()

for row in rows:
    print("Name:", row[0], "| Age:", row[1], "| Course:", row[2])

conn.close()