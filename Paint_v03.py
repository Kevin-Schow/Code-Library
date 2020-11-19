from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser

root = Tk()
root.title('Paint')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('800x800')

brush_color = 'black'


def paint(e):

    # Brush Parameters
    brush_width = '%0.0f' % float(my_slider.get())
    # Brush Type: BUTT, ROUND, PROJECTING
    brush_type_style = brush_type.get()

    # Starting Position
    x1 = e.x - 1
    y1 = e.y - 1

    # Ending Position
    x2 = e.x + 1
    y2 = e.y + 1

    # Draw On Canvas
    my_canvas.create_line(x1, y1, x2, y2, fill=brush_color, width=brush_width, capstyle=brush_type_style, smooth=True)


def change_brush_size(e):
    slider_label.config(text='%0.0f' % float(my_slider.get()))


def change_brush_color():
    global brush_color
    brush_color = 'black'
    brush_color = colorchooser.askcolor(color=brush_color)[1]


def change_canvas_color():
    global canvas_color
    canvas_color = 'white'
    canvas_color = colorchooser.askcolor(color=canvas_color)[1]
    my_canvas.config(bg=canvas_color)


w = 600
h = 400

my_canvas = Canvas(root, width=w, height=h, bg='white')
my_canvas.pack(pady=20)

my_canvas.bind('<B1-Motion>', paint)

# Create Brush Options Frame
brush_options_frame = Frame(root)
brush_options_frame.pack(pady=20)

# Brush Size
brush_size_frame = LabelFrame(brush_options_frame, text='Brush Size')
brush_size_frame.grid(row=0, column=0, padx=50)
# Brush Slider
my_slider = ttk.Scale(brush_size_frame, from_=1, to=100, command=change_brush_size, orient=VERTICAL, value=10)
my_slider.pack(pady=10, padx=10)
# Brush Slider Label
slider_label = Label(brush_size_frame, text=my_slider.get())
slider_label.pack(pady=5)

# Brush Type
brush_type_frame = LabelFrame(brush_options_frame, text='Brush Type', height=400)
brush_type_frame.grid(row=0, column=1, padx=50)

brush_type = StringVar()
brush_type.set('round')

# Create Radio Buttons for Brush Type
brush_type_radio1 = Radiobutton(brush_type_frame, text='Round', variable=brush_type, value='round')
brush_type_radio2 = Radiobutton(brush_type_frame, text='Slash', variable=brush_type, value='butt')
brush_type_radio3 = Radiobutton(brush_type_frame, text='Diamond', variable=brush_type, value='projecting')

brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

# Change Colors
change_colors_frame = LabelFrame(brush_options_frame, text='Change Colors')
change_colors_frame.grid(row=0, column=2)

# Change Brush Color Button
brush_color_button = Button(change_colors_frame, text='Brush Color', command=change_brush_color)
brush_color_button.pack(pady=10, padx=10)

# Change Canvas Background Color
canvas_color_button = Button(change_colors_frame, text='Canvas Color', command=change_canvas_color)
canvas_color_button.pack(pady=10, padx=10)


root.mainloop()
