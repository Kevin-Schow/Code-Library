from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Python Tkinter')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('400x400')


vertical = Scale(root, from_=200, to=0)
vertical.pack()

horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL)
horizontal.pack()



def slide():
    my_label = Label(root, text=horizontal.get()).pack()

my_btn = Button(root, text='Apply', command=slide).pack()

root.mainloop()
