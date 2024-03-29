from tkinter import *

root = Tk()
root.title('Mouse Hover Over')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('600x400')

def button_hover(e):
    my_button['bg'] = 'white'
    status_label.config(text='Hovering Over The Button!')

def button_hover_leave(e):
    my_button['bg'] = 'SystemButtonFace'
    status_label.config(text='')

my_button = Button(root, text='Click Me', font=('Helvetica', 28))
my_button.pack(pady=50)

status_label = Label(root, text='', bd=1, relief=SUNKEN, anchor=E)
status_label.pack(fill=X, side=BOTTOM, ipady=2)

my_button.bind('<Enter>', button_hover)
my_button.bind('<Leave>', button_hover_leave)



root.mainloop()
