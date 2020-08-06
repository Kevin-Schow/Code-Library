from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title('Python Tkinter')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')

frame = LabelFrame(root, text='This is my frame', padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = Button(frame, text='Dont Click Me')
b.pack()

# r = IntVar()
# r.set('2')

MODES = [
    ('Pepperoni', 'Pepperoni'),
    ('Cheese', 'Cheese'),
    ('Mushroom', 'Mushroom'),
    ('Onion', 'Onion')
]

pizza = StringVar()
pizza.set('Pepperoni')

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

# Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=pizza.get())
myLabel.pack()

myButton = Button(root, text='Click Me', command=lambda: clicked(pizza.get()))
myButton.pack()
root.mainloop()
