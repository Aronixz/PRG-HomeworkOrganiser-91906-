import tkinter as tk
from tkinter import ttk

# Tell Windows your app is DPI-aware: https://stackoverflow.com/questions/41315873/attempting-to-resolve-blurred-tkinter-text-scaling-on-windows-10-high-dpi-disp
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

class HmwkOrganiser:
    def __init__(self, root):
        self.root = root

        # initialise ttk.Notebook in the root window
        self.notebook = ttk.Notebook(self.root)

        # initialise the frames
        frame1 = ttk.Frame(self.notebook)
        frame2 = ttk.Frame(self.notebook)
        frame1.pack(padx=5, pady=5)
        frame2.pack(padx=5, pady=5)

        # labels that will be included in each frame
        label1 = ttk.Label(frame1, text="Window 1")
        label2 = ttk.Label(frame2, text="Window 2")
        label1.pack()
        label2.pack()

        # add the frames to each tab
        self.notebook.add(frame1, text="Window 1")
        self.notebook.add(frame2, text="Window 2")

        self.notebook.pack(padx=5, pady=5)


root = tk.Tk()
window = HmwkOrganiser(root)
root.mainloop()