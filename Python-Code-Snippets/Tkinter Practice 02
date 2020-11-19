# Basic Image Viewer

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Images')
root.iconbitmap('Images/icon.ico')

button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()

my_img = ImageTk.PhotoImage(Image.open(Images/time.jpg'))
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()
