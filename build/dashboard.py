from pathlib import Path
from tkinter import *
import os



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\dashboard")
filename=OUTPUT_PATH/Path("data.csv")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def execute_python_file(file_path):
   try:
      os.system(f'python {file_path}')
   except FileNotFoundError:
      print(f"Error: The file '{file_path}' does not exist.")

def execute_python_file(file_path):
   try:
      os.system(f'python {file_path}')
   except FileNotFoundError:
      print(f"Error: The file '{file_path}' does not exist.")


def switch_login():
    window.destroy()
    execute_python_file(OUTPUT_PATH/Path("login.py"))

def switch_income():
    window.destroy()
    execute_python_file(OUTPUT_PATH/Path("income.py"))

def switch_expense():
    window.destroy()
    execute_python_file(OUTPUT_PATH/Path("expense.py"))

def switch_summery():
    window.destroy()
    execute_python_file(OUTPUT_PATH/Path("summery.py"))



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
    291.0,
    image=image_image_1
)

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
