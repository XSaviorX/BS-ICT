import imports as i

def aattendance_student():

    def get_student_data(student_id):

        student_data = i.db.db_getStudentData(student_id)

        student_id_label.config(text=student_data[0][0])
        student_name_label.config(text=student_data[0][1])

        # Insert data into the table with checkboxes
        for row in student_data:
            item_id = str(row[4])  # Using the ID as the row identifier
            checkbox_states[item_id] = False  # Initialize each checkbox as unchecked
            # Insert the row with an unchecked checkbox symbol
            checkbox_symbol = UNCHECKED
            table.insert("", "end", iid=item_id, values=(checkbox_symbol, row[4], row[5]))

    def update_attendance():
        pass

    #-----------------------------------------------------
    #Setup window size and position
    panel_student_attendance = i.tk.Tk()
    panel_student_attendance.title("STUDENT ATTENDANCE (ADMIN)")
    panel_student_attendance = i.Functions.c_Panel_Setup.Panel_Setup(panel_student_attendance,600,450)
    #-----------------------------------------------------
    #Widgets
    search_frame = i.tk.LabelFrame(panel_student_attendance, text="Search Student", font=("Helvetica", 10, "bold"))
    search_frame.grid(padx=10,pady=10, row=0,column=0,sticky="nsew")

    # Add widgets inside the LabelFrame
    #ID
    id_label = i.tk.Label(search_frame, text="ID:")
    id_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    id_entry = i.tk.Entry(search_frame, width=30)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    submit_button =i.tk.Button(search_frame, text="Search", command=lambda: get_student_data(id_entry.get()))
    submit_button.grid(row=0, column=2, columnspan=2, pady=5,padx=10)

    #==========================================================================
    student_frame = i.tk.LabelFrame(panel_student_attendance, font=("Helvetica", 10, "bold"),text="Student Information")
    student_frame.grid(padx=10,pady=10, row=0,column=1,sticky="nsew")

    space_label = i.tk.Label(student_frame, text="")
    space_label.grid(row=0, column=4, sticky="e", padx=5, pady=5)
    #--------------------------------------------------------------------------
    n_id_label = i.tk.Label(student_frame, text="ID:")
    n_id_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
    
    student_id_label = i.tk.Label(student_frame, text="",width=25)
    student_id_label.grid(row=0, column=1, sticky="w", padx=5, pady=5)
    #--------------------------------------------------------------------------
    name_label = i.tk.Label(student_frame, text="Name:")
    name_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
    
    student_name_label = i.tk.Label(student_frame, text="",width=25)
    student_name_label.grid(row=1, column=1, sticky="w", padx=5, pady=5)
    #--------------------------------------------------------------------------

    listofClass = i.tk.LabelFrame(panel_student_attendance, font=("Helvetica", 10, "bold"),text="Student Class List")
    listofClass.grid(padx=10,pady=10, row=1,column=0,columnspan=2,sticky="nsew")


    # Define columns for the table
    columns = ("Status", "ID", "Description")

    # Checkbox symbols
    CHECKED = "☑"
    UNCHECKED = "☐"

    # Dictionary to hold checkbox states
    checkbox_states = {}

    # Function to toggle checkbox state
    def toggle_checkbox(item_id):
        # Toggle the checkbox state for the item
        checkbox_states[item_id] = not checkbox_states[item_id]
        # Update the displayed checkbox symbol
        checkbox_symbol = CHECKED if checkbox_states[item_id] else UNCHECKED
        table.item(item_id, values=(checkbox_symbol,) + table.item(item_id, "values")[1:])

    # Create the Treeview widget with checkboxes

    table = i.ttk.Treeview(listofClass, columns=columns, show="headings", height=8)
    table.grid(row=1,column=0,pady=20,padx=30)

    # Define column headings
    table.heading("#1", text="Status")
    table.heading("#2", text="ID")
    table.heading("#3", text="Description")

    # Define column widths
    table.column("#1", anchor="center", width=50)  # Checkbox column
    table.column("#2", anchor="center", width=150)
    table.column("#3", anchor="center", width=300)

    # Bind a click event to toggle the checkbox state
    def on_click(event):
        # Get the clicked row item
        item_id = table.identify_row(event.y)
        # Check if it is in the checkbox column
        if table.identify_column(event.x) == "#1" and item_id:
            toggle_checkbox(item_id)

    # Bind the click event to the table
    table.bind("<Button-1>", on_click)


    i.tk.Button(listofClass,text="Update Attendance", command=lambda: update_attendance()).grid(row=2,column=0,padx=5,pady=5)

    
    date_label = i.tk.Label(panel_student_attendance, font=("Helvetica", 12),text=f"Date:  {i.datetime.now().date()}")
    date_label.grid(row=2,column=0,padx=5, pady=5,sticky="w")


    panel_student_attendance.mainloop()
    

#attendance_student()




