import imports as i

def attendance_class_admin():

    def create_class_attendance():
        class_requirements = {}
        class_requirements["code"] = selected_course_Code.get()
        class_requirements["date"] = date_today
        class_requirements["time"] = f"{selected_time_start.get()} - {selected_time_end.get()}"
        class_requirements["room"] = selected_classroom.get()

        print(f"Creating Attendance: {class_requirements}") 
        i.db.db_create_class_attendance(class_requirements)  
        get_class_list_attendance()

    def get_class_list_attendance():
        class_list = i.db.db_getClassList()
        
        print(f"Class List: {class_list}") 
        #clear the table
        for items in tree.get_children():
            tree.delete(items)

        # Insert data into the Treeview
        for row in class_list:
            tree.insert("", "end", values=row)
    
    def get_Course_List():
        c_list = i.db.db_getCourses()
        print(f"Course List: {c_list}")
        return c_list

    #-----------------------------------------------------
    #Setup window size and position
    panel_attendance_class = i.tk.Tk()
    panel_attendance_class.title("CLASS ATTENDANCE (ADMIN)")
    panel_attendance_class = i.Functions.c_Panel_Setup.Panel_Setup(panel_attendance_class,900,450)
    #-----------------------------------------------------

    #Main Widgets
    # Define columns for the Treeview
    columns = ("ID", "Code","Name","Date")

    # Create the labelForm Widget
    frame_options = i.tk.LabelFrame(panel_attendance_class, text="Options", font=("Helvetica", 10, "bold"))
    frame_options.pack(padx=10,pady=10,side="left",expand=True,fill="both")
    #-----------------------------------------------------------------------------------------------
    frame_class_list = i.tk.LabelFrame(panel_attendance_class, text="Class List", font=("Helvetica", 10, "bold"))
    frame_class_list.pack(padx=10,pady=10,side="right",expand=True,fill="both")

    # Create the Treeview widget
    tree = i.ttk.Treeview(frame_class_list, columns=columns, show="headings", height=8)
    tree.pack(pady=20,padx=20,expand=True,fill="both")

    # Define column headings
    tree.heading("ID", text="ID")
    tree.heading("Code", text="Code")
    tree.heading("Name", text="Name")
    tree.heading("Date", text="Date")

    # Define column widths
    tree.column("ID", anchor="center", width=50)
    tree.column("Code", anchor="center", width=50)
    tree.column("Name", anchor="center", width=150)
    tree.column("Date", anchor="center", width=50)

    # Sample data for the Treeview
    get_class_list_attendance()

    i.tk.Label(frame_options,text="CREATE ATTENDANCE", font=("Helvetica", 9, "bold")).grid(row=0,column=0,padx=5,pady=5)

    # Variable to store the selected option
    course_list = get_Course_List()
    selected_course_Code = i.tk.StringVar(value=course_list[0][0])

    def course_codes():
        codes = []
        for items in course_list:
            codes.append(items[0])

        return codes
    
    label_courseName = i.tk.Label(frame_options, text="",font=("Helvetica", 9))
    def getCourseName(*args):
        selected_code = selected_course_Code.get()
        print(selected_code)
        for items in course_list:
            if selected_code == items[0]:
                label_courseName.config(text=items[1])
                print(f"Updated Course Name: {items[1]}")

    # Create the dropdown (OptionMenu)
    i.tk.Label(frame_options,text="Select Class : ", font=("Helvetica", 9,"bold")).grid(row=1,column=0,padx=5,pady=5,sticky="w")
    opt_courseCode = i.tk.OptionMenu(frame_options, selected_course_Code, *course_codes())
    selected_course_Code.trace_add("write", getCourseName)
    opt_courseCode.config(width=8)
    opt_courseCode.grid(row=1,column=1,pady=5,sticky="w")

    i.tk.Label(frame_options, text="Course Name : ",font=("Helvetica", 9,"bold")).grid(row=2,column=0,padx=5,pady=5,sticky="w")
    label_courseName.grid(row=2,column=1,sticky="w")

    # Time Slot for Class
    time_slot = ["8:00AM","9:00AM","10:00AM","11:00AM","12:00PM","1:00PM","2:00PM",
                  "3:00PM","4:00PM","5:00PM","6:00PM","7:00PM","8:00PM","9:00PM"
                 ]
    
    selected_time_start = i.tk.StringVar()
    selected_time_start.set(time_slot[0])
    selected_time_end = i.tk.StringVar()
    selected_time_end.set(time_slot[-1])

    # Create the dropdown (Time Start)
    i.tk.Label(frame_options,text="Time Start : ", font=("Helvetica", 9,"bold")).grid(row=3,column=0,padx=5,pady=5,sticky="w")
    opt_timeStart = i.tk.OptionMenu(frame_options, selected_time_start, *time_slot)
    opt_timeStart.config(width=8)
    opt_timeStart.grid(row=3,column=1,pady=5,sticky="w")

    # Create the dropdown (Time End)
    i.tk.Label(frame_options,text="Time End : ", font=("Helvetica", 9,"bold")).grid(row=4,column=0,padx=5,pady=5,sticky="w")
    opt_timeEnd = i.tk.OptionMenu(frame_options, selected_time_end, *time_slot)
    opt_timeEnd.config(width=8)
    opt_timeEnd.grid(row=4,column=1,pady=5,sticky="w")

    # Classrooms
    classroom_list = ["G1","G2","G3","G4","G5",
                      "1.1","1.2","1.3","1.4","1.5"
                 ]
    # time_end = ["8:00AM","9:00AM","10:00AM","11:00AM","12:00PM","1:00PM","2:00PM",
    #               "3:00PM","4:00PM","5:00PM","6:00PM","7:00PM","8:00PM","9:00PM"
    #              ]
    
    selected_classroom = i.tk.StringVar()
    selected_classroom.set(classroom_list[0])

    # Create the dropdown (Time Start)
    i.tk.Label(frame_options,text="Classroom : ", font=("Helvetica", 9,"bold")).grid(row=5,column=0,padx=5,pady=5,sticky="w")
    opt_classroom = i.tk.OptionMenu(frame_options, selected_classroom, *classroom_list)
    opt_classroom.config(width=8)
    opt_classroom.grid(row=5,column=1,pady=5,sticky="w")

    # Spacer / New Line
    space_label = i.tk.Label(frame_options, text="")
    space_label.grid(row=6, column=0, sticky="nsew")

    btn_create_attendance_list = i.tk.Button(frame_options,
                                             text="Create",
                                             command=lambda: create_class_attendance(),
                                             font=("Helvetica", 10),
                                             width=10)
    btn_create_attendance_list.grid(row=7,column=1,sticky="w")
    
    # Date Today Label
    date_today = i.datetime.now().date()

    date_label = i.tk.Label(frame_options, text=f"DATE : \t{date_today}", font=("Helvetica", 10))
    date_label.grid(row=8,column=0,sticky="s")
    frame_options.rowconfigure(8,weight=1)

    panel_attendance_class.mainloop()


# attendance_class_admin()