import tkinter as tk
# Tell Windows your app is DPI-aware: https://stackoverflow.com/questions/41315873/attempting-to-resolve-blurred-tkinter-text-scaling-on-windows-10-high-dpi-disp
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

class App:
    def __init__(self, root):
        self.root = root

        # frame container
        self.container = tk.Frame(self.root)
        self.container.grid(row=0, column=0, sticky="nsew")

        # dict to hold the frames
        self.frames = {}
        self.frames["Window 1"] = self.window1_frame()
        self.frames["Window 2"] = self.window2_frame()

        # show the add subjects frame first
        self.show_frame("Window 1")

    def show_frame(self, name):
        '''displays the reqired frame from the dict'''
        frame = self.frames[name]
        frame.tkraise() # move the frame to the top of the stack

    def window1_frame(self):
        frame = tk.Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")

        self.to_window2 = tk.Button(frame, text="to Window 2", bg="yellow", command=lambda: self.show_frame("Window 2"))
        self.to_window2.pack()

        self.label = tk.Label(frame, text="Window 1")
        self.label.pack()

        return frame

    def window2_frame(self):
        frame = tk.Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")

        self.to_window1 = tk.Button(frame, text="to Window 1", bg="yellow", command=lambda: self.show_frame("Window 1"))
        self.to_window1.pack()

        self.label1 = tk.Label(frame, text="Window 2")
        self.label1.pack()

        return frame


root = tk.Tk()
app = App(root)
root.mainloop()
