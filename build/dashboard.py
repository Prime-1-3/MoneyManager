from datetime import datetime, timedelta
from pathlib import Path
from tkinter import *
import os
import csv

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\dashboard")
filename = OUTPUT_PATH / Path("data.csv")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def execute_python_file(file_path):
    try:
        os.system(f'python {file_path}')
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")


def switch_login():
    window.destroy()
    execute_python_file(OUTPUT_PATH / Path("login.py"))


def switch_income():
    window.destroy()
    execute_python_file(OUTPUT_PATH / Path("income.py"))


def switch_expense():
    window.destroy()
    execute_python_file(OUTPUT_PATH / Path("expense.py"))


def switch_summery():
    window.destroy()
    execute_python_file(OUTPUT_PATH / Path("summery.py"))


def get_bangladesh_time():
    bangladesh_time = datetime.utcnow() + timedelta(hours=6)  # Adding 6 hours for Bangladesh time
    return bangladesh_time.strftime("%I:%M %p")


def get_greeting():
    current_hour = (datetime.utcnow() + timedelta(hours=6)).hour  # Adding 6 hours for Bangladesh time
    if 6 <= current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 15:
        return "Good Noon"
    elif 15 <= current_hour < 17:
        return "Good Afternoon"
    elif 17 <= current_hour < 20:
        return "Good Evening"
    elif 20 <= current_hour < 24:
        return "Good Night"


def calculate_income_expenses(csv_file):
    income_data = {}
    expenses_data = {}

    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            flag = int(row['flag'])
            source = row['Source']
            amount = float(row['Amount'])

            if flag == 0:  # Expense
                expenses_data[source] = amount
            elif flag == 1:  # Income
                income_data[source] = amount

    # Sort the dictionaries by value in descending order
    sorted_income_data = dict(sorted(income_data.items(), key=lambda item: item[1], reverse=True))
    sorted_expenses_data = dict(sorted(expenses_data.items(), key=lambda item: item[1], reverse=True))

    # Keep the top 4 categories for expenses and sum the rest for "Others"
    top_expenses = dict(list(sorted_expenses_data.items())[:4])
    other_expenses = sum(list(sorted_expenses_data.values())[4:])
    top_expenses['Others'] = other_expenses

    # Keep the top 4 categories for income and sum the rest for "Others"
    top_income = dict(list(sorted_income_data.items())[:4])
    other_income = sum(list(sorted_income_data.values())[4:])
    top_income['Others'] = other_income

    return top_income, top_expenses


def draw_pie_chart(canvas, data, title, x, y, radius, colors):
    total = sum(data.values())
    start_angle = 0

    for category, value, color in zip(data.keys(), data.values(), colors):
        angle = 360 * value / total
        canvas.create_arc(x - radius, y - radius, x + radius, y + radius, start=start_angle, extent=angle,
                          fill=color)
        start_angle += angle

    # Draw legend
    legend_x, legend_y = x + radius + 5, y - radius
    for category, value, color in zip(data.keys(), data.values(), colors):
        canvas.create_rectangle(legend_x, legend_y, legend_x + 20, legend_y + 20, fill=color)
        canvas.create_text(legend_x + 25, legend_y + 10, text=f"{category} ({value})", anchor='w')
        legend_y += 25

    # Draw title
    canvas.create_text(x, y - radius - 30, text=title, font=('Arial', 14, 'bold'))


window = Tk()
window.iconbitmap(relative_to_assets("window_logo.ico"))
window.geometry("1116x582")
window.configure(bg="#28283F")
window.title("Money Manager")
window.geometry("+150+40")

canvas = Canvas(
    window,
    bg="#28283F",
    height=582,
    width=1116,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    134.0,
    291.0,
    image=image_image_1
)

# Header
header = Frame(window, bg='#C07BB5')
header.place(x=300, y=0, width=840, height=50)

# Greeting text 
greeting_text = Label(header, text=f"{get_greeting()}", font=("Pacifico", 22, "bold"), fg='black', bg='#C07BB5')
greeting_text.place(x=310, y=5)

