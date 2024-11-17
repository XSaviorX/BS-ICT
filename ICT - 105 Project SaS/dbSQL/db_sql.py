# import imports as i
import mysql.connector
import bcrypt
from mysql.connector import Error

from imports import messagebox
from tkinter import messagebox, ttk
from datetime import datetime as dt


def db_connect():
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'ochirrej120796',
            database = 'sas'
        )

        if connection.is_connected():
            return connection
        
    except Error as e:
        return messagebox.showerror("ERROR",e)
    
def db_getAccount(parameters):
    # messagebox.showinfo("dsadsada",parameters.passw)
    try:
        conn = db_connect()
        cursor = conn.cursor()
        query = f"SELECT * FROM accounts WHERE a_username = '{parameters.id}'"
        cursor.execute(query)
        result = cursor.fetchall()
        
        for items in result:
            usern = items[1]
            passw = items[2]
            role = items[3]

        # user_pass = 
        
        # pass_test = bcrypt.checkpw(user_pass, passw)

        # if pass_test:
        acount_info = {'username':usern,
                        'password':passw,
                        'role':role}

        return acount_info
        
    except Error as e:
        return messagebox.showerror("LOGIN ERROR",e)
    
#Getting student account
def db_getStudentData(student_id):
    try:
        #i.messagebox.showinfo("getStudentData", student_id)
        conn = db_connect()
        cursor = conn.cursor()
        query = f"SELECT * FROM student WHERE student_id = '{student_id}'"
        cursor.execute(query)
        result = cursor.fetchall()
        return result
        
    except Error as e:
        return messagebox.showerror("GET STUDENT DATA ERROR",e)

#get student_classes
def db_getStudent_ClassesData(student_id):
    try:
        #i.messagebox.showinfo("getStudentData", student_id)
        conn = db_connect()
        cursor = conn.cursor()
        query = f"SELECT * FROM student_classes_view WHERE student_id = '{student_id}'"
        cursor.execute(query)
        result = cursor.fetchall()
        return result
        
    except Error as e:
        return messagebox.showerror("GET STUDENT DATA",e)
    
#get Class List
def db_getClassList():
    try:
        #i.messagebox.showinfo("getStudentData", student_id)
        conn = db_connect()
        cursor = conn.cursor()
        query = f"SELECT class_id,course_code,course_name,class_date FROM class_list"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    except Error as e:
        return messagebox.showerror("GET CLASS LIST",e)

# get all courses
def db_getCourses():
    try:
        #i.messagebox.showinfo("getStudentData", student_id)
        conn = db_connect()
        cursor = conn.cursor()
        query = f"SELECT * FROM courses"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    except Error as e:
        return messagebox.showerror("GET COURSE LIST",e)
    

# create class attendance
def db_create_class_attendance(class_req):
    try:
        # i.messagebox.showinfo("das", class_req)
        conn = db_connect()
        cursor = conn.cursor()
        query = f"INSERT INTO classes (course_code, class_date, class_time, room) VALUES (%s,%s,%s,%s)"
        values = (class_req['code'],class_req['date'],class_req['time'],class_req['room'])
        cursor.execute(query,values)

        # query2 = f"SELECT * FROM student_classes"
        # cursor.execute(query2)
        # result2 = cursor.fetchall()

        # for items in result2:
        #     result3 = db_get_Attendance_status(items[1],items[2],dt.now().date())
        #     print(f"{items[1]},- {items[2]},- {dt.now().date()}")
        #     if len(result3) == 0 :
        #         query4 = f"INSERT INTO attendance (student_id,class_id,date,attendance_status,excuse_reason) VALUES (%s,%s,%s,%s,%s)"
        #         values4 = (items[1],items[2],dt.now().date(),"ABSENT","ABSENT")
        #         cursor.execute(query4,values4)

        conn.commit()
        
        messagebox.showinfo("CLASS ATTENDANCE INFO", "Creating of class attendance is successful \n\n " +
                               " You can now check the added record in the table")

    except Error as e:
        return messagebox.showerror("CREATE CLASS ATTENDANCE",e)
    
#get User List
def db_getUserList():
    try:
        #i.messagebox.showinfo("getStudentData", student_id)
        conn = db_connect()
        cursor = conn.cursor()
        query = f"SELECT * FROM user_list"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    except Error as e:
        return messagebox.showerror("GET USER LIST",e)

#get attendance status
def db_get_Attendance_status(student_id,class_id,date):
    try:
        #i.messagebox.showinfo("getStudentData", student_id)
        conn = db_connect()
        cursor = conn.cursor()
        query = f"SELECT * FROM attendance WHERE student_id= '{student_id}' AND class_id = '{class_id}' AND date = '{date}'"
        cursor.execute(query)
        result = cursor.fetchall()

        if len(result) == 0:
            result = 'ABSENT'

        return result

    except Error as e:
        return messagebox.showerror("GET STUDENT ATTENDANCE STATUS",e)
    

#update attendance status
def db_updateAttendance_Status():
    pass

#create account student
def db_create_studentAccount(student_data):
    
    try:
        conn = db_connect()
        cursor = conn.cursor()
        query = f"INSERT INTO accounts (a_username, a_password, role) VALUES (%s,%s,%s)"
        values = (student_data[2],student_data[3],'student')
        cursor.execute(query,values)

        query1 = f"SELECT account_id FROM accounts WHERE a_username = '{student_data[2]}'"
        cursor.execute(query1)
        result1 = cursor.fetchall()

        print(result1)

        # i.messagebox.showinfo("das", class_req)
        query2 = f"INSERT INTO student (student_id, student_name, student_email, account_id) VALUES (%s,%s,%s,%s)"
        values2 = (student_data[0],student_data[1],f'{student_data[0]}@stanleycollege.edu.au',result1[0][0])
        cursor.execute(query2,values2)

        conn.commit()
        
        messagebox.showinfo("ACCOUNT CREATION SUCCESSFUL")

    except Error as e:
        return messagebox.showerror("CREATE ACCOUNT ERROR",e)

            
















# import sqlite3

# def add_student(student_id, name, course):
#     connection = sqlite3.connect("attendance.db")
#     cursor = connection.cursor()
#     cursor.execute("INSERT INTO students (id, name, course) VALUES (?, ?, ?)", (student_id, name, course))
#     connection.commit()
#     connection.close()
#     print(f"Added student: {name}")

# def view_students():
#     connection = sqlite3.connect("attendance.db")
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM students")
#     students = cursor.fetchall()
#     connection.close()
#     print("Student List:")
#     for student in students:
#         print(student)

# # Example console-based role-based login
# def role_based_login():
#     if login("instructor_password.hash"):
#         print("Login successful. Role: Instructor.")
#     else:
#         print("Invalid login.")
