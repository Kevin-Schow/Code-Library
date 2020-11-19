from tkinter import *

root = Tk()
root.title('Config')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('400x600')

def something():
    my_label.config(text='BLUE', bg='blue')
    root.config(bg='blue')
    my_button.config(text='You got configged', state=DISABLED)

global my_label
my_label = Label(root, text='This is my text', font=('Helvetica', 18))
my_label.pack(pady=10)

global my_button
my_button = Button(root, text='Click', command=something)
my_button.pack(pady=10)


root.mainloop()