# Time text 
time_text = f'It\'s {get_bangladesh_time()}'
time_label = Label(header, text=time_text, font=("Pacifico", 14, "bold"), fg='#0000FF', bg='#C07BB5')
time_label.place(x=680, y=10)

# User name
cname = Label(header, text='', fg='#BD2EEF', bg='#C07BB5', font=("", 15, "bold"))
cname.place(x=53, y=15)

# Profile
profile_image_path = relative_to_assets("avatar_7235981.png")
try:
    profile_photo = PhotoImage(file=profile_image_path)
except TclError:
    profile_photo = None
    print(f"Profile image not found: {profile_image_path}")
profile_label = Label(header, image=profile_photo, bg='#C07BB5')
profile_label.image = profile_photo
profile_label.place(x=15, y=8)

# Body
frame1 = Frame(window, bg='#7CCEC9')
frame1.place(x=300, y=70, width=840, height=350)

# Calculate income and expenses
income_data, expenses_data = calculate_income_expenses(filename)

# Create a canvas for drawing pie charts
canvas = Canvas(frame1, bg='#7CCEC9', width=800, height=350, bd=0, highlightthickness=0)
canvas.pack()

# Define colors for the pie chart slices
income_colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700']
expenses_colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700']

# Draw pie charts with specified colors
draw_pie_chart(canvas, income_data, "Income Details", 120, 175, 120, income_colors)
draw_pie_chart(canvas, expenses_data, "Expenses Details", 502, 175, 120, expenses_colors)

# Frame 2
frame2 = Frame(window, bg='#FF004D')
frame2.place(x=300, y=430, width=210, height=148)

# Calculate total balance (Total Income - Total Expenses)
total_income = sum(income_data.values())
total_expenses = sum(expenses_data.values())
total_balance = total_income - total_expenses

# Label for total balance
total_balance_label = Label(frame2, text=f'Total Balance\n\n{total_balance}', font=("", 15, "bold"), fg='dark blue', bg='#FF004D')
total_balance_label.place(x=40, y=20)

# Frame 3
frame3 = Frame(window, bg='#BFEA7C')
frame3.place(x=600, y=430, width=210, height=148)

# Calculate the most income-earning source
most_income_source = max(income_data, key=income_data.get)
most_income_amount = income_data[most_income_source]

# Display the most income-earning source and its amount
most_income_label = Label(frame3,
                          text=f"Most Income Source\n\n{most_income_source}\n\nAmount: {most_income_amount}",
                          font=("light", 15), fg='blue', bg='#BFEA7C')
most_income_label.place(x=100, y=70, anchor=CENTER)

# Frame 4
frame4 = Frame(window, bg='#FF8911')
frame4.place(x=890, y=430, width=210, height=148)

# Calculate the most expense source
most_expense_source = max(expenses_data, key=expenses_data.get)
most_expense_amount = expenses_data[most_expense_source]

# Display the most expense source and its amount
most_expense_label = Label(frame4,
                           text=f"Most Expense Source\n\n{most_expense_source}\n\nAmount: {most_expense_amount}",
                           font=("bold", 15), fg='#FFFFFF', bg='#FF8911')
most_expense_label.place(x=110, y=70, anchor=CENTER)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=51.0,
    y=72.0,
    width=193.0,
    height=32.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=switch_income,
    relief="flat"
)
button_2.place(
    x=47.0,
    y=108.0,
    width=193.0,
    height=28.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=switch_expense,
    relief="flat"
)
button_3.place(
    x=45.0,
    y=139.0,
    width=192.0,
    height=33.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=switch_summery,
    relief="flat"
)
button_4.place(
    x=45.0,
    y=169.0,
    width=208.0,
    height=33.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=switch_login,
    relief="flat"
)
button_5.place(
    x=87.0,
    y=440.0,
    width=136.0,
    height=64.0
)
window.resizable(False, False)
window.mainloop()
