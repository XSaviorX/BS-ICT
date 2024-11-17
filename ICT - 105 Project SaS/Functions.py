import imports as i

#Function/Classes for setting up window/panel size and position

class c_Panel_Setup(i.ThemedTk):
    def __init__(self):
         self.__init__(theme="classic")
         
    def Panel_Setup(panel,window_width = 400, window_height = 300):
        panel.geometry(f"{window_width}x{window_height}")

        screen_width = panel.winfo_screenwidth()
        screen_height = panel.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        panel.geometry(f"{window_width}x{window_height}+{x}+{y}")

        return panel

class user:
     
    def __init__(self):
        self.id = ''
        self.passw = ''
        self.role = ''

    def set_role(role):
         user.role = role

    def set_account(account):
        user.id = account['username']
        user.passw = account['password']

    def get_account():
         pass

    

#Funciton for printing space/ newline
def label_spacer(panel,loop=1):

        newLine = ""

        while True:
            if loop == 0:
                break
            else:
                newLine += "\n"
                loop -= 1


        label = i.tk.Label(panel, text="\n")
        label.pack()

        return label
