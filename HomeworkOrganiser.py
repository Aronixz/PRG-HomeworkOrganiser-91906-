'''
Name: Aaron Adil
Purpose: Help students organise their learning after school
Start Date: 21/07/2026
Date: 12/8/2026
Version: 2 (almosy done second tab, need to add save features)
Notes For Later: I can try to create a Logic class, and put the add subject functionality in the logic class. *BACK UP THE FILE FIRST!!!
'''
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import*
import json
import os

# Tell Windows your app is DPI-aware: https://stackoverflow.com/questions/41315873/attempting-to-resolve-blurred-tkinter-text-scaling-on-windows-10-high-dpi-disp
# fixes blurry tkinter window
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

# CONSTANTS
font_title = ("Verdana", 14, "bold")
font = ("Verdana", 11)
font_sub = ("Verdana", 12, "bold")
IMPORTANCE = ["Low", "Medium", "High", "Very High"]
MAX_TIME = 1440
MIN_TIME = 2
CHARACTER_LIMIT = 100

# VARIABLES
total_time = 0
subject_details = {}
temp_subject_details = subject_details
add_subject_combolist = []
count = 1

class TimeLogic:
    def remove_total_time(self, time):
        global total_time
        total_time -= time

    def add_to_total_time(self, time):
        global total_time
        total_time += time
        print(total_time)


