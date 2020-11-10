from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Read Write Text Files')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('500x400')

# Read only r
# Read and Write r+
# Write only w
# Write and read w+
# Append only a
# Append and read a+

def open_text():
    text_file = filedialog.askopenfilename(initialdir='c:/Users/haugl/PycharmProjects/TutorialPlayground/', title='Open Text File', filetypes=(('Text Files', '*.txt'), ))
    text_file = open(text_file, 'r')
    stuff = text_file.read()

    my_text.insert(END, stuff)
    text_file.close()


def save_text():
    text_file = filedialog.askopenfilename(initialdir='c:/Users/haugl/PycharmProjects/TutorialPlayground/', title='Open Text File', filetypes=(('Text Files', '*.txt'), ))
    text_file = open(text_file, 'w')
    text_file.write(my_text.get(1.0, END))

my_text = Text(root, width=40, height=10, font=('Helvetica', 16))
my_text.pack(pady=20)

open_button = Button(root, text='Open Text File', command=open_text)
open_button.pack(pady=20)

save_button = Button(root, text='Save File', command=save_text)
save_button.pack(pady=20)



root.mainloop()
