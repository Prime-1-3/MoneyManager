from datetime import datetime
from pathlib import Path
from tkinter import *
import os
import tkinter
import csv


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\summery")
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

def switch_expense():
    window.destroy()
    execute_python_file(OUTPUT_PATH/Path("expense.py"))


def switch_income():
    window.destroy()
    execute_python_file(OUTPUT_PATH/Path("income.py"))




window = Tk()
window.iconbitmap(relative_to_assets("window_logo.ico"))
window.geometry("1116x582")
window.configure(bg = "#28283F")
window.title("Money Manager")
window.geometry("+150+40")



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
    455.0,
    image=image_image_1
)

def extract_date(row):
    date_string = row[1] 
    try:
        return datetime.strptime(date_string, "%b %d %y")
    except ValueError:
        return datetime.strptime(date_string,'%b %d %Y')

with open(filename,"r",newline="") as file:
    reader = csv.reader(file)
    data=list(reader)
    header=data[0]
    d_sorted=sorted(data[1:],key=extract_date)
    d_sorted.insert(0,header)
    d_count=len(data)
    

    window.grid_columnconfigure(0,weight=1)    
    
    if d_count<=10:
        for i, row in enumerate(d_sorted, start=1):
            for col in range(1, 4):
                if row[0]=='1':
                    lebel= tkinter.Label(window, text=row[col],font='oregano',height=2,width=12,relief=tkinter.RIDGE,bg='#0FFF52')
                    lebel.grid(row=i, column=col,ipadx='72')
                elif row[0]=='flag':
                    lebel= tkinter.Label(window, text=row[col],font='oregano',height=2,width=12,relief=tkinter.RIDGE,bg='#E2B2FF')
                    lebel.grid(row=i, column=col,ipadx='72')
                else:
                    lebel= tkinter.Label(window, text=row[col],font='oregano',height=2,width=12,relief=tkinter.RIDGE,bg='#FF4545')
                    lebel.grid(row=i, column=col,ipadx='72')
                
    else:
        for i, row in enumerate(d_sorted, start=1):
            for col in range(1, 4):
                if row[0]=='1':
                    lebel= tkinter.Label(window, text=row[col],font='oregano',height=1,width=12,relief=tkinter.RIDGE,bg='#0FFF52')
                    lebel.grid(row=i, column=col,ipadx='72')
                elif row[0]=='flag':
                    lebel= tkinter.Label(window, text=row[col],font='oregano',height=1,width=12,relief=tkinter.RIDGE,bg='#E2B2FF')
                    lebel.grid(row=i, column=col,ipadx='72')
                else:
                    lebel= tkinter.Label(window, text=row[col],font='oregano',height=1,width=12,relief=tkinter.RIDGE,bg='#FF4545')
                    lebel.grid(row=i, column=col,ipadx='72')



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
    command=switch_expense,
    relief="flat"
)
button_3.place(
    x=45.0,
    y=139.0,
    width=192.0,
    height=24.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=44.0,
    y=172.0,
    width=193.0,
    height=32.0
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

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1060.0,
    550.0,
    image=image_image_2
)

window.resizable(False, False)
window.mainloop()
