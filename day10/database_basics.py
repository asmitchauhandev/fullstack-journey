# =====================================
# DAY 10: SQL BASICS USING SQLITE
# =====================================

import sqlite3

# Connect to database (file create ho jayegi)
conn = sqlite3.connect("students.db")

# Cursor object
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

# Insert data
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Asmit", 20))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Rahul", 22))

conn.commit()

# Select data
print("=== All Students ===")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Update data
cursor.execute("UPDATE students SET age = 21 WHERE name = 'Asmit'")
conn.commit()

# Delete data
cursor.execute("DELETE FROM students WHERE name = 'Rahul'")
conn.commit()

print("\n=== After Update & Delete ===")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close connection
conn.close()