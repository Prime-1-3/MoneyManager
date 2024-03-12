from pathlib import Path
from tkinter import *
import os
from tkcalendar import DateEntry
import csv

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\expense")
filename=OUTPUT_PATH/Path("data.csv")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def execute_python_file(file_path):
   try:
      os.system(f'python {file_path}')
   except FileNotFoundError:
      print(f"Error: The file '{file_path}' does not exist.")


def switch_login():
    window.destroy()
    execute_python_file(OUTPUT_PATH/Path("login.py"))

def switch_dash():
    window.destroy()
    execute_python_file(OUTPUT_PATH/Path("dashboard.py"))

def switch_income():
    window.destroy()
    execute_python_file(OUTPUT_PATH/Path("income.py"))

def switch_summery():
    window.destroy()
    execute_python_file(OUTPUT_PATH/Path("summery.py"))


def submit_button_press():
    with open(filename,'a',newline="") as file:
    
        expense_source = entry_1.get().strip()
        expense_amount = entry_2.get().strip()

    
        if expense_source and expense_amount.isnumeric():
            field=[0,cal.get_date().strftime("%b %d %Y"),expense_source, expense_amount]
            csv.writer(file).writerow(field)
            entry_1.delete(0,'end')
            entry_2.delete(0,'end')
            file.close()

            warning_label.place(x=515.0, y=430.0)
            warning_label.config(text="Successfully Submitted!!",fg="white")
            window.after(900,lambda:warning_label.place_forget())

        elif expense_amount and not expense_source:
            warning_label.place(x=515.0, y=430.0)
            warning_label.config(text="Please Enter Expense Source",fg="red")

        elif not expense_amount and expense_source:
            warning_label.place(x=515.0, y=430.0)
            warning_label.config(text="Please Enter Expense Amount",fg="red")

        elif not expense_source and not expense_amount:
            warning_label.place(x=515.0, y=430.0)
            warning_label.config(text="Please provide both Expense Source and Expense Amount.", fg="red", font=("Poppins", 10))

        elif not expense_amount.isnumeric():
            warning_label.place(x=515.0, y=430.0)
            warning_label.config(text="Expense Amount Can Be Only Numbers",fg="red")



window = Tk()
window.iconbitmap(relative_to_assets("window_logo.ico"))
window.title("Money Manager")
window.geometry("1116x582")
window.geometry("+150+40")
window.configure(bg = "#28283F")


canvas = Canvas(
    window,
    bg = "#28283F",
    height = 582,
    width = 1116,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    134.0,
    367.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=switch_dash,
    relief="flat"
)
button_1.place(
    x=50.0,
    y=74.0,
    width=196.0,
    height=33.0
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
    x=51.0,
    y=107.0,
    width=189.0,
    height=26.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=53.0,
    y=139.0,
    width=193.0,
    height=32.0
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
    x=47.0,
    y=173.0,
    width=196.0,
    height=31.0
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

canvas.create_rectangle(
    486.0,
    46.0,
    881.0,
    539.0,
    fill="#28283F",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    684.0,
    292.0,
    image=image_image_2
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=submit_button_press,
    relief="flat"
)
button_6.place(
    x=612.0,
    y=466.0,
    width=136.0,
    height=65.46057891845703
)

canvas.create_rectangle(
    503.0,
    107.0,
    858.0,
    191.0,
    fill="#454567",
    outline="")

canvas.create_rectangle(
    503.0,
    247.0,
    858.0,
    331.0,
    fill="#454567",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    680.5,
    149.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=526.0,
    y=107.0,
    width=309.0,
    height=82.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    680.5,
    289.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=526.0,
    y=247.0,
    width=309.0,
    height=82.0
)

canvas.create_text(
    503.0,
    69.0,
    anchor="nw",
    text="Enter Expense Reason",
    fill="#FEFAD9",
    font=("Poppins SemiBold", 18 * -1)
)

canvas.create_text(
    503.0,
    209.0,
    anchor="nw",
    text="Enter Expense Amount",
    fill="#FEFAD9",
    font=("Poppins SemiBold", 18 * -1)
)

canvas.create_text(
    503.0,
    350.0,
    anchor="nw",
    text="Select Date",
    fill="#FEFAD9",
    font=("Poppins SemiBold", 18 * -1)
)

cal=DateEntry(window,selectmode="day",date_pattern='dd-MM-yyyy',background="dark green",
              fieldbackground='lightblue',
              foreground='yellow',
              arrowcolor='red')
cal.grid(pady=385,padx=504)

warning_label = Label(
    window,
    text="",
    bg="#28283F",
    fg="red",
    font=("Poppins", 12)
)


window.resizable(False, False)
window.mainloop()
