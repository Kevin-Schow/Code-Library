from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Tabs')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('500x500')

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15)

def hide():
    my_notebook.hide(1)

def show():
    my_notebook.add(my_frame2, text='Red Tab')

def select():
    my_notebook.select(1)

my_frame1 = Frame(my_notebook, width=500, height=500, bg='blue')
my_frame2 = Frame(my_notebook, width=500, height=500, bg='red')
my_frame3 = Frame(my_notebook, width=500, height=500, bg='green')
my_frame4 = Frame(my_notebook, width=500, height=500, bg='yellow')

my_frame1.pack(fill='both', expand=1)
my_frame2.pack(fill='both', expand=1)
my_frame3.pack(fill='both', expand=1)
my_frame4.pack(fill='both', expand=1)

my_notebook.add(my_frame1, text='Blue Tab')
my_notebook.add(my_frame2, text='Red Tab')
my_notebook.add(my_frame3, text='Green Tab')
my_notebook.add(my_frame4, text='Yellow Tab')

# Hide/Show Tab
my_button1 = Button(my_frame1, text='Hide Tab 2', command=hide).pack(pady=10)
my_button2 = Button(my_frame1, text='Show Tab 2', command=show).pack(pady=10)

# Navigate to a Tab
my_button3 = Button(my_frame1, text='Navigate to Tab 2', command=select).pack(pady=10)


root.mainloop()
