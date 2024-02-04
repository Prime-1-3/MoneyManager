import tkinter
from tkinter import *
from pathlib import Path
from tkinter import messagebox

window = Tk()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\SDP\MoneyManager\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def fun1():
   messagebox.showinfo("hello","nice")


window.geometry("1116x590")
window.configure(bg = "#FFFFFF")


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=fun1,
    relief="flat"
)
button_2.place(
    x=660.0,
    y=462.0,
    width=220.0,
    height=44.0
)


window.resizable(True, True)
window.mainloop()
