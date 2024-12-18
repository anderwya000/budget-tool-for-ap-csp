import tkinter as tk
import json
import datetime
import re

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_pies():
    global income_costs
    global expenses_costs
    # Update income plot
    income_costs = [salary.get(), gifts.get(), side_hustles.get(), passive.get()]
    income_plot.clear()
    income_plot.pie(income_costs, radius=1, labels=income_list, autopct='%1.2f%%', shadow=True, textprops={'fontsize': 2.8})
    income_plot.draw(income_chart.renderer)
    fig.canvas.draw()
    expenses_costs = [rent.get(), transport.get(), food.get(), investments.get(), entertainment.get(), savings.get(), other.get()]
    expenses_plot.clear()
    expenses_plot.pie(expenses_costs, radius=1, labels=expenses_list, autopct='%1.2f%%', shadow=True, textprops={'fontsize': 2.8})
    expenses_plot.draw(income_chart.renderer)
    fig1.canvas.draw()

    root.after(10, update_pies)

def update_comparisons():
    income_costs = [salary.get(), gifts.get(), side_hustles.get(), passive.get(), investments.get()]
    income_label.configure(text=f'Income: ${sum(income_costs)}')
    expenses_costs = [rent.get(), transport.get(), food.get(), entertainment.get(), savings.get(), other.get()]
    expenses_label.configure(text=f'Expenses: ${sum(expenses_costs)}')
    expenses_colors()

    root.after(10, update_comparisons)


def expenses_colors():
    expenses_costs = [rent.get(), transport.get(), food.get(), investments.get(), entertainment.get(), savings.get(), other.get()]
    income_costs = [salary.get(), gifts.get(), side_hustles.get(), passive.get()]
    total_income = sum(income_costs)
    total_expenses = sum(expenses_costs)

    if total_expenses > total_income:
        for label in expenses_labels:
            label.config(fg='red')
    else:
        for label in expenses_labels:
            label.config(fg='#000000')


def str_to_float(string: str) -> float:
    try:
        float(string)
        return float(string)
    except ValueError:
        return float(0)


def first_load():
    global data
    try:
        with open('data.json', 'r') as file:
            json_data = file.read()
            data = json.loads(json_data)
    except FileNotFoundError:
        with open('data.json', 'w') as file:
            file.write('{"income":{"salary":100.0,"gifts":100.0,"side hustles":100.0,"passive":100.0},"expenses":{"rent":100.0,"transport":100.0,"food":100.0,"investments":100.0,"savings":100.0,"entertainment":100.0,"other":100.0}}')
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
    rent.set(data['expenses']['rent'])
    transport.set(data['expenses']['transport'])
    food.set(data['expenses']['food'])
    investments.set(data['expenses']['investments'])
    entertainment.set(data['expenses']['entertainment'])
    savings.set(data['expenses']['savings'])
    other.set(data['expenses']['other'])
    global income_costs
    global expenses_costs
    income_costs = [salary.get(), gifts.get(), side_hustles.get(), passive.get()]
    expenses_costs = [rent.get(), transport.get(), food.get(), investments.get(), entertainment.get(), savings.get(), other.get()]


def save():
    global data
    data = {'income': {'salary': salary.get(), 'gifts': gifts.get(), 'side hustles': side_hustles.get(), 'passive': passive.get()}, 'expenses': {'rent': rent.get(), 'transport': transport.get(), 'food': food.get(), 'investments': investments.get(), 'savings': savings.get(), 'entertainment': entertainment.get(), 'other': other.get()}}
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)


def export():
    global data
    data = {'income': {'salary': salary.get(), 'gifts': gifts.get(), 'side hustles': side_hustles.get(), 'passive': passive.get()}, 'expenses': {'rent': rent.get(), 'transport': transport.get(), 'food': food.get(), 'investments': investments.get(), 'savings': savings.get(), 'entertainment': entertainment.get(), 'other': other.get()}}
    name = datetime.datetime.today().strftime('%Y-%m-%d %H-%M-%S')
    with open(f'{name}.json', 'w') as file:
        json.dump(data, file, indent=2)


def validate_input(action, value, widget_name):
    try:
        widget = root.nametowidget(widget_name)
        if value == '':
            widget.configure(validate='none')
            widget.delete(0, tk.END)
            widget.insert(0, '0')
            widget.configure(validate='key')
            return False
        if re.match(r"^0\d+$", value):
            corrected_value = value.lstrip("0")
            widget.configure(validate='none')
            widget.delete(0, tk.END)
            widget.insert(0, corrected_value)
            widget.configure(validate='key')
            if corrected_value == '':
                widget.configure(validate='none')
                widget.delete(0, tk.END)
                widget.insert(0, '0')
                widget.configure(validate='key')
            return False
        if float(value) >= 0:
            return True
    except ValueError:
        return False
    return False

first_load()
root = tk.Tk()

bold_font = tk.font.Font(family='Segoe UI', size=9, weight='bold')

