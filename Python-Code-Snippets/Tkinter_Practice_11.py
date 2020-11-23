from tkinter import *


root = Tk()
root.title('Classes')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('400x400')

class Elder:

    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(master, text='Click Me', command=self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print('Click')

e = Elder(root)

root.mainloop()
