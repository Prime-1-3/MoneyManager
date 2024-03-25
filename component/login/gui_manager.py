from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from pathlib import Path
from login_manager import LoginManager


class GUI(LoginManager):
    def __init__(self):
        super().__init__()
        self.OUTPUT_PATH = Path(__file__).parent.parent.parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("assets/login")
        self.filename = self.OUTPUT_PATH / Path("data_store/user_rec.csv")

        self.window = Tk()
        self.window.iconbitmap(self.relative_to_assets("window_logo.ico"))
        self.window.title("Money Manager")
        self.window.geometry("1116x582")
        self.window.geometry("+150+40")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=582,
            width=1116,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.create_widgets()

    def create_widgets(self):
        # Image
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            558.0,
            291.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        image_1 = self.canvas.create_image(
            772.0,
            290.0,
            image=self.image_image_2
        )

        self.canvas.create_text(
            614.0,
            103.0,
            anchor="nw",
            text="Enter Your Email and Password",
            fill="#000000",
            font=("ZenKakuGothicAntique Medium", 20 * -1)
        )

        # Email Entry
        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            772.9159851074219,
            220.88128662109375,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#DAF3C6",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=622.7203369140625,
            y=197.34115600585938,
            width=300.39129638671875,
            height=45.08026123046875
        )

        # Password Entry
        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            772.9159851074219,
            284.7759418487549,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#DAF3C6",
            fg="#000716",
            highlightthickness=0,
            show="*"
        )
        self.entry_2.place(
            x=622.7203369140625,
            y=261.2358093261719,
            width=300.39129638671875,
            height=45.080265045166016
        )

        # Email Label
        self.canvas.create_rectangle(
            624.0,
            187.65084838867188,
            662.0,
            202.70169639587402,
            fill="#FAFAFA",
            outline=""
        )
        self.canvas.create_text(
            620.0,
            180.6271209716797,
            anchor="nw",
            text="Email",
            fill="#212121",
            font=("ZenKakuGothicAntique Regular", 12 * -1)
        )

        # Password Label
        self.canvas.create_rectangle(
            621.0,
            247.85423278808594,
            686.0,
            265.9152488708496,
            fill="#FAFAFA",
            outline=""
        )
        self.canvas.create_text(
            625.0,
            240.8305206298828,
            anchor="nw",
            text="Password",
            fill="#212121",
            font=("ZenKakuGothicAntique Regular", 12 * -1)
        )

        # Login Button
        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.get_data,
            relief="flat"
        )
        button_1.place(
            x=614.7203369140625,
            y=321.767578125,
            width=316.39129638671875,
            height=47.080265045166016
        )

        # Register Text
        self.canvas.create_text(
            633.0,
            415.0,
            anchor="nw",
            text="Don’t have an account?",
            fill="#212121",
            font=("ZenKakuGothicAntique Regular", 24 * -1)
        )

        # Register Button
        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_reg,
            relief="flat"
        )
        button_2.place(
            x=660.0,
            y=457.0,
            width=220.0,
            height=44.0
        )

        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            213.0,
            59.10955810546875,
            image=self.image_image_4
        )

    def run(self):
        self.window.resizable(False,False)
        self.window.mainloop()
