import imports as i
import Panel_MenuSelection
import Panel_Attendance_Student

#Function for Login Page
def Login():
    def test_LogIn():
        username = input_username.get()
        password = input_password.get()

        account = {'username': username,
                   'password': password}
        
        Acc_Valid = i.Functions.user
        Acc_Valid.set_account(account=account)
        account_info = i.db.db_getAccount(Acc_Valid)

        i.Functions.user.set_role(role=account_info["role"])

        if account_info:
            i.messagebox.showinfo("STATUS", "Successful Login")
            Panel_Attendance_Student.account = account_info
            Panel_login.destroy()
            role = i.Functions.user
            Panel_MenuSelection.menuSelection(role.role)
        else:        
            register_ask = i.messagebox.askyesno(title="ERROR: Non-existing account used",message="Please register first \n- [Yes] to proceed \n- [No] to cancel",options=any)
            if register_ask == i.messagebox.YES:
                pass
            else:
                pass


    Panel_login = i.tk.Tk()
    Panel_login.title("Student Attendance System (SaS) - Login")

    #-----------------------------------------------------
    #Setup window size and position
    i.Functions.c_Panel_Setup.Panel_Setup(Panel_login,600,450)
    #-----------------------------------------------------
    # - WIDGETS
    label_SaS = i.tk.Label(Panel_login, text="Student Attendance System", font=("Helvetica", 16, "bold"))
    label_SaS.pack(pady=10)
    label_welcome = i.tk.Label(Panel_login, text="Please enter your login details", font=("Helvetica", 12))
    label_welcome.pack(pady=5)

    #username input box
    label_username = i.tk.Label(Panel_login, text="Username:", font=("Helvetica", 11))
    label_username.pack(pady=5)
    input_username = i.tk.Entry(Panel_login,font=("Helvetica", 11), width=30, justify= 'center')
    input_username.pack(pady=10)
    
    #password input box
    label_password = i.tk.Label(Panel_login, text="Password:", font=("Helvetica", 11))
    label_password.pack(pady=5)
    input_password = i.tk.Entry(Panel_login, font=("Helvetica", 11),width=30, justify= 'center', show="*")
    input_password.pack(pady=10)

    i.Functions.label_spacer(Panel_login)

    button = i.tk.Button(Panel_login, text="LOG IN", font=("Helvetica", 10), command=lambda: test_LogIn())
    button.pack()

    Panel_login.mainloop()
