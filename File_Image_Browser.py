from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Python Tkinter')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')


def open_btn():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir='c:/Users/haugl/PycharmProjects/TutorialPlayground/Images',
                                               title='Select a file', filetypes=(
            ('jpg files', '*.jpg'), ('png files', '*.png'), ('all files', '*.*')))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text='Open File', command=open_btn).pack()

root.mainloop()
