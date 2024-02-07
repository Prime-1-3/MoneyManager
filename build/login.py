import os
import csv
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\SDP\MoneyManager\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def execute_python_file(file_path):
   try:
      os.system(f'python {file_path}')
   except FileNotFoundError:
      print(f"Error: The file '{file_path}' does not exist.")


def switch_reg():
    window.destroy()
    execute_python_file("E:/SDP/MoneyManager/build/registration.py")

def popmsg(name):
    messagebox.showinfo("Greetings",name+" Welcome Back")

def pop_reg_msg():
    messagebox.showinfo("Incorrect Mail or Password","Wrong Email or Password \n"+
                        "please enter Your Email and Password correctly\n\n"+
                        "If you don't have an accont, please register")

def input_err(field):
    field=field+" has no value"
    messagebox.showerror("No Input",field)

filename="E:/SDP/MoneyManager/user_rec.csv"

def check_user():
    with open(filename,'r') as file:
        email=entry_1.get()
        if email=="":
            input_err("Email")
        Password=entry_2.get()
        if Password=="":
            input_err("Password")
        

        readar=csv.reader(file)
        flag=0
        for line in readar:
            if email==line[1] and Password==line[2]:
                popmsg(line[0])
                flag=1
                break
        if flag==0:
            pop_reg_msg()
        file.close()




window = Tk()

window.title("Money Manager")
window.geometry("1116x582")
window.geometry("+150+40")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
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
    558.0,
    291.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    772.0,
    290.0,
    image=image_image_2
)

canvas.create_text(
    614.0,
    103.0,
    anchor="nw",
    text="Enter Your Email and Password",
    fill="#000000",
    font=("ZenKakuGothicAntique Medium", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    772.9159851074219,
    220.88128662109375,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#DAF3C6",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=622.7203369140625,
    y=197.34115600585938,
    width=300.39129638671875,
    height=45.08026123046875
)

canvas.create_rectangle(
    624.0,
    187.65084838867188,
    662.0,
    202.70169639587402,
    fill="#FAFAFA",
    outline="")

canvas.create_text(
    620.0,
    180.6271209716797,
    anchor="nw",
    text="Email",
    fill="#212121",
    font=("ZenKakuGothicAntique Regular", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    772.9159851074219,
    284.7759418487549,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#DAF3C6",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=622.7203369140625,
    y=261.2358093261719,
    width=300.39129638671875,
    height=45.080265045166016
)

canvas.create_rectangle(
    621.0,
    247.85423278808594,
    686.0,
    265.9152488708496,
    fill="#FAFAFA",
    outline="")

canvas.create_text(
    625.0,
    240.8305206298828,
    anchor="nw",
    text="Password",
    fill="#212121",
    font=("ZenKakuGothicAntique Regular", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=check_user,
    relief="flat"
)
button_1.place(
    x=614.7203369140625,
    y=321.767578125,
    width=316.39129638671875,
    height=47.080265045166016
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    772.3043212890625,
    389.30169677734375,
    image=image_image_3
)

canvas.create_text(
    633.0,
    415.0,
    anchor="nw",
    text="Don’t have an account?",
    fill="#212121",
    font=("ZenKakuGothicAntique Regular", 24 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=switch_reg,
    relief="flat"
)
button_2.place(
    x=660.0,
    y=457.0,
    width=220.0,
    height=44.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    213.0,
    59.10955810546875,
    image=image_image_4
)
window.resizable(False, False)
window.mainloop()
