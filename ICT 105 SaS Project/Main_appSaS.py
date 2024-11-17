import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedTk
from setup_database import initialize_database  # Import the database setup function
from user_management import login  # Import the login function from user_management

# User data for login validation (simple dictionary for now, could load from a database)
users = {
    "admin": {"password": "admin", "role": "instructor"},
    "student": {"password": "student", "role": "student"}
}

class LoginPage(ThemedTk):
    def __init__(self):
        super().__init__(theme="breeze")
        self.title("Student Attendance System (SaS) - Login")
        self.geometry("400x250")
        
        tk.Label(self, text="Student Attendance System", font=("Helvetica", 16, "bold")).pack(pady=10)
        tk.Label(self, text="Please enter your login details", font=("Helvetica", 10)).pack(pady=5)
        
        # Username Entry
        tk.Label(self, text="Username:", font=("Helvetica", 10)).pack(pady=5)
        self.username_entry = tk.Entry(self, font=("Helvetica", 10))
        self.username_entry.pack()
        
        # Password Entry
        tk.Label(self, text="Password:", font=("Helvetica", 10)).pack(pady=5)
        self.password_entry = tk.Entry(self, show="*", font=("Helvetica", 10))
        self.password_entry.pack()
        
        # Login Button
        tk.Button(self, text="Login", command=self.verify_login, font=("Helvetica", 10), bg="#4CAF50", fg="white").pack(pady=20)

    def verify_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username in users and users[username]["password"] == password:
            self.destroy()
            role = users[username]["role"]
            SaSHomePage(role).mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

class SaSHomePage(ThemedTk):
    def __init__(self, role):
        super().__init__(theme="breeze")
        self.title("Student Attendance System (SaS) - Home")
        self.geometry("450x350")
        self.role = role
        
        tk.Label(self, text="Welcome to Student Attendance System", font=("Helvetica", 16, "bold")).pack(pady=10)
        tk.Label(self, text="Please select an option from below", font=("Helvetica", 12)).pack(pady=5)
        
        # Buttons for Menu Options
        tk.Button(self, text="Report Menu", command=self.open_report_menu, font=("Helvetica", 10), width=20).pack(pady=5)
        tk.Button(self, text="Attendance Menu", command=self.open_attendance_menu, font=("Helvetica", 10), width=20).pack(pady=5)
        if self.role == "instructor":
            tk.Button(self, text="Configuration Management Menu", command=self.open_configuration_menu, font=("Helvetica", 10), width=20).pack(pady=5)
        else:
            tk.Label(self, text="(Instructor-only access for Configuration)", font=("Helvetica", 8), fg="grey").pack(pady=5)
        
    def open_report_menu(self):
        ReportMenu(self).mainloop()
    
    def open_attendance_menu(self):
        AttendanceMenu(self).mainloop()
    
    def open_configuration_menu(self):
        if self.role == "instructor":
            ConfigurationMenu(self).mainloop()
        else:
            messagebox.showerror("Access Denied", "Only instructors can access the configuration menu")

class ReportMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Report Menu")
        self.geometry("300x300")
        
        tk.Label(self, text="Report Options", font=("Helvetica", 14, "bold")).pack(pady=10)
        
        tk.Button(self, text="Stats Report", command=self.generate_stats_report, font=("Helvetica", 10), width=20).pack(pady=5)
        tk.Button(self, text="Class Report", command=self.generate_class_report, font=("Helvetica", 10), width=20).pack(pady=5)
        tk.Button(self, text="Individual Report", command=self.generate_individual_report, font=("Helvetica", 10), width=20).pack(pady=5)
        tk.Button(self, text="Exit", command=self.destroy, font=("Helvetica", 10), width=20).pack(pady=10)
    
    def generate_stats_report(self):
        messagebox.showinfo("Report", "Generating Stats Report...")
    
    def generate_class_report(self):
        messagebox.showinfo("Report", "Generating Class Report...")
    
    def generate_individual_report(self):
        messagebox.showinfo("Report", "Generating Individual Report...")

class AttendanceMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Attendance Menu")
        self.geometry("300x300")
        
        tk.Label(self, text="Attendance Management", font=("Helvetica", 14, "bold")).pack(pady=10)
        
        tk.Button(self, text="Unit/Class Attendance", command=self.manage_unit_class_attendance, font=("Helvetica", 10), width=20).pack(pady=5)
        tk.Button(self, text="Student Attendance", command=self.manage_student_attendance, font=("Helvetica", 10), width=20).pack(pady=5)
        tk.Button(self, text="Exit", command=self.destroy, font=("Helvetica", 10), width=20).pack(pady=10)
    
    def manage_unit_class_attendance(self):
        messagebox.showinfo("Attendance", "Managing Unit/Class Attendance...")
    
    def manage_student_attendance(self):
        messagebox.showinfo("Attendance", "Managing Student Attendance...")

class ConfigurationMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Configuration Management")
        self.geometry("400x350")
        
        tk.Label(self, text="Configuration Management", font=("Helvetica", 14, "bold")).pack(pady=10)
        
        tk.Button(self, text="Manage Units/Classes", command=self.manage_units_classes, font=("Helvetica", 10), width=25).pack(pady=5)
        tk.Button(self, text="Manage Users (Lecturers and Students)", command=self.manage_users, font=("Helvetica", 10), width=25).pack(pady=5)
        tk.Button(self, text="Exit", command=self.destroy, font=("Helvetica", 10), width=25).pack(pady=10)
    
    def manage_units_classes(self):
        messagebox.showinfo("Configuration", "Managing Units/Classes...")
    
    def manage_users(self):
        messagebox.showinfo("Configuration", "Managing Users (Lecturers and Students)...")

# Main Application Execution
if __name__ == "__main__":
    initialize_database()
    LoginPage().mainloop()
