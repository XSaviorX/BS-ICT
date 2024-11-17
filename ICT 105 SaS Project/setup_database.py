import sqlite3

def initialize_database():
    connection = sqlite3.connect("attendance.db")
    cursor = connection.cursor()
    # Create tables for students and attendance records
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (id TEXT PRIMARY KEY, name TEXT, course TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS attendance (date TEXT, id TEXT, status TEXT, time TEXT)''')
    connection.commit()
    connection.close()
