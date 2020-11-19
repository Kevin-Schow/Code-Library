from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title('Color Picker')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('400x400')


def color():
    # [0][0] Selects first item of RGB values, [1] gets hex code
    my_color = colorchooser.askcolor()[1]
    my_label = Label(root, text=my_color).pack(pady=10)
    my_label2 = Label(root, text='You picked a color', font=('Helvetica', 32), bg=my_color).pack()


my_button = Button(root, text='Pick a Color', command=color).pack()

root.mainloop()
