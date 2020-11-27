from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title('Image Swap on Mouse Hover')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('600x400')

def  change(e):
    my_pic = PhotoImage(file='c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/smile.png')
    my_label.config(image=my_pic)
    my_label.image = my_pic

def  change_back(e):
    my_pic = PhotoImage(file='c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/triangle.png')
    my_label.config(image=my_pic)
    my_label.image = my_pic

my_pic = PhotoImage(file='c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/triangle.png')
my_label = Label(root, image=my_pic)
my_label.pack(pady=20)

# <Enter> Is when mouse hovers of image / Enter area of image
my_label.bind('<Enter>', change)
my_label.bind('<Leave>', change_back)


root.mainloop()