class HomeworkOrganiserGUI:
    def __init__(self, root):
        '''Initialise everything'''
        self.root = root
        self.root.title("Homework Organiser")

        # initialise time logic
        self.time = TimeLogic()

        # initialise ttk.Notebook in the root window
        self.notebook = ttk.Notebook(self.root)

        # initialise the frames
        self.frame1 = ttk.Frame(self.notebook)
        self.frame2 = ttk.Frame(self.notebook)
        self.frame3 = ttk.Frame(self.notebook)
        self.frame1.pack(padx=5, pady=5)
        self.frame2.pack(padx=5, pady=5)
        self.frame3.pack(padx=5, pady=5)

        # labels that will be included in each frame
        label1 = ttk.Label(self.frame1, text="Add Homework", font=font_title)
        label2 = ttk.Label(self.frame2, text="Homework List", font=font_title)
        label3 = ttk.Label(self.frame3, text="Remove Homework", font=font_title)
        label1.pack(padx=15, pady=15)
        label2.pack(padx=15, pady=15)
        label3.pack(padx=15, pady=15)


        # opens a help window for clarification using show info message box
        self.help1 = ttk.Button(self.frame1, text="?", width= 5, command=lambda:showinfo("What can you do here?", "Here you can add homework tasks by clicking the 'Add Homework' button. Once you do that, the tasks are added onto the 'Homework List' tab. To view your list, click that tab."))
        self.help1.pack(side=tk.TOP)

        # add the frames to each tab
        self.notebook.add(self.frame1, text="Add Homework")
        self.notebook.add(self.frame2, text="Homework List")
        self.notebook.add(self.frame3, text="Remove Homework")

        self.notebook.pack(padx=5, pady=5)

        # frame 1 components gui
        self.frame1_components()
        # frame 2 components gui
        self.frame2_components()
        # frame 3 components gui
        self.frame3_components()


    def frame1_components(self):
        '''Initialise the Add Homework components'''
        # holds the add subjects components
        add_subject_frame = ttk.LabelFrame(self.frame1, text="Add Homework")
        add_subject_frame.pack(padx=5, pady=5)

        # entry boxes with labels
        subject_label = ttk.Label(add_subject_frame, text="Subject")
        self.subject_entry = ttk.Combobox(add_subject_frame, values=add_subject_combolist)

        self.subject_entry.grid(row=1, column=0)
        subject_label.grid(row=0, column=0)

        importance_label = ttk.Label(add_subject_frame, text="Importance")
        self.importance_entry = ttk.Combobox(add_subject_frame, values=IMPORTANCE)
        self.importance_entry.grid(row=1,column=1)
        importance_label.grid(row=0, column=1)

        time_label = ttk.Label(add_subject_frame, text="Time (minutes)")
        self.time_entry = ttk.Spinbox(add_subject_frame, from_=5, to=1440, increment=5)
        self.time_entry.grid(row=3,column=0)
        time_label.grid(row=2, column=0)

        # add subject button
        self.add_homework_button = ttk.Button(add_subject_frame, text="Add Homework", command=self.add_subject)
        self.add_homework_button.grid(column=1, row=2, rowspan=2)

        # details entry box with label
        detail_label = ttk.Label(add_subject_frame, text="Details")
        detail_label.grid(row=4, column=0)
        self.details_entry = ttk.Entry(add_subject_frame, width=42)
        self.details_entry.grid(row=5, columnspan=2, padx=5)
        self.details_entry.bind("<KeyRelease>", self.check_detail_entry_len)

        '''Load Homework on button press'''
        ttk.Label(self.frame1, text="Load homework data", font=font_sub).pack()
        ttk.Label(self.frame1, text="If you want to edit a previous task, \nselect it from the subject dropdown, \nand click this button ⬇").pack()

        # Load homework button
        load_subject_button = ttk.Button(self.frame1, text="Load Homework", command=self.load_subject_data)
        load_subject_button.pack()


    def frame2_components(self):
        '''Initialise the Homework list components'''
        self.time_label = ttk.Label(self.frame2, text=f"{total_time} min")
        self.time_label.pack()

        self.save_button = ttk.Button(self.frame2, text="Save", command=self.save)
        self.save_button.pack()

        self.load_save()


    def frame3_components(self):
        '''Initialise the components for Remove Homework frame'''
        # combo box with all the subjects
        self.remove_homework_combo = ttk.Combobox(self.frame3, values=list(subject_details.keys()), state="readonly")
        self.remove_homework_combo.pack()

        # remove button
        self.remove_homework_but = ttk.Button(self.frame3, text="Remove", command=self.remove_homework)
        self.remove_homework_but.pack()

        # opens a help window for clarification using show info message box
        self.help1 = ttk.Button(self.frame3, text="?", width= 5, command=lambda:showinfo("Heads up", "Removing a subject may require you to restart the program"))
        self.help1.pack()


    def remove_homework(self):
        '''Command for the remove homework button. It removes it from the dictionary, saves, then restarts the program'''
        global subject_details
        homework_remove = self.remove_homework_combo.get()
        if homework_remove in subject_details:
            # remove
            subject_details.pop(homework_remove, "Not Found")

            # save
            self.save()

            # restarts the program
            root.destroy()
            os.startfile("main.py")
        else:
            showerror("Error", "No input in the box")
        

    def add_to_hmklist(self):
        '''Adds the homework to the second tab'''
        # creates a list for all subjects
        subject_list = list(subject_details.keys())

        # resets the temporary dictionary
        temp_subject_details = {}

        # makes it so that the only subject and its details is the last subject
        temp_subject_details.update({f"{subject_list[-1]}":subject_details[subject_list[-1]]})
        print(temp_subject_details)

        global count
        for subject in temp_subject_details:            
            self.homework_list_frame = ttk.LabelFrame(self.frame2, text=f"Homework #{count}")
            self.homework_list_frame.pack()
            count += 1

            # preconfigured grid for each frame
            self.homework_list_frame.rowconfigure([0,1,2], minsize=20)
            self.homework_list_frame.columnconfigure([0,1,2,3], minsize=100)

            # titles 
            ttk.Label(self.homework_list_frame, text="Subject", font=font_sub).grid(row=0, column=1)
            ttk.Label(self.homework_list_frame, text="Importance", font=font_sub).grid(row=0, column=2)
            ttk.Label(self.homework_list_frame, text="Time", font=font_sub).grid(row=0, column=3)

            # checkbox
            self.tick_homework = ttk.Checkbutton(self.homework_list_frame)
            self.tick_homework.grid(row=1, column=0)

            # label for items
            subject_lbl = ttk.Label(self.homework_list_frame, text=subject)
            subject_lbl.grid(row=1, column=1)

            importance_lbl = ttk.Label(self.homework_list_frame, text=temp_subject_details[subject]["Importance"])
            importance_lbl.grid(row=1, column=2)

            time_lbl = ttk.Label(self.homework_list_frame, text=temp_subject_details[subject]["Time"])
            time_lbl.grid(row=1, column=3)

            details_lbl = ttk.Label(self.homework_list_frame, text=temp_subject_details[subject]["Details"])
            details_lbl.grid(row=2, column=1, columnspan=3)


    def add_subject(self):
        '''Adds the subjects into a dictionary and deletes what was in the entry boxes'''
        time = self.time_entry.get()
        importance = self.importance_entry.get()
        details = self.details_entry.get()
        subject = self.subject_entry.get()

        # add the time to total time and display the new total time
        self.time.add_to_total_time(int(time))
        self.time_label.configure(text=f"Total time: {total_time} min")

        # if there is nothing in any of the boxes then show the error
        if time == "" or importance == "" or details == "" or subject == "":
            showerror("Missing Parameters", "You have empty entries, please write something")
        else:
            try:
                time = int(time)
                # not allowed if the time is greater than a full day
                if time <= MAX_TIME and time >= MIN_TIME:
                    # adds the entries into a dictionary if valid
                    inner_dict = {"Time":time, "Importance":importance, "Details":details}
                    subject_details.update({self.subject_entry.get():inner_dict})
                    print(subject_details)

                    # adds the subject into a list for the combobox. It updates constantly
                    self.subject_entry.config(values=list(subject_details.keys()))
                    self.remove_homework_combo.config(values=list(subject_details.keys()))

                    # deletes the entries after confirmation
                    self.clear_subject_entries()
                    
                    #self.remove_homework_list()
                    self.add_to_hmklist()
                else:
                    showerror("Invalid Entry", f"Invalid time!\n({MIN_TIME} minutes - {MAX_TIME} minutes)")

            except ValueError: # if the time is not an integer
                showerror("Invalid Entry", "Time must be an integer")


    def check_homework_changetime(self):
        if self.tick_homework.instate(['selected']):
            self.time.remove_total_time
        

    def clear_subject_entries(self):
        '''Deletes the entries'''
        self.subject_entry.delete(0, tk.END)
        self.importance_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.details_entry.delete(0, tk.END)


    def load_subject_data(self):
        '''Loads the subject details for a particular selected subject'''
        # get the subject
        subject = self.subject_entry.get()

        # if there is no subject (the dict is empty)
        if subject_details == {}:
            showerror("No homework", "Lucky you! You have no homework to load.")
        elif subject == "":
            showerror("No subject selected in entry box", "You have no subject in the entry box")
        elif subject not in list(subject_details.keys()):
            showwarning("Subejct Not Added", "This subject has not been added yet. Click the 'Add Homework' button first")
        else:
            # clear the entries first
            self.clear_subject_entries()

            # it also clears the subject entry, so I will add it back
            self.subject_entry.insert(0, subject)

            # enter the subject time
            time = subject_details[subject]["Time"]
            self.time_entry.insert(0, time)

            # enter the subject importance
            importance = subject_details[subject]["Importance"]
            self.importance_entry.insert(0, importance)

            # enter the details 
            details = subject_details[subject]["Details"]
            self.details_entry.insert(0, details)

    
    def save(self):
        '''Saves the data'''
        with open("TaskSave.json", "w") as file:
            json.dump(subject_details, file, indent=4)
            showinfo("Saved", "Your list is saved")
            

    def load_save(self):
        '''Loads the save data'''
        global subject_details
        # open previous save
        try:
            with open("TaskSave.json", "r") as file:
                subject_details = json.load(file)
                # loads the stuff onto the second tab
                global count
                global total_time
                global add_subject_combolist

                add_subject_combolist = list(subject_details.keys())
                for subject in subject_details:            
                    self.homework_list_frame = ttk.LabelFrame(self.frame2, text=f"Homework #{count}")
                    self.homework_list_frame.pack()
                    count += 1

                    # preconfigured grid for each frame
                    self.homework_list_frame.rowconfigure([0,1,2], minsize=20)
                    self.homework_list_frame.columnconfigure([0,1,2,3], minsize=100)

                    # titles 
                    ttk.Label(self.homework_list_frame, text="Subject", font=font_sub).grid(row=0, column=1)
                    ttk.Label(self.homework_list_frame, text="Importance", font=font_sub).grid(row=0, column=2)
                    ttk.Label(self.homework_list_frame, text="Time", font=font_sub).grid(row=0, column=3)

                    # checkbox
                    self.tick_homework = ttk.Checkbutton(self.homework_list_frame)
                    self.tick_homework.grid(row=1, column=0)

                    # label for items
                    subject_lbl = ttk.Label(self.homework_list_frame, text=subject)
                    subject_lbl.grid(row=1, column=1)

                    importance_lbl = ttk.Label(self.homework_list_frame, text=subject_details[subject]["Importance"])
                    importance_lbl.grid(row=1, column=2)

                    time_lbl = ttk.Label(self.homework_list_frame, text=subject_details[subject]["Time"])
                    time_lbl.grid(row=1, column=3)

                    details_lbl = ttk.Label(self.homework_list_frame, text=subject_details[subject]["Details"])
                    details_lbl.grid(row=2, column=1, columnspan=3)

                    total_time += subject_details[subject]["Time"]

                # add the subject details into a list for combobox
                self.subject_entry.config(values=add_subject_combolist)

                self.time_label.configure(text=f"Total time: {total_time} min")
        
        except FileNotFoundError:
            subject_details = {} # from the entries


    def check_detail_entry_len(self, event):
        '''Checks the length of the entry used to add character limit'''
        if len(self.details_entry.get()) >= CHARACTER_LIMIT:
            # delete any extra characters
            self.details_entry.delete(CHARACTER_LIMIT-1, tk.END)


root = tk.Tk()
window = HomeworkOrganiserGUI(root)
root.mainloop()