import tkinter as tk

def test():
    def on_selection_change(*args):
        print(f"Selected value: {selected_option.get()}")

    root = tk.Tk()
    root.title("OptionMenu Example")

    # Create StringVar and set default value
    selected_option = tk.StringVar(value="Option 1")
    selected_option.trace_add("write", on_selection_change)

    # Create OptionMenu
    options = ["Option 1", "Option 2", "Option 3"]
    option_menu = tk.OptionMenu(root, selected_option, *options)
    option_menu.pack(pady=20)

    root.mainloop()