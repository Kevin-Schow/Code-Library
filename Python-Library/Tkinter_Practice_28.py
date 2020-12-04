from tkinter import *

root = Tk()
root.title('Drag Images with Mouse')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('800x600')

w = 600
h = 400
x = w / 2
y = h / 2

my_canvas = Canvas(root, width=w, height=h, bg='white')
my_canvas.pack(pady=20)

# Add image to canvas
img = PhotoImage(file='c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/smile.png')
my_image = my_canvas.create_image(0, 0, anchor=NW, image=img)


def move(e):
    global img
    img = PhotoImage(file='c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/smile.png')
    my_image = my_canvas.create_image(e.x, e.y, image=img)
    my_label.config(text='Coordinates: x ' + str(e.x) + ' y ' + str(e.y))

my_label = Label(root, text='')
my_label.pack(pady=20)

my_canvas.bind('<B1-Motion>', move)

root.mainloop()
