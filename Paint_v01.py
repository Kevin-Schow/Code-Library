from tkinter import *

root = Tk()
root.title('Paint')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('800x800')


def paint(e):

    # Brush Parameters
    brush_width = 10
    brush_color = 'green'
    # Brush Type: BUTT, ROUND, PROJECTING
    brush_type = ROUND

    # Starting Position
    x1 = e.x - 1
    y1 = e.y - 1

    # Ending Position
    x2 = e.x + 1
    y2 = e.y + 1

    # Draw On Canvas
    my_canvas.create_line(x1, y1, x2, y2, fill=brush_color, width=brush_width, capstyle=brush_type, smooth=True)


w = 600
h = 400

my_canvas = Canvas(root, width=w, height=h, bg='white')
my_canvas.pack(pady=20)

my_canvas.bind('<B1-Motion>', paint)





root.mainloop()
