import imports as i



#Function for Home Page
def ReportMenu(panel):

    def rpt_class():
        pass
    def rpt_individual():
        pass
    def exit():
        new_window.destroy()

    #-----------------------------------------------------
    #Setup window size and position

    new_window = i.tk.Toplevel(panel)
    new_window = i.Functions.c_Panel_Setup.Panel_Setup(new_window,300,300)
    new_window.title("Report Menu")
    #-----------------------------------------------------
    # - WIDGETS
    
    i.tk.Label(new_window, text="Report Options", font=("Helvetica", 14, "bold")).pack(pady=10)

    i.tk.Button(new_window, text="Class Report",command=lambda:rpt_class(), font=("Helvetica", 10), width=20).pack(pady=10)
    i.tk.Button(new_window, text="Individual Report",command=lambda:rpt_individual(), font=("Helvetica", 10), width=20).pack(pady=10)
    i.tk.Button(new_window, text="Exit",command=lambda:exit(), font=("Helvetica", 10), width=20).pack(pady=10)

    
        