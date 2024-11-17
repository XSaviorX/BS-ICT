import imports as i
from Panel_Attendance_Class import attendance_class_admin
from Panel_Attendance_Student import attendance_student

#Function for Home Page
def Menu_Attendance(panel,role):

    def rpt_Class():
        new_window.destroy()
        attendance_class_admin()

    def rpt_Student():
        new_window.destroy()
        attendance_student()
    def exit():
        new_window.destroy()

    #-----------------------------------------------------
    #Setup window size and position

    new_window = i.tk.Toplevel(panel)
    new_window = i.Functions.c_Panel_Setup.Panel_Setup(new_window,300,300)
    new_window.title("Attendance Menu")
    #-----------------------------------------------------
    # - WIDGETS
    i.tk.Label(new_window, text="Attendance Options", font=("Helvetica", 14, "bold")).pack(pady=10)

    i.tk.Button(new_window, text="Unit/Class Attendance",command=lambda: rpt_Class(), font=("Helvetica", 10), width=20).pack(pady=10)
    i.tk.Button(new_window, text="Student Attendance",command=lambda:rpt_Student(), font=("Helvetica", 10), width=20).pack(pady=10)
    i.tk.Button(new_window, text="Exit",command=lambda:exit(), font=("Helvetica", 10), width=20).pack(pady=10)

    
        