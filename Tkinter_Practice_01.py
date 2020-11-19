from tkinter import *

root = Tk()

e = Entry(root, width=50, bg='aliceblue', borderwidth=10)
e.pack()
e.insert(0, 'Enter Your Name: ')


def my_click():
    my_label = Label(root, text='+ ' + e.get())
    my_label.pack()


myButton = Button(root, text='Enter your name', padx=50, pady=50, command=my_click, bg='lightblue')
myButton.pack()

root.mainloop()
