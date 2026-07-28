import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# entry box
entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=20)

clear_button = tk.Button(root, text="Add Subject", font=("Helvetica", 14))
clear_button.pack(pady=20)

# deletes the entry
clear_button.config(command=lambda: entry.delete(0, tk.END))

root.mainloop()