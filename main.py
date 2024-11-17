import tkinter as tk
import json
import matplotlib as mpl
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

def str_to_float(string: str) -> float:
    try:
        float(string)
        return float(string)
    except ValueError:
        return float(0)

def first_load():
    global data
    with open('data.json', 'r') as file:
        json_data = file.read()
        data = json.loads(json_data)


def load():
    global data
    with open('data.json', 'r') as file:
        json_data = file.read()
        data = json.loads(json_data)
    salary.set(data['income']['salary'])
    gifts.set(data['income']['gifts'])
    side_hustles.set(data['income']['side hustles'])
    passive.set(data['income']['passive'])
    investments.set(data['income']['investments'])
    rent.set(data['expenses']['rent'])
    transport.set(data['expenses']['transport'])
    food.set(data['expenses']['food'])
    health.set(data['expenses']['health'])
    entertainment.set(data['expenses']['entertainment'])
    savings.set(data['expenses']['savings'])
    other.set(data['expenses']['other'])
    global income_costs
    global expenses_costs
    income_costs = [salary.get(), gifts.get(), side_hustles.get(), passive.get(), investments.get()]
    expenses_costs = [rent.get(), transport.get(), food.get(), health.get(), entertainment.get(), savings.get(), other.get()]


def save():
    global data
    data = {'income': {'salary': salary.get(), 'gifts': gifts.get(), 'side hustles': side_hustles.get(), 'passive': passive.get(), 'investments': investments.get()}, 'expenses': {'rent': rent.get(), 'transport': transport.get(), 'food': food.get(), 'health': health.get(), 'savings': savings.get(), 'entertainment': entertainment.get(), 'other': other.get()}}
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)
    global income_costs
    global expenses_costs
    # Update income plot
    income_costs = [salary.get(), gifts.get(), side_hustles.get(), passive.get(), investments.get()]
    income_plot.clear()
    income_plot.pie(income_costs, radius=1, labels=income_list, autopct='%1.2f%%', shadow=True, textprops={'fontsize': 2.8})
    income_plot.draw(income_chart.renderer)
    fig.canvas.draw()
    # Update expenses plot
    expenses_costs = [rent.get(), transport.get(), food.get(), health.get(), entertainment.get(), savings.get(), other.get()]
    expenses_plot.clear()
    expenses_plot.pie(expenses_costs, radius=1, labels=expenses_list, autopct='%1.2f%%', shadow=True, textprops={'fontsize': 2.8})
    expenses_plot.draw(income_chart.renderer)
    fig1.canvas.draw()


def validate_numeric_input(action, value):
    if action != '1':
        return True
    try:
        if value == '' or float(value) >= 0:
            return True
    except ValueError:
        return False

    return False

first_load()
root = tk.Tk()

bold_font = tk.font.Font(family='Segoe UI', size=9, weight='bold')

# Make main window.
root.geometry('900x600')
root.configure(background='#FFFFFF')
root.title('Budget Calculator')

vcmd = (root.register(validate_numeric_input), '%d', '%P')

title = tk.Label(root, text='Budget Calculator', font=('helvetica', 22, 'bold'), bg='#FFFFFF', anchor='center')
title.grid(row=0, column=0, columnspan=3,padx=15, pady=15)

income_inputs = tk.Listbox(root)
income_inputs.grid(row=1, column=0, padx=10, sticky=tk.NS)

expenses_inputs = tk.Listbox(root)
expenses_inputs.grid(row=1, column=1, padx=10, sticky=tk.NS)

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

income_list = ['Salary', 'Side Hustles', 'Gifts', 'Passive', 'Investments']
income_costs = [salary.get(), side_hustles.get(), gifts.get(), passive.get(), investments.get()]

fig = Figure(figsize=(1,1), dpi=300)

income_plot = fig.add_subplot(111)
income_plot.pie(income_costs, radius=1, labels=income_list, autopct='%1.2f%%', shadow=True, textprops={'fontsize': 2.8})

income_chart = FigureCanvasTkAgg(fig, root)
income_chart.draw()
income_chart.get_tk_widget().grid(row=2, column=0)

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

expenses_list = ['Rent', 'Transportation', 'Food', 'Health', 'Entertainment', 'Saving', 'Other']
expenses_costs = [rent.get(), transport.get(), food.get(), health.get(), entertainment.get(), savings.get(), other.get()]

fig1 = Figure(figsize=(1,1), dpi=300)

expenses_plot = fig1.add_subplot(111)
expenses_plot.pie(expenses_costs, radius=1, labels=expenses_list, autopct='%1.2f%%', shadow=True, textprops={'fontsize': 2.8})

expenses_chart = FigureCanvasTkAgg(fig1, root)
expenses_chart.draw()
expenses_chart.get_tk_widget().grid(row=2, column=1)

# Income
income_label = tk.Label(income_inputs, text='Income', bg='#FFFFFF', font=bold_font)
income_label.grid(row=0, column=0, columnspan=2)

