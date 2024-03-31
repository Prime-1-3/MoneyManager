from file_handling import FileHandling
from tkinter import *


class ShowInfo:
    def __init__(self, window):
        self.data = FileHandling()
        self.window = window
        self.frame2 = Frame(window, bg='#008DDA')
        self.frame2.place(x=300, y=430, width=210, height=148)
        self.frame3 = Frame(window, bg='#BFEA7C')
        self.frame3.place(x=574, y=430, width=239, height=148)
        self.frame4 = Frame(window, bg='#FF8911')
        self.frame4.place(x=870, y=430, width=239, height=148)
        self.update_balance_labels()

    def update_balance_labels(self):
        income_data, expenses_data = self.data.calculate_income_expenses()
        total_income = sum(income_data.values())
        total_expenses = sum(expenses_data.values())
        self.total_balance = total_income - total_expenses

    def display_balance_labels(self):
        total_balance_label = Label(self.frame2, font=("", 14, "bold"), bg='#008DDA')
        total_balance_label.place(x=36, y=20)
        total_balance_label.config(text='Total Balance\n\n', fg='#FBA834')
        balance_text = f'{self.total_balance}'
        balance_label = Label(self.frame2, text=balance_text, font=("", 28, "bold"), fg='#9CFF2E', bg='#008DDA')
        balance_label.place(x=33, y=60)

# Your other methods go here

