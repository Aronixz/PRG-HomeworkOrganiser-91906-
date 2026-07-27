import tkinter as tk
from tkinter import ttk

# Tell Windows your app is DPI-aware: https://stackoverflow.com/questions/41315873/attempting-to-resolve-blurred-tkinter-text-scaling-on-windows-10-high-dpi-disp
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

# CONSTANTS
font_title = ("Verdana", 14, "bold")
font = ("Verdana", 11)

class Logic:
    def __init__(self):
        pass


class HomeworkOrganiserGUI:
    def __init__(self, root):
        '''Initialise everything'''
        self.root = root

        # initialise ttk.Notebook in the root window
        self.notebook = ttk.Notebook(self.root)

        # initialise the frames
        self.frame1 = ttk.Frame(self.notebook)
        self.frame2 = ttk.Frame(self.notebook)
        self.frame1.pack(padx=5, pady=5)
        self.frame2.pack(padx=5, pady=5)

        # labels that will be included in each frame
        label1 = ttk.Label(self.frame1, text="Add Subjects", font=font_title)
        label2 = ttk.Label(self.frame2, text="Homework List", font=font_title)
        label1.pack(padx=15, pady=15)
        label2.pack(padx=15, pady=15)

        # add the frames to each tab
        self.notebook.add(self.frame1, text="Add Subjects")
        self.notebook.add(self.frame2, text="Homework List")

        self.notebook.pack(padx=5, pady=5)

        # frame 1 components
        self.frame1_components()


    def frame1_components(self):
        '''Initialise the frame1 components'''
        # I can compare using .grid with using .pack
        # holds the add subjects components
        add_subject_frame = ttk.LabelFrame(self.frame1, text="Add Subject")
        add_subject_frame.pack(padx=5, pady=5)

        # entry boxes with labels
        subject_label = ttk.Label(add_subject_frame, text="Subject")
        self.subject_entry = ttk.Entry(add_subject_frame)
        self.subject_entry.grid(row=1, column=0)
        subject_label.grid(row=0, column=0)

        importance_label = ttk.Label(add_subject_frame, text="Importance")
        self.importance_entry = ttk.Entry(add_subject_frame)
        self.importance_entry.grid(row=1,column=1)
        importance_label.grid(row=0, column=1)

        time_label = ttk.Label(add_subject_frame, text="Time")
        self.time_entry = ttk.Entry(add_subject_frame)
        self.time_entry.grid(row=3,column=0)
        time_label.grid(row=2, column=0)

        # add subject button
        self.add_subject_button = ttk.Button(add_subject_frame, text="Add Subject", command=self.add_subject)
        self.add_subject_button.grid(column=1, row=2, rowspan=2)

        # details entry box with label
        detail_label = ttk.Label(add_subject_frame, text="Details")
        detail_label.grid(row=4, column=0)
        self.details_entry = ttk.Entry(add_subject_frame, width=42)
        self.details_entry.grid(row=5, columnspan=2, padx=5)


    def frame2_components(self):
        '''Initialise the frame2 components'''
        pass

    def add_subject(self):
        '''Adds the subjects into a dictionary and deletes what was in the entry boxes'''
        # must go after dictionary input
        # deletes the entries
        self.subject_entry.delete(0, tk.END)
        self.importance_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.details_entry.delete(0, tk.END)

root = tk.Tk()
window = HomeworkOrganiserGUI(root)
root.mainloop()