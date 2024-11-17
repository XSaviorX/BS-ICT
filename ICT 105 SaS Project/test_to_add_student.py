import sqlite3
from user_management import login

def add_student(student_id, name, course):
    connection = sqlite3.connect("attendance.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students (id, name, course) VALUES (?, ?, ?)", (student_id, name, course))
    connection.commit()
    connection.close()
    print(f"Added student: {name}")

def view_students():
    connection = sqlite3.connect("attendance.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    connection.close()
    print("Student List:")
    for student in students:
        print(student)

# Example console-based role-based login
def role_based_login():
    if login("instructor_password.hash"):
        print("Login successful. Role: Instructor.")
    else:
        print("Invalid login.")
