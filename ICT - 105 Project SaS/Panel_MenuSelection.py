import imports as i
import Panel_Menu_Report
import Panel_Menu_Attendance
import Panel_Menu_Configuration

def menuSelection(role):

    def btnClicked_report():
        Panel_Menu_Report.ReportMenu(Panel_Menu)

    def btnClicked_attendance():
        Panel_Menu_Attendance.Menu_Attendance(Panel_Menu,role)

    def btnClicked_configuration():
        Panel_Menu_Configuration.Menu_Configuration(Panel_Menu)

    Panel_Menu = i.tk.Tk()
    Panel_Menu.title("Student Attendance System (SaS) - Home")

    #-----------------------------------------------------
    #Setup window size and position
    i.Functions.c_Panel_Setup.Panel_Setup(Panel_Menu,500,350)
    #-----------------------------------------------------
    # - WIDGETS
    i.tk.Label(Panel_Menu, text="Welcome to Student Attendance System", font=("Helvetica", 16, "bold")).pack(pady=10)
    i.tk.Label(Panel_Menu, text="Please select an option from below", font=("Helvetica", 12)).pack(pady=5)

    # btn_menu_report =  i.tk.Button(Panel_Menu, text="REPORTS", command=lambda: btnClicked_report(), font=("Helvetica", 20),width=20, height=1).pack(padx=3,pady=3)
    
    btn_menu_attendance =  i.tk.Button(Panel_Menu, text="Attendance", command=lambda: btnClicked_attendance(), font=("Helvetica", 20),width=20, height=1).pack(padx=3,pady=3)

    if role== 'admin':
        btn_menu_configuration =  i.tk.Button(Panel_Menu, text="Configuration", command=lambda: btnClicked_configuration(), font=("Helvetica", 20),width=20, height=1).pack(padx=3,pady=3)
    else:
        pass

    Panel_Menu.mainloop()