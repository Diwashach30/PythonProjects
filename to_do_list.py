## to do list using GUI

import tkinter as tk
from tkinter import messagebox
from tkinter import *



window = tk.Tk()
window.title("To Do List")
window.config(padx=50, pady=50)

tasks = []

def add_task():
    task = entry.get()
    tasks.append(task)
    listbox.insert(tk.END, task)
    entry.delete(0, tk.END)

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        listbox.delete(selected_task)

def clear_tasks():
    tasks.clear()
    listbox.delete(0, tk.END)
    
def show_tasks():
    for task in tasks:
        listbox.insert(tk.END, task)
    listbox.pack()



     

entry = tk.Entry(window, width=30)
entry.pack(pady=10)

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=10)

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=10)

clear_button = tk.Button(window, text="Clear Tasks", command=clear_tasks)
clear_button.pack(pady=10)



listbox = tk.Listbox(window, width=30)
listbox.pack(pady=10)

show_tasks()
window.mainloop()