import tkinter as tk
import json
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


def str_to_float(string: str) -> float:
    try:
        float(string)
        return float(string)
    except ValueError:
        return float(0)


def load():
    global data
    with open('data.json', 'r') as file:
        json_data = file.read()
        data = json.loads(json_data)

def save():
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)


def validate_numeric_input(action, value):
    if action != '1':
        return True
    try:
        if value == '' or float(value) >= 0:
            return True
    except ValueError:
        return False

    return False

load()
save()
root = tk.Tk()

# Make main window.
root.geometry('900x600')
root.configure(background='#FFFFFF')
root.title('Budget Calculator')

vcmd = (root.register(validate_numeric_input), '%d', '%P')

title = tk.Label(root, text='Budget Calculator', font=('helvetica', 22, 'bold'), bg='#FFFFFF', anchor='center')
title.grid(row=0, column=0, padx=15, pady=15)

income_inputs = tk.Listbox(root)
income_inputs.grid(row=1, column=0, padx=15, pady=15)

expenses_inputs = tk.Listbox(root)
expenses_inputs.grid(row=2, column=0, padx=15, pady=15)

# Income variables
salary = tk.DoubleVar()
salary.set(data['income']['salary'])
gifts = tk.DoubleVar()
gifts.set(data['income']['gifts'])
side_hustles = tk.DoubleVar()
side_hustles.set(data['income']['side hustles'])
passive = tk.DoubleVar()
passive.set(data['income']['passive'])
investments = tk.DoubleVar()
investments.set(data['income']['investments'])

# Expenses variables
rent = tk.DoubleVar()
rent.set(data['expenses']['rent'])
transport = tk.DoubleVar()
transport.set(data['expenses']['transport'])
food = tk.DoubleVar()
food.set(data['expenses']['food'])
health = tk.DoubleVar()
health.set(data['expenses']['health'])
entertainment = tk.DoubleVar()
entertainment.set(data['expenses']['entertainment'])
savings = tk.DoubleVar()
savings.set(data['expenses']['savings'])
other = tk.DoubleVar()
other.set(data['expenses']['other'])

# Income
salary_label = tk.Label(income_inputs, text='Salary: ', bg='#FFFFFF')
salary_label.grid(row=0, column=0)
salary_input = tk.Entry(income_inputs, textvariable=salary, validate='key', validatecommand=vcmd)
salary_input.grid(row=0, column=1)

gifts_label = tk.Label(income_inputs, text='Gifts: ', bg='#FFFFFF')
gifts_label.grid(row=1, column=0)
gifts_input = tk.Entry(income_inputs, textvariable=gifts, validate='key', validatecommand=vcmd)
gifts_input.grid(row=1, column=1)

side_hustles_label = tk.Label(income_inputs, text='Side Hustles: ', bg='#FFFFFF')
side_hustles_label.grid(row=2, column=0)
side_hustles_input = tk.Entry(income_inputs, textvariable=side_hustles, validate='key', validatecommand=vcmd)
side_hustles_input.grid(row=2, column=1)

passive_label = tk.Label(income_inputs, text='Passive: ', bg='#FFFFFF')
passive_label.grid(row=3, column=0)
passive_input = tk.Entry(income_inputs, textvariable=passive, validate='key', validatecommand=vcmd)
passive_input.grid(row=3, column=1)

investments_label = tk.Label(income_inputs, text='Investments: ', bg='#FFFFFF')
investments_label.grid(row=4, column=0)
investments_input = tk.Entry(income_inputs, textvariable=investments, validate='key', validatecommand=vcmd)
investments_input.grid(row=4, column=1)
# Expenses
rent_label = tk.Label(expenses_inputs, text='Rent: ', bg='#FFFFFF')
rent_label.grid(row=0, column=0)
rent_input = tk.Entry(expenses_inputs, textvariable=rent, validate='key', validatecommand=vcmd)
rent_input.grid(row=0, column=1)

transport_label = tk.Label(expenses_inputs, text='Transportation: ', bg='#FFFFFF')
transport_label.grid(row=1, column=0)
transport_input = tk.Entry(expenses_inputs, textvariable=transport, validate='key', validatecommand=vcmd)
transport_input.grid(row=1, column=1)

food_label = tk.Label(expenses_inputs, text='Food: ', bg='#FFFFFF')
food_label.grid(row=2, column=0)
food_input = tk.Entry(expenses_inputs, textvariable=food, validate='key', validatecommand=vcmd)
food_input.grid(row=2, column=1)

health_label = tk.Label(expenses_inputs, text='Healthcare: ', bg='#FFFFFF')
health_label.grid(row=3, column=0)
health_input = tk.Entry(expenses_inputs, textvariable=health, validate='key', validatecommand=vcmd)
health_input.grid(row=3, column=1)

entertainment_label = tk.Label(expenses_inputs, text='Entertainment: ', bg='#FFFFFF')
entertainment_label.grid(row=4, column=0)
entertainment_input = tk.Entry(expenses_inputs, textvariable=entertainment, validate='key', validatecommand=vcmd)
entertainment_input.grid(row=4, column=1)

savings_label = tk.Label(expenses_inputs, text='Saving: ', bg='#FFFFFF')
savings_label.grid(row=5, column=0)
savings_input = tk.Entry(expenses_inputs, textvariable=savings, validate='key', validatecommand=vcmd)
savings_input.grid(row=5, column=1)

other_label = tk.Label(expenses_inputs, text='Other: ', bg='#FFFFFF')
other_label.grid(row=6, column=0)
other_input = tk.Entry(expenses_inputs, textvariable=other, validate='key', validatecommand=vcmd)
other_input.grid(row=6, column=1)

root.mainloop()