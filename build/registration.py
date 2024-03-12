from pathlib import Path
from tkinter import *
import csv
from tkinter import messagebox
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\reg")
filename=OUTPUT_PATH/Path("user_rec.csv")

def execute_python_file(file_path):
   try:
      os.system(f'python {file_path}')
   except FileNotFoundError:
      print(f"Error: The file '{file_path}' does not exist.")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def popmsg():
   messagebox.showinfo("Already Registered","User Already Exist\nPlease Log in")

def input_err(field):
    field=field+" has no value"
    messagebox.showerror("No Input",field)

def new_user():
    with open(filename,'r+',newline="") as file:
        name=entry_1.get()
        if name=="":
            input_err("Name")
        email=entry_2.get()
        if email=="":
            input_err("Email")
        Password=entry_3.get()
        if Password=="":
            input_err("Password")
        field=[name,email,Password]

        readar=csv.reader(file)
        flag=0
        for line in readar:
            if field==line:
                print(line)
                popmsg()
                flag=1
                break
        if flag==0:
            csv.writer(file).writerow(field)
            messagebox.showinfo("Success","New User Registration is Successful.\n"+
                                "Now Log Into The System")
            file.close()
            switch_login()


def switch_login():
    window.destroy()
    execute_python_file(OUTPUT_PATH/Path("login.py"))
        


window = Tk()

window.iconbitmap(relative_to_assets("window_logo.ico"))
window.title("Money Manager")
window.geometry("1116x590")
window.geometry("+150+40")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 590,
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
    296.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    772.0,
    295.0,
    image=image_image_2
)

canvas.create_text(
    613.0,
    33.0,
    anchor="nw",
    text="LET'S GET YOU STARTED",
    fill="#000000",
    font=("ZenKakuGothicAntique Regular", 12 * -1)
)

canvas.create_text(
    613.0,
    92.0,
    anchor="nw",
    text="Create an Account",
    fill="#000000",
    font=("ZenKakuGothicAntique Medium", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    772.9159851074219,
    161.43939399719238,
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
    y=137.97879028320312,
    width=300.39129638671875,
    height=44.921207427978516
)

canvas.create_rectangle(
    624.0,
    129.0,
    690.0,
    143.0,
    fill="#FAFAFA",
    outline="")

canvas.create_text(
    621.0,
    120.0,
    anchor="nw",
    text="Your Name",
    fill="#212121",
    font=("ZenKakuGothicAntique Regular", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    772.9159851074219,
    225.1181812286377,
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
    y=201.65757751464844,
    width=300.39129638671875,
    height=44.921207427978516
)

canvas.create_rectangle(
    624.0,
    192.0,
    662.0,
    207.0,
    fill="#FAFAFA",
    outline="")

canvas.create_text(
    620.0,
    185.0,
    anchor="nw",
    text="Email",
    fill="#212121",
    font=("ZenKakuGothicAntique Regular", 12 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    772.9159851074219,
    288.79697036743164,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#DAF3C6",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=622.7203369140625,
    y=265.33636474609375,
    width=300.39129638671875,
    height=44.92121124267578
)

canvas.create_rectangle(
    621.0,
    252.0,
    686.0,
    270.0,
    fill="#FAFAFA",
    outline="")

canvas.create_text(
    625.0,
    245.0,
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
    #command=lambda: print("button_1 clicked"),
    command=new_user,
    relief="flat"
)
button_1.place(
    x=614.7203369140625,
    y=325.66363525390625,
    width=316.39129638671875,
    height=46.92121124267578
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    772.3043212890625,
    393.0,
    image=image_image_3
)

canvas.create_text(
    633.0,
    419.0,
    anchor="nw",
    text="Already have an account?",
    fill="#212121",
    font=("ZenKakuGothicAntique Regular", 24 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=switch_login,
    relief="flat"
)
button_2.place(
    x=660.0,
    y=462.0,
    width=220.0,
    height=44.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    213.0,
    64.10955810546875,
    image=image_image_4
)
window.resizable(True, True)
window.mainloop()



