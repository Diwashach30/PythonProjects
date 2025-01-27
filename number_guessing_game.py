##number guessing game using GUI

from tkinter import *
from random import randint
from tkinter import messagebox  
import time

def start():
    global num
    num = randint(1,100)
    print(num)
    
def guess():
    global num
    guess = int(entry.get())
    if guess == num:
        messagebox.showinfo("Result","You guessed it right")
    elif guess > num:
        messagebox.showinfo("Result","Too high")
    else:
        messagebox.showinfo("Result","Too low"),
        time.sleep(2)
    entry.delete(0,END)
    
window = Tk()
window.title("Number Guessing Game")
window.geometry("400x200")

window.configure(bg="lightblue")

label = Label(window,text="Enter any number",font=("Arial",20),bg="lightblue")
label.pack(pady=10)

entry = Entry(window,font=("Arial",20),width=15)
entry.pack(pady=10)

button = Button(window,text="Start",font=("Arial",20),command=start , width=6)
button.pack(pady=10)

button1 = Button(window,text="Guess",font=("Arial",20),command=guess , width=6)   
button1.pack(pady=10)  


window.mainloop()
