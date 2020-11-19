from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title('Progress Bars')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('600x400')

def step():
    # my_progress['value'] += 20
    # my_progress.start(10)
    for x in range(5):
        my_progress['value'] += 20
        root.update_idletasks()
        time.sleep(1)

my_progress = ttk.Progressbar(root, orient=HORIZONTAL,
                              length=300, mode='determinate')
my_progress.pack(pady=20)

my_button = Button(root, text='Progress', command=step)
my_button.pack(pady=20)




root.mainloop()
