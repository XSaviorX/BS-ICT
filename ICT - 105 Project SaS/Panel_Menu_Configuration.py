import imports as i
from Panel_Configuration_User import config_user
from Panel_Configuration_Class import config_class


#Function for Home Page
def Menu_Configuration(panel):

    def c_Class():
        new_window.destroy()
        config_class()
    def c_users():
        new_window.destroy()
        config_user()
    def exit():
        new_window.destroy()

    #-----------------------------------------------------
    #Setup window size and position

    new_window = i.tk.Toplevel(panel)
    new_window = i.Functions.c_Panel_Setup.Panel_Setup(new_window,400,350)
    new_window.title("Configuration Management")
    #-----------------------------------------------------
    # - WIDGETS
    i.tk.Label(new_window, text="Configuration Management", font=("Helvetica", 14, "bold")).pack(pady=10)

    i.tk.Button(new_window, text="Manage Units/Classes",command=lambda: c_Class(), font=("Helvetica", 10), width=20).pack(pady=10)
    i.tk.Button(new_window, text="Manage Users (Lecturers and Students)",command=lambda:c_users(), font=("Helvetica", 10), width=20).pack(pady=10)
    i.tk.Button(new_window, text="Exit",command=lambda:exit(), font=("Helvetica", 10), width=20).pack(pady=10)

    
        