from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from random import randint

root = Tk()
root.title('Bind Keyboard Events')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('400x400')

def clicker(event):
    myLabel = Label(root, text='Click' + str(event.x) + ' ' + str(event.y))
    myLabel.pack()


myButton = Button(root, text='Click Me')
 # Enter, Leave, Button-3, FocusIn, Return, Key(event.char)
myButton.bind('<Button-1>', clicker)
myButton.pack(pady=20)



root.mainloop()
