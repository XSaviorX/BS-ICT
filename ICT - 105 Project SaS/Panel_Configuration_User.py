import imports as i
import Panel_Student_Registration as sr

def config_user():


    def get_UserList():
        user_list = i.db.db_getUserList()
        
        print(f"User List: {user_list}") 
        #clear the table
        for items in tree.get_children():
            tree.delete(items)

        # Insert data into the Treeview
        for row in user_list:
            tree.insert("", "end", values=row)

    def edit_user():
        pass

    def add_user():
        sr.student_registration()

    def on_row_select(event):
        # Get the selected item
        selected_item = tree.selection()
        if selected_item:
            # Retrieve the data from the selected row
            row_data = tree.item(selected_item[0], "values")
            en_name.delete(0,i.tk.END)
            en_username.delete(0,i.tk.END)
            en_id.delete(0,i.tk.END)
            en_id.insert(0,row_data[0])
            en_name.insert(0,row_data[1])
            en_username.insert(0,row_data[2])
            print(f"Selected Row Data: {row_data}")
        else:
            print("No row selected")

    #-----------------------------------------------------
    #Setup window size and position
    panel_config_user = i.tk.Tk()
    panel_config_user.title("USER CONFIGURATION")
    panel_config_user = i.Functions.c_Panel_Setup.Panel_Setup(panel_config_user,800,550)
    #-----------------------------------------------------

    #Main Widgets

    # Create the labelForm Widget
    frame_config_user = i.tk.LabelFrame(panel_config_user, text="User Acccount List", font=("Helvetica", 10, "bold"))
    frame_config_user.pack(padx=10,pady=10,expand=True,fill="both")
    #-----------------------------------------------------------------------------------------------

    
    # Define columns for the Treeview
    columns = ("ID","Name", "Username","Role")

    # Create the Treeview widget
    tree = i.ttk.Treeview(frame_config_user, columns=columns, show="headings", height=8)
    tree.pack(pady=20,padx=20,expand=True,fill="both")

    # Define column headings
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Username", text="Username")
    tree.heading("Role", text="Role")

    # Define column widths
    tree.column("ID", anchor="center", width=50)
    tree.column("Name", anchor="center", width=150)
    tree.column("Username", anchor="center", width=50)
    tree.column("Role", anchor="center", width=50)

    # Sample data for the Treeview
    get_UserList()

    tree.bind("<ButtonRelease-1>", on_row_select)
    #--------------------------------------------------------------------------
    frame_edit_class = i.tk.LabelFrame(panel_config_user, text="EDIT CLASS", font=("Helvetica", 10, "bold"))
    frame_edit_class.pack(padx=10,pady=10,expand=True,fill="both")

    i.tk.Label(frame_edit_class, text="ID NUMBER : ", font=("Helvetica",10)).grid(row=1,column=0,sticky="e",padx=10,pady=10)
    en_id = i.tk.Entry(frame_edit_class, width=30)
    en_id.grid(row=1, column=1, padx=5, pady=5)
    i.tk.Label(frame_edit_class, text="NAME : ", font=("Helvetica",10)).grid(row=2,column=0,sticky="e",padx=10,pady=10)
    en_name = i.tk.Entry(frame_edit_class, width=30)
    en_name.grid(row=2, column=1, padx=5, pady=5)
    i.tk.Label(frame_edit_class, text="USERNAME : ", font=("Helvetica",10)).grid(row=3,column=0,sticky="e",padx=10,pady=10)
    en_username = i.tk.Entry(frame_edit_class, width=30)
    en_username.grid(row=3, column=1, padx=5, pady=5)


    btn_add_user = i.tk.Button(panel_config_user,
                                text="ADD USER",
                                command=lambda: add_user(),
                                font=("Helvetica", 10),
                                width=10)
    btn_add_user.pack(padx=10,pady=10)

    btn_edit_user = i.tk.Button(panel_config_user,
                                text="EDIT USER",
                                command=lambda: edit_user(),
                                font=("Helvetica", 10),
                                width=10)
    btn_edit_user.pack(padx=10,pady=10)

    panel_config_user.mainloop()


#config_user()