import json
import termcharts
from rich import print


def strtofloat(str: str) -> float:
    try:
        float(str)
        return float(str)
    except ValueError:
        return float(0)


def setup():
    print('Welcome!')
    name = input('Please enter your name:')
    total_budget = input('Please enter your budget:')
    if strtofloat(total_budget) == 0:
        print('That is not a number. Please try again.')
    elif strtofloat(total_budget) != 0:
        total_budget = strtofloat(total_budget)
    else:
        print('Error. Please try again.')
    data = {'been_used': True, 'name': name, 'total_budget': total_budget, 'payments': []}
    print(data)
    with open('data.json', 'w') as file:
        json.dump(data, file)


def print_spending():
    chart_data = {}
    for i in range(len(data['payments'])):
        chart_data[data['payments'][i]['item']] = data['payments'][i]['cost']
        chart = termcharts.pie(chart_data, title = 'Spending', rich = True)
    print(chart)


def main():
    name = data['name']
    total_budget = data['total_budget']
    total_paid = 0
    for i in range(len(data['payments'])):
        total_paid = total_paid +  data['payments'][i]['cost']
    print('Welcome, ' + name + '!')
    print('Your total budget is $' + str(total_budget))
    print('You have $' + str(total_budget - total_paid) + ' remaining.')
    print('You have spent $' + str(total_paid))
    if input('Would you like record some spending? Y/n ') != 'n':
        record_spending()
    elif input('Would you like view your spending? Y/n ') != 'n':
        print_spending()


def record_spending():
    what_spent_on = input('What did you buy?:')
    amount_spent = input('How much did it cost?:')
    if strtofloat(amount_spent) == 0:
        print('That is not a number. Please try again.')
    elif strtofloat(amount_spent) != 0:
        amount_spent = strtofloat(amount_spent)
    else:
        print('Error. Please try again.')
    spending = {'item': what_spent_on, 'amount': amount_spent}
    data['payments'].append(spending)
    with open('data.json', 'w') as file:
        json.dump(data, file)
    main()
    
    


with open('data.json', 'r') as file:
    json_data = file.read()
    data = json.loads(json_data)
if data['been_used']:
    main()
elif not(data['been_used']):
    setup()