from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Buttons')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('600x500')

root.configure(bg='white')

def thing():
    my_label.config(text='You Signed In')

# login_btn = PhotoImage(file='c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/signin.jpg')
login_btn = ImageTk.PhotoImage(Image.open('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/signin.jpg'))

img_label = Label(image=login_btn)
# img_label.pack(pady=20)

my_button = Button(root, image=login_btn, command=thing, borderwidth=0)
my_button.pack(pady=20)

my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()
