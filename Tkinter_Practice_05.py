from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Python Tkinter')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')

def open_second():
    global my_img
    top = Toplevel()
    top.title('Images')
    top.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
    lbl = Label(top, text='Here is your image:').pack()
    my_img = ImageTk.PhotoImage(Image.open('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/mages.jpg'))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text='Close Window', command=top.destroy).pack()

btn = Button(root, text='Open second window', command=open_second).pack()

root.mainloop()
