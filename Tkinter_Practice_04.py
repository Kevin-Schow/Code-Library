from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Python Tkinter')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno('Title Bar', 'Hello')
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text='You clicked Yes').pack()
    else:
        Label(root, text='You clicked No').pack()


Button(root, text='Popup', command=popup).pack()



root.mainloop()
