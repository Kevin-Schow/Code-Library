from tkinter import *
import time


root = Tk()
root.title('Resize Window Dynamically')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('600x400')

def resize():
    w = width_entry.get()
    h = height_entry.get()
    root.geometry(f'{w}x{h}')

my_button = Button(root, text='Resize', command=resize)
my_button.pack(pady=20)

width_label = Label(root, text='Width:')
width_label.pack(pady=20)
width_entry = Entry(root)
width_entry.pack()

height_label = Label(root, text='Width:')
height_label.pack(pady=20)
height_entry = Entry(root)
height_entry.pack()




root.mainloop()