root.geometry('600x600')
root.configure(background='#FFFFFF')
root.title('Budget Calculator')

vcmd = (root.register(validate_input), '%d', '%P', '%W')

title = tk.Label(root, text='Budget Calculator', font=('helvetica', 22, 'bold'), bg='#FFFFFF', anchor='center')
title.grid(row=0, column=0, columnspan=3,padx=15, pady=15)

income_inputs = tk.Listbox(root)
income_inputs.grid(row=1, column=0, padx=10, sticky=tk.NS)

expenses_inputs = tk.Listbox(root)
expenses_inputs.grid(row=1, column=1, padx=10, sticky=tk.NS)

salary = tk.DoubleVar()
salary.set(data['income']['salary'])
gifts = tk.DoubleVar()
gifts.set(data['income']['gifts'])
side_hustles = tk.DoubleVar()
side_hustles.set(data['income']['side hustles'])
passive = tk.DoubleVar()
passive.set(data['income']['passive'])

income_list = ['Salary', 'Side Hustles', 'Gifts', 'Passive']
income_costs = [salary.get(), side_hustles.get(), gifts.get(), passive.get()]

fig = Figure(figsize=(1,1), dpi=300)

income_plot = fig.add_subplot(111)
income_plot.pie(income_costs, radius=1, labels=income_list, autopct='%1.2f%%', shadow=True, textprops={'fontsize': 2.8})

income_chart = FigureCanvasTkAgg(fig, root)
income_chart.draw()
income_chart.get_tk_widget().grid(row=2, column=0)

rent = tk.DoubleVar()
rent.set(data['expenses']['rent'])
transport = tk.DoubleVar()
transport.set(data['expenses']['transport'])
food = tk.DoubleVar()
food.set(data['expenses']['food'])
investments = tk.DoubleVar()
investments.set(data['expenses']['investments'])
entertainment = tk.DoubleVar()
entertainment.set(data['expenses']['entertainment'])
savings = tk.DoubleVar()
savings.set(data['expenses']['savings'])
other = tk.DoubleVar()
other.set(data['expenses']['other'])

expenses_list = ['Rent', 'Transportation', 'Food', 'Investments', 'Entertainment', 'Saving', 'Other']
expenses_costs = [rent.get(), transport.get(), food.get(), investments.get(), entertainment.get(), savings.get(), other.get()]

fig1 = Figure(figsize=(1,1), dpi=300)

expenses_plot = fig1.add_subplot(111)
expenses_plot.pie(expenses_costs, radius=1, labels=expenses_list, autopct='%1.2f%%', shadow=True, textprops={'fontsize': 2.8})

expenses_chart = FigureCanvasTkAgg(fig1, root)
expenses_chart.draw()
expenses_chart.get_tk_widget().grid(row=2, column=1)

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

filler_element = tk.Label(income_inputs, bg='#FFFFFF')
filler_element.grid(row=6, column=0)

filler_element1 = tk.Label(income_inputs, bg='#FFFFFF')
filler_element1.grid(row=6, column=1)

filler_element2 = tk.Label(income_inputs, bg='#FFFFFF')
filler_element2.grid(row=7, column=0)

filler_element3 = tk.Label(income_inputs, bg='#FFFFFF')
filler_element3.grid(row=5, column=1)

filler_element4 = tk.Label(income_inputs, bg='#FFFFFF')
filler_element4.grid(row=5, column=1)

income_save = tk.Button(income_inputs, text='Save', command=save)
income_save.grid(row=8, column=0, pady=3, sticky='wes')
income_load = tk.Button(income_inputs, text='Load', command=load)
income_load.grid(row=8, column=1, pady=3, sticky='wes')
income_export = tk.Button(income_inputs, text='Export', command=export)
income_export.grid(row=9, column=0, columnspan=2, pady=3, sticky='wes')

expenses_label = tk.Label(expenses_inputs, text='Expenses', bg='#FFFFFF', font=bold_font)
expenses_label.grid(row=0, column=0, columnspan=2)

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

investments_label = tk.Label(expenses_inputs, text='Investments: ', bg='#FFFFFF')
investments_label.grid(row=4, column=0)
investments_input = tk.Entry(expenses_inputs, textvariable=investments, validate='key', validatecommand=vcmd, width=10)
investments_input.grid(row=4, column=1)

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

expenses_labels = [rent_label, rent_input, transport_label, transport_input, food_label, food_input, investments_label, investments_input, entertainment_label, entertainment_input, savings_label, savings_input, other_label, other_input, expenses_label]

expenses_save = tk.Button(expenses_inputs, text='Save', command=save)
expenses_save.grid(row=8, column=0, pady=3, sticky='wes')
expenses_load = tk.Button(expenses_inputs, text='Load', command=load)
expenses_load.grid(row=8, column=1, pady=3, sticky='wes')
expenses_export = tk.Button(expenses_inputs, text='Export', command=export)
expenses_export.grid(row=9, column=0, columnspan=2, pady=3, sticky='wes')

update_pies()
update_comparisons()

root.mainloop()
