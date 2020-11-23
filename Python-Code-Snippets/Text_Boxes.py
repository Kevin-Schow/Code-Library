from tkinter import *


root = Tk()
root.title('Text Boxes')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('500x400')

def clear():
    my_text.delete(1.0, END)

def get_text():
    my_label.config(text=my_text.get(1.0, END))


my_text = Text(root, width=40, height=10, font=('Helvetica', 18))
my_text.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame,text='Clear Screen', command=clear)
clear_button.grid(row=0, colum=0)

get_text_button = Button(button_frame, text='Get Text', command=get_text)
get_text_button.grid(row=0, column=1)

my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()
