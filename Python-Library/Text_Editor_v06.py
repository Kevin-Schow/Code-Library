from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Text Editor')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('1200x660')


def new_file():
    my_text.delete('1.0', END)
    root.title('New File - Text Editor')
    status_bar.config(text='New File        ')


def open_file():
    my_text.delete('1.0', END)
    text_file = filedialog.askopenfilename(initialdir='c:/Users/haugl/PycharmProjects/TutorialPlayground/', title='Open File', filetypes=(('Text Files', '*.txt'), ('HTML Files', '*.html'), ('Python Files', '*.py'), ('All Files', '*.*')))

    # Update Status Bars
    name = text_file
    status_bar.config(text=f'{name}        ')
    name = name.replace('C:/Users/haugl/PycharmProjects/TutorialPlayground/', '')
    name = name.replace('.txt', '')
    root.title(f'{name} - Text Editor')

    # Open File
    text_file = open(text_file, 'r')
    text = text_file
    my_text.insert(END, text)
    text_file.close


def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension='.*', initialdir='C:/Users/haugl/PycharmProjects/TutorialPlayground/', title='Save File As', filetypes=(('Text Files', '*.txt'), ('HTML Files', '*.html'), ('Python Files', '*.py'), ('All Files', '*.*')))
    if text_file:
        # Update Status Bars
        name = text_file
        status_bar.config(text=f'Saved:  {name}        ')
        name = name.replace('C:/Users/haugl/PycharmProjects/TutorialPlayground/', '')
        root.title(f'{name} - Text Editor')

        # SAve The File
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()



# Create  Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create Scrollbar for Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box
my_text = Text(my_frame, width=97, height=25, font=('Helvetica', 16), selectbackground='yellow',
               selectforeground='black', undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# Configure Scrollbar
text_scroll.config(command=my_text.yview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save')
file_menu.add_command(label='Save As', command=save_as_file)
file_menu.add_seperator()
file_menu.add_command(label='Exit', command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')
edit_menu.add_command(label='Undo')
edit_menu.add_command(label='Redo')

# Add Status Bar to Bottom of App
status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()