salary_label = tk.Label(income_inputs, text='Salary: ', bg='#FFFFFF', width=12)
salary_label.grid(row=1, column=0)
salary_input = tk.Entry(income_inputs, textvariable=salary, validate='key', validatecommand=vcmd, width=10)
salary_input.grid(row=1, column=1)

side_hustles_label = tk.Label(income_inputs, text='Side Hustles: ', bg='#FFFFFF')
side_hustles_label.grid(row=2, column=0)
side_hustles_input = tk.Entry(income_inputs, textvariable=side_hustles, validate='key', validatecommand=vcmd, width=10)
side_hustles_input.grid(row=2, column=1)

gifts_label = tk.Label(income_inputs, text='Gifts: ', bg='#FFFFFF')
gifts_label.grid(row=3, column=0)
gifts_input = tk.Entry(income_inputs, textvariable=gifts, validate='key', validatecommand=vcmd, width=10)
gifts_input.grid(row=3, column=1)

passive_label = tk.Label(income_inputs, text='Passive: ', bg='#FFFFFF')
passive_label.grid(row=4, column=0)
passive_input = tk.Entry(income_inputs, textvariable=passive, validate='key', validatecommand=vcmd, width=10)
passive_input.grid(row=4, column=1)

investments_label = tk.Label(income_inputs, text='Investments: ', bg='#FFFFFF')
investments_label.grid(row=5, column=0)
investments_input = tk.Entry(income_inputs, textvariable=investments, validate='key', validatecommand=vcmd, width=10)
investments_input.grid(row=5, column=1)

filler_element = tk.Label(income_inputs, bg='#FFFFFF')
filler_element.grid(row=6, column=0)

filler_element1 = tk.Label(income_inputs, bg='#FFFFFF')
filler_element1.grid(row=6, column=1)

filler_element2 = tk.Label(income_inputs, bg='#FFFFFF')
filler_element2.grid(row=7, column=0)

filler_element3 = tk.Label(income_inputs, bg='#FFFFFF')
filler_element3.grid(row=7, column=1)

income_save = tk.Button(income_inputs, text="Save", command=save)
income_save.grid(row=8, column=0, pady=3, sticky=tk.S)
income_load = tk.Button(income_inputs, text="Load", command=load)
income_load.grid(row=8, column=1, pady=3, sticky=tk.S)

# Expenses
income_label = tk.Label(expenses_inputs, text='Expenses', bg='#FFFFFF', font=bold_font)
income_label.grid(row=0, column=0, columnspan=2)

rent_label = tk.Label(expenses_inputs, text='Rent: ', bg='#FFFFFF', width=12)
rent_label.grid(row=1, column=0)
rent_input = tk.Entry(expenses_inputs, textvariable=rent, validate='key', validatecommand=vcmd, width=10)
rent_input.grid(row=1, column=1)

transport_label = tk.Label(expenses_inputs, text='Transportation: ', bg='#FFFFFF')
transport_label.grid(row=2, column=0)
transport_input = tk.Entry(expenses_inputs, textvariable=transport, validate='key', validatecommand=vcmd, width=10)
transport_input.grid(row=2, column=1)

food_label = tk.Label(expenses_inputs, text='Food: ', bg='#FFFFFF')
food_label.grid(row=3, column=0)
food_input = tk.Entry(expenses_inputs, textvariable=food, validate='key', validatecommand=vcmd, width=10)
food_input.grid(row=3, column=1)

health_label = tk.Label(expenses_inputs, text='Health: ', bg='#FFFFFF')
health_label.grid(row=4, column=0)
health_input = tk.Entry(expenses_inputs, textvariable=health, validate='key', validatecommand=vcmd, width=10)
health_input.grid(row=4, column=1)

entertainment_label = tk.Label(expenses_inputs, text='Entertainment: ', bg='#FFFFFF')
entertainment_label.grid(row=5, column=0)
entertainment_input = tk.Entry(expenses_inputs, textvariable=entertainment, validate='key', validatecommand=vcmd, width=10)
entertainment_input.grid(row=5, column=1)

savings_label = tk.Label(expenses_inputs, text='Saving: ', bg='#FFFFFF')
savings_label.grid(row=6, column=0)
savings_input = tk.Entry(expenses_inputs, textvariable=savings, validate='key', validatecommand=vcmd, width=10)
savings_input.grid(row=6, column=1)

other_label = tk.Label(expenses_inputs, text='Other: ', bg='#FFFFFF')
other_label.grid(row=7, column=0)
other_input = tk.Entry(expenses_inputs, textvariable=other, validate='key', validatecommand=vcmd, width=10)
other_input.grid(row=7, column=1)

expenses_save = tk.Button(expenses_inputs, text="Save", command=save)
expenses_save.grid(row=8, column=0, pady=3, sticky=tk.S)
expenses_load = tk.Button(expenses_inputs, text="Load", command=load)
expenses_load.grid(row=8, column=1, pady=3, sticky=tk.S)

root.mainloop()