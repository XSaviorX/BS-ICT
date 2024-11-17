import imports as i

account = {}

def attendance_student():

    def get_student_data(student_id):

        student_data = i.db.db_getStudentData(student_id)

        if account_role == "admin":
            student_id_label.config(text=f"{student_data[0][0]}")
            student_name_label.config(text=f"{student_data[0][1]}")
        else:
            n_id_label.config(text=f"ID   : \t{student_data[0][0]}")
            name_label.config(text=f"Name : \t{student_data[0][1]}")

        class_data = i.db.db_getStudent_ClassesData(student_id)

        # Insert data into the table with checkboxes

        def get_status(student_id,class_id,date):
            status = i.db.db_get_Attendance_status(student_id,class_id,date)

            return status

        for row in class_data:
            item_id = str(row[0])  # Using the ID as the row identifier
            table.insert("", "end", iid=item_id, values=(row[3], row[4], get_status(student_id,row[2],i.datetime.now().date())))

    def update_attendance(class_data,student_id):
        if account_role == "admin":
            pass
        else:
            pass

    #-----------------------------------------------------
    #Setup window size and position
    panel_student_attendance = i.tk.Tk()
    panel_student_attendance.title("STUDENT ATTENDANCE (ADMIN)")
    panel_student_attendance = i.Functions.c_Panel_Setup.Panel_Setup(panel_student_attendance,600,450)
    #-----------------------------------------------------
    #Widgets

    account_role = i.Functions.user.role

    
    search_frame = i.tk.LabelFrame(panel_student_attendance, text="Search Student", font=("Helvetica", 10, "bold"))
    id_label = i.tk.Label(search_frame, text="ID:")
    id_entry = i.tk.Entry(search_frame, width=30)
    submit_button =i.tk.Button(search_frame, text="Search", command=lambda: get_student_data(id_entry.get()))

    student_frame = i.tk.LabelFrame(panel_student_attendance, font=("Helvetica", 10, "bold"),text="Student Information")
    space_label = i.tk.Label(student_frame, text="")
    n_id_label = i.tk.Label(student_frame, text="ID:")
    student_id_label = i.tk.Label(student_frame, text="",width=25)
    name_label = i.tk.Label(student_frame, text="Name:")
    student_name_label = i.tk.Label(student_frame, text="",width=25)

    listofClass = i.tk.LabelFrame(panel_student_attendance, font=("Helvetica", 10, "bold"),text="Student Class List")
    btn_attendance = i.tk.Button(listofClass,text="Update Attendance", command=lambda: update_attendance(),font=("Helvetica", 6))

    if account_role == "admin":
        search_frame.grid(padx=10,pady=10, row=0,column=0,sticky="nsew")
        # Add widgets inside the LabelFrame
        id_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        id_entry.grid(row=0, column=1, padx=5, pady=5)
        submit_button.grid(row=0, column=2, columnspan=2, pady=5,padx=10)
        #==========================================================================
        student_frame.grid(padx=10,pady=10, row=0,column=1,sticky="nsew")
        space_label.grid(row=0, column=4, sticky="e", padx=5, pady=5)
        #--------------------------------------------------------------------------
        n_id_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        student_id_label.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        #--------------------------------------------------------------------------
        name_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        student_name_label.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        #--------------------------------------------------------------------------
        listofClass.grid(padx=10,pady=10, row=1,column=0,columnspan=2,sticky="nsew")
        #--------------------------------------------------------------------------
    else:
        student_frame.pack(padx=10,pady=10,fill="both")
        #space_label.grid(column=1,row=0, padx=5, pady=5)
        #--------------------------------------------------------------------------
        n_id_label.grid(column=0,row=0,padx=1, pady=5,sticky="e")
        #student_id_label.grid(column=1,row=0, padx=1, pady=5)
        #--------------------------------------------------------------------------
        name_label.grid(column=0,row=1, padx=5, pady=5,sticky="e")
        #student_name_label.grid(column=1,row=1, padx=5, pady=5)
        #--------------------------------------------------------------------------
        listofClass = i.tk.LabelFrame(panel_student_attendance, font=("Helvetica", 10, "bold"),
                                      text=f"Student Class List for today ({i.datetime.now().date()})")
        listofClass.pack(padx=10,pady=10, fill="both")
        #--------------------------------------------------------------------------
        btn_attendance.config(text="Take Attendance")

    # Define columns for the table
    columns = ("ID", "Description","Status")

    table = i.ttk.Treeview(listofClass, columns=columns, show="headings", height=8)
    table.grid(row=1,column=0,pady=20,padx=30)

    # Define column headings
    table.heading("#1", text="ID")
    table.heading("#2", text="Description")
    table.heading("#3", text="Status")

    # Define column widths
    table.column("#1", anchor="center", width=50)
    table.column("#2", anchor="center", width=300)
    table.column("#3", anchor="center", width=150)

    btn_attendance.grid(row=2,column=0,padx=5,pady=5)

    date_label = i.tk.Label(panel_student_attendance, font=("Helvetica", 12),text=f"Date:  {i.datetime.now().date()}")
    
    if account_role == "student":
        get_student_data(account['username'])
    else:
        date_label.grid(row=2,column=0,padx=5, pady=5,sticky="w")

    panel_student_attendance.mainloop()
    

#attendance_student()




