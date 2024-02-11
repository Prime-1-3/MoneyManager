from tkinter import Tk, Button, Label, messagebox

root = Tk()
root.title("Message")
root.geometry('700x350')

def clicker():
    mb = messagebox.askretrycancel("Message", "Display Some Message Here")
    my_label.config(text=f'You Clicked {mb}')

my_button = Button(root, text="Click Me", command=clicker)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()
