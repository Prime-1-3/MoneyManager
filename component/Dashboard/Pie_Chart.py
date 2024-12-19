import tkinter as tk
import random

def rgb_to_hex(rgb):
    """Convert an RGB tuple to a HEX color string."""
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def generate_random_colors(count):
    """Generate a list of 'count' random colors represented as RGB tuples."""
    return [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(count)]



def draw_pie_chart(canvas, data):
    width = canvas.winfo_reqwidth()
    height = canvas.winfo_reqheight()
    diameter = min(width, height) * 0.9
    x0 = (width - diameter) / 2
    y0 = (height - diameter) / 2
    x1 = x0 + diameter
    y1 = y0 + diameter

    start_angle = 0
    total = sum(data.values())
    for category, value in data.items():
        extent = (value / total) * 360
        canvas.create_arc(x0, y0, x1, y1, start=start_angle, extent=extent, fill=next(color_cycle))
        start_angle += extent

# Create a Tkinter window
root = tk.Tk()
root.title("Simple Pie Chart")

# Set the window size
root.geometry("600x600")

# Create a canvas widget
pie1 = tk.Canvas(root, width=300, height=300)
pie1.pack(fill=tk.BOTH, expand=True)

# Define data for the pie chart
data = {
    "Apples": 300,
    "Bananas": 159,
    "Cherries": 235,
    "Dates": 100,
    "kelea":99,
    'malfta':200,
    "Datfwes": 103,
    "kelsa":99,
    'mavlta':200,
    "Daetes": 103,
    "kelaw":99,
    'malfta':100
}

# Define a simple cycle of colors for the pie slices
colors =[]
x=len(data)
c_limit=generate_random_colors(x)
for i in c_limit:
    colors.append(rgb_to_hex(i))

print(colors)
color_cycle = iter(colors * (len(data) // len(colors) + 1))

# Draw the pie chart
draw_pie_chart(pie1, data)

# Run the Tkinter event loop
root.mainloop()
