import imports as i
import bcrypt

def student_registration():
    
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed
    
    def create_account():
        s_id = id_entry.get()
        s_name = name_entry.get()
        uname = uname_entry.get()
        passw = hash_password(pword_entry.get())

        student = [s_id,s_name,uname,passw]

        i.db.db_create_studentAccount(student)


    #-----------------------------------------------------
    #Setup window size and position
    panel_student = i.tk.Tk()
    panel_student.title("STUDENT REGISTRATION")
    panel_student = i.Functions.c_Panel_Setup.Panel_Setup(panel_student,400,350)
    #-----------------------------------------------------
    #Widgets
    group_frame = i.tk.LabelFrame(panel_student, text="Student Information", padx=10, pady=10)
    group_frame.pack(padx=10, pady=10, fill="both", expand=True)

    # Add widgets inside the LabelFrame
    #ID
    id_label = i.tk.Label(group_frame, text="ID:")
    id_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    id_entry = i.tk.Entry(group_frame, width=20)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    #Name
    name_label = i.tk.Label(group_frame, text="Name:", font=("Helvetica", 10))
    name_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

    name_entry = i.tk.Entry(group_frame, width=20)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    #Username
    uname_label = i.tk.Label(group_frame, text="Username:", font=("Helvetica", 10))
    uname_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

    uname_entry = i.tk.Entry(group_frame, width=20)
    uname_entry.grid(row=2, column=1, padx=5, pady=5)

    #Password
    pword_label = i.tk.Label(group_frame, text="Password:", font=("Helvetica", 10))
    pword_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)

    pword_entry = i.tk.Entry(group_frame, width=20, show="*")
    pword_entry.grid(row=3, column=1, padx=5, pady=5)

    submit_button =i.tk.Button(group_frame, text="Register", command=lambda: create_account())
    submit_button.grid(row=4, column=0, columnspan=2, pady=10)

    panel_student.mainloop()

# student_registration()
    

    
    
    




