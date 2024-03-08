from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import pytz

def get_bangladesh_time():
    bangladesh_time = datetime.now(pytz.timezone('Asia/Dhaka'))
    return bangladesh_time.strftime("%I:%M %p")

def get_greeting():
    current_hour = datetime.now(pytz.timezone('Asia/Dhaka')).hour
    if 6 <= current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 17:
        return "Good Afternoon"
    elif 17 <= current_hour < 20:
        return "Good Evening"
    elif 20 <= current_hour < 24:
        return "Good Night"
    else:
        return "Good Night"

def calculate_income_expenses():
    # This function should fetch the data for income and expenses dynamically
    # For this example, I'll return static sample data
    income_data = {'Salary': 4000, 'Freelance': 1500, 'Investment': 800, 'Other': 200}
    expenses_data = {'Rent': 1000, 'Food': 600, 'Transport': 400, 'Entertainment': 300, 'Others': 300}
    return income_data, expenses_data

def win():
    window = Tk()
    window.title('Money Manager')
    window.geometry('1200x1000')
    window.state('zoomed')
    window.config(background='#170422')

    # Header
    header = Frame(window, bg='#C07BB5')
    header.place(x=300, y=0, width=1275, height=60)
    pacifico_font = ("Pacifico", 22)  # Specify "Pacifico" font

    # Greeting text (in red)
    greeting_text = Label(header, text=f"{get_greeting()}", font=("Pacifico", 19, "bold"), fg='#1789CA', bg='#C07BB5')
    greeting_text.place(x=562, y=1)

    # Time text (in blue)
    time_text = f'It\'s {get_bangladesh_time()}'
    time_label = Label(header, text=time_text, font=("Pacifico", 19, "bold"), fg='#0000FF', bg='#C07BB5')
    time_label.place(x=1080, y=1)

    # Profile
    filename = r"D:\New folder\images\avatar_7235981.png"
    img = Image.open(filename)
    photo = ImageTk.PhotoImage(img)
    logo = Label(header, image=photo, bg='red')
    logo.image = photo
    logo.place(x=30, y=1)

    # User name
    cname = Label(header, text='Ratin Sharafat', fg='#BD2EEF', bg='#C07BB5', font=("", 15, "bold"))
    cname.place(x=110, y=20)

    # Sidebar
    sidebar = Frame(window, bg='#1C1221')
    sidebar.place(x=0, y=0, width=300, height=750)

    # Body
    heading = Label(window, text='Dashboard', font=("", 13, "bold"), fg='#0064d3', bg='#170422')
    heading.place(x=325, y=70)

    # Frame 1
    frame1 = Frame(window, bg='#7CCEC9')
    frame1.place(x=328, y=110, width=1250, height=350)

    # Calculate income and expenses
    income_data, expenses_data = calculate_income_expenses()

    # Pie Chart for Income
    fig_income, ax_income = plt.subplots()
    labels_income = list(income_data.keys())
    sizes_income = list(income_data.values())
    ax_income.pie(sizes_income, labels=labels_income, autopct='%1.1f%%', startangle=90)
    ax_income.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    ax_income.set_title('Income Details')  # Add title to the pie chart
    canvas_income = FigureCanvasTkAgg(fig_income, master=frame1)
    canvas_income.draw()
    canvas_income.get_tk_widget().pack(side=LEFT, padx=10, pady=10)

    # Frame 2
    frame2 = Frame(window, bg='#F6636B')
    frame2.place(x=328, y=495, width=310, height=220)

    # Label for "Total Users"
    total_users_label = Label(frame2, text='Total Users', font=("", 19, "bold"), fg='#5154A1', bg='#F6636B')
    total_users_label.place(x=90, y=20)

    # Label for total count
    total_count_label = Label(frame2, text='100', font=("", 25, "bold"), fg='#2ACF94', bg='#F6636B')
    total_count_label.place(x=150, y=110, anchor=CENTER)

    # Frame 3
    frame3 = Frame(window, bg='#EA2EFB')
    frame3.place(x=780, y=495, width=310, height=220)

    # Calculate the most income-earning source
    most_income_source = max(income_data, key=income_data.get)
    most_income_amount = income_data[most_income_source]

    # Display the most income-earning source and its amount
    most_income_label = Label(frame3, text=f"Most Income Source\n{most_income_source}\n\nAmount: {most_income_amount}",
                              font=("bold", 19), fg='blue', bg='#EA2EFB')
    most_income_label.place(x=150, y=90, anchor=CENTER)

    # Pie Chart for Expenses
    fig_expenses, ax_expenses = plt.subplots()
    labels_expenses = list(expenses_data.keys())
    sizes_expenses = list(expenses_data.values())
    ax_expenses.pie(sizes_expenses, labels=labels_expenses, autopct='%1.1f%%', startangle=90)
    ax_expenses.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    ax_expenses.set_title('Expenses Details')  # Add title to the pie chart
    canvas_expenses = FigureCanvasTkAgg(fig_expenses, master=frame1)
    canvas_expenses.draw()
    canvas_expenses.get_tk_widget().pack(side=RIGHT, padx=10, pady=10)

    # Frame 4
    frame4 = Frame(window, bg='#3462D9')
    frame4.place(x=1270, y=495, width=310, height=220)

    # Calculate the most expense source
    most_expense_source = max(expenses_data, key=expenses_data.get)
    most_expense_amount = expenses_data[most_expense_source]

    # Display the most expense source and its amount
    most_expense_label = Label(frame4,
                               text=f"Most Expense Source:\n{most_expense_source}\n\nAmount: {most_expense_amount}",
                               font=("bold", 19), fg='#FFFFFF', bg='#3462D9')
    most_expense_label.place(x=150, y=90, anchor=CENTER)

    window.mainloop()

if __name__ == '__main__':
    win()
