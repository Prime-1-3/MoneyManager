from tkinter import *
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\sdp\ui")

def button_clicked(button_name):
    print(button_name + " button clicked!")

root = Tk()
root.title("Overview Button Example")

# Load the image
background_image = PhotoImage(file=ASSETS_PATH / "1_cd_KQ7ZAAdna0lovp2v8HQ.png")

# Create a label with the image and adjust its size
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Increase image size
new_width = background_image.width() * 2
new_height = background_image.height() * 2
background_image = background_image.zoom(2)
background_label.config(image=background_image)

# Define the colors
green_color = "#4CAF50"
red_color = "#FF5733"
blue_color = "#3399FF"
black_color = "black"

# Function to create elliptical-like buttons
def create_elliptical_like_button(text, color, rely):
    button = Button(root, text=text, command=lambda: button_clicked(text), bg=color, fg=black_color, width=20, height=2)
    button.place(relx=0.05, rely=rely, anchor=W)
    return button

# Create buttons
overview_button = create_elliptical_like_button("Overview", green_color, 0.2)
message_button = create_elliptical_like_button("Message", green_color, 0.35)
payment_button = create_elliptical_like_button("Payment", green_color, 0.5)
community_button = create_elliptical_like_button("Community", green_color, 0.65)
account_button = create_elliptical_like_button("Account", red_color, 0.8)
setting_button = create_elliptical_like_button("Setting", blue_color, 0.95)

root.mainloop()
