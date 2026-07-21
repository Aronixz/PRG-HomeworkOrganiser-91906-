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
        add_subject_frame.pack()

        # entry boxes with labels
        subject_label = ttk.Label(add_subject_frame, text="Subject")
        self.subject = ttk.Entry(add_subject_frame)
        self.subject.grid(row=1, column=0)
        subject_label.grid(row=0, column=0)

        importance_label = ttk.Label(add_subject_frame, text="Importance")
        self.importance = ttk.Entry(add_subject_frame)
        self.importance.grid(row=1,column=1)
        importance_label.grid(row=0, column=1)

        time_label = ttk.Label(add_subject_frame, text="Time")
        self.time = ttk.Entry(add_subject_frame)
        self.time.grid(row=3,column=0)
        time_label.grid(row=2, column=0)


    def frame2_components(self):
        '''Initialise the frame2 components'''
        pass

root = tk.Tk()
window = HomeworkOrganiserGUI(root)
root.mainloop()