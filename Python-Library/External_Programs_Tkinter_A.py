from tkinter import *
from External_Programs_Tkinter_B import nameit

root = Tk()
root.title('External files')
root.iconbitmap('c:/code/Code-Snippets/Python-Code-Snippets/images/icon.ico')
root.geometry('500x350')

greet = nameit('Kevin')

my_label = Label(root, text=greet, font=('Helvetica', 30))
my_label.pack(pady=20)

root.mainloop()