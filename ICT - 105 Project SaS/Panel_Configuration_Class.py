import imports as i

def config_class():


    def get_classList():
        class_list = i.db.db_getClassList()
        
        print(f"User List: {class_list}") 
        #clear the table
        for items in tree.get_children():
            tree.delete(items)

        # Insert data into the Treeview
        for row in class_list:
            tree.insert("", "end", values=row)

    def edit_class():
        pass

    def on_row_select(event):
        # Get the selected item
        selected_item = tree.selection()
        if selected_item:
            # Retrieve the data from the selected row
            row_data = tree.item(selected_item[0], "values")
            en_courseCode.delete(0,i.tk.END)
            en_description.delete(0,i.tk.END)
            en_courseCode.insert(0,row_data[1])
            en_description.insert(0,row_data[2])
            print(f"Selected Row Data: {row_data}")
        else:
            print("No row selected")

    #-----------------------------------------------------
    #Setup window size and position
    panel_config_class = i.tk.Tk()
    panel_config_class.title("USER CONFIGURATION")
    panel_config_user = i.Functions.c_Panel_Setup.Panel_Setup(panel_config_class,800,550)
    #-----------------------------------------------------

    #Main Widgets

    # Create the labelForm Widget
    frame_config_class = i.tk.LabelFrame(panel_config_class, text="Class List", font=("Helvetica", 10, "bold"))
    frame_config_class.pack(padx=10,pady=10,expand=True,fill="both")
    #-----------------------------------------------------------------------------------------------

    
    # Define columns for the Treeview
    columns = ("ID","Code", "Description")

    # Create the Treeview widget
    tree = i.ttk.Treeview(frame_config_class, columns=columns, show="headings", height=8)
    tree.pack(pady=20,padx=20,expand=True,fill="both")

    # Define column headings
    tree.heading("ID", text="ID")
    tree.heading("Code", text="Code")
    tree.heading("Description", text="Description")

    # Define column widths
    tree.column("ID", anchor="center", width=50)
    tree.column("Code", anchor="center", width=50)
    tree.column("Description", anchor="center", width=150)

    # Sample data for the Treeview
    get_classList()

    tree.bind("<ButtonRelease-1>", on_row_select)

    #--------------------------------------------------------------------------
    frame_edit_class = i.tk.LabelFrame(panel_config_class, text="EDIT CLASS", font=("Helvetica", 10, "bold"))
    frame_edit_class.pack(padx=10,pady=10,expand=True,fill="both")

    i.tk.Label(frame_edit_class, text="COURSE CODE : ", font=("Helvetica",10)).grid(row=1,column=0,sticky="e",padx=10,pady=10)
    en_courseCode = i.tk.Entry(frame_edit_class, width=30)
    en_courseCode.grid(row=1, column=1, padx=5, pady=5)
    i.tk.Label(frame_edit_class, text="DESCRIPTIION : ", font=("Helvetica",10)).grid(row=2,column=0,sticky="e",padx=10,pady=10)
    en_description = i.tk.Entry(frame_edit_class, width=30)
    en_description.grid(row=2, column=1, padx=5, pady=5)

    btn_edit_user = i.tk.Button(panel_config_user,
                                text="EDIT CLASS",
                                command=lambda: edit_class(),
                                font=("Helvetica", 10),
                                width=10)
    btn_edit_user.pack(padx=10,pady=10)

    panel_config_user.mainloop()


# config_class()