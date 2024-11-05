import tkinter as tk
import json
from tkinter import ttk


def str_to_float(string: str) -> float:
    try:
        float(string)
        return float(string)
    except ValueError:
        return float(0)


def main():
    with open('data.json', 'r') as file:
        json_data = file.read()
        data = json.loads(json_data)
    name = data['name']
    total_budget = data['total_budget']
    total_paid = 0
    for i in range(len(data['payments'])):
        total_paid = total_paid + data['payments'][i]['cost']


root = tk.Tk()

# Make main window.
root.geometry('800x500')
root.configure(background='#FFFFFF')
root.title('Budget Calculator')

title = tk.Label(root, text='Budget Calculator', font=('helvetica', 22, 'bold'), bg='#FFFFFF', anchor='center')
title.grid(row=0, column=0, padx=15, pady=15)

items_list = tk.Listbox(root, )
items_list.grid(row=1, rowspan=5, column=0, padx=15, pady=15)


root.mainloop()