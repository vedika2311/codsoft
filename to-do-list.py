import tkinter as tkn
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_listbox.insert(tkn.END, task)
        entry.delete(0, tkn.END)
    else:
        dialog = tkn.Toplevel(parent)
        dialog.title("Warning..!!")
        dialog.geometry("250x120")  # Set the width and height

        label = tkn.Label(dialog, text="Please Enter some task first before adding task .")
        label.pack(pady=20)

        button = tkn.Button(dialog, text="OK", command=dialog.destroy)
        button.pack(pady=10)

def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
    else:
        dialog = tkn.Toplevel(parent)
        dialog.title("Warning..!!")
        dialog.geometry("250x120")  # Set the width and height

        label = tkn.Label(dialog, text="Please select task first before removing it .")
        label.pack(pady=20)

        button = tkn.Button(dialog, text="OK", command=dialog.destroy)
        button.pack(pady=10)


parent = tkn.Tk()
parent.title("To-Do List Box")

entry = tkn.Entry(parent, width=70)
entry.pack(pady=20)


add_button = tkn.Button(parent, text="Click to Add Task ", command=add_task)
add_button.pack()


task_listbox = tkn.Listbox(parent, selectmode=tkn.SINGLE, height=10, width=40)
task_listbox.pack()


remove_button = tkn.Button(parent, text="Click to Remove Task", command=remove_task)
remove_button.pack()


parent.mainloop()
