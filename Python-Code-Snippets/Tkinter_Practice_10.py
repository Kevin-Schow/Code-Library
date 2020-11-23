from tkinter import *

root = Tk()
root.title('Remove Label')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('400x400')


def myDelete():
    # myLabel.pack_forget()
    myLabel.destroy()
    myButton['state'] = NORMAL


def myClick():
    global myLabel
    hello = 'Hello ' + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, 'end')
    myLabel.grid(row=3, column=0, pady=10)
    myButton['state'] = DISABLED


e = Entry(root, width=17, font=('Helvetica', 30))
e.grid(row=0, column=0, padx=10, pady=10)

myButton = Button(root, text='Enter Your Name', command=myClick)
myButton.grid(row=1, column=0, pady=10)

deleteButton = Button(root, text='Delete Text', command='myDelete')
deleteButton.grid(row=2, column=0,pady=10)

root.mainloop()
