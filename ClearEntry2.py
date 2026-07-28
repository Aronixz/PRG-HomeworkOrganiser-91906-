import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# sets the variable for entry box which stores the value
entry_var = tk.StringVar()

# sets the textvariable to the entry variable so they are linked
entry = tk.Entry(root, textvariable=entry_var, font=("Helvetica", 14))
entry.pack(pady=20)

clear_button = tk.Button(root, text="Add Subject", font=("Helvetica", 14))
clear_button.pack(pady=20)

# uses .set(""), to clear the entry
clear_button.config(command=lambda: entry_var.set(""))

root.mainloop()