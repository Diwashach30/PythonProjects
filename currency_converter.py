#creating a currency converter project using GUI in python.

import tkinter as tk
from tkinter import messagebox
from tkinter import *

window = tk.Tk()
window.title("Currency Converter")
window.config(padx=50, pady=50)

def convert_currency():
    try:
        amount = float(entry.get())
        rate = float(rate_entry.get())
        converted_amount = amount * rate
        result_label.config(text=f"{amount} USD = {converted_amount} RS")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

label = Label(window, text="Enter the amount in USD:")
label.pack()

entry = Entry(window)
entry.pack()

label2 = Label(window, text="Enter the exchange rate:")
label2.pack()

rate_entry = Entry(window)
rate_entry.pack()

button = Button(window, text="Convert", command=convert_currency)
button.pack()

result_label = Label(window, text="")
result_label.pack()

window.mainloop()