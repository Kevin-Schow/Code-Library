from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Text Editor')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('1200x660')

# Set Variable for Open File Name
global open_status_name
open_status_name = False

global selected
selected = False


def new_file():
    my_text.delete('1.0', END)
    root.title('New File - Text Editor')
    status_bar.config(text='New File        ')

    global open_status_name
    open_status_name = False


def open_file():
    my_text.delete('1.0', END)
    text_file = filedialog.askopenfilename(initialdir='c:/Users/haugl/PycharmProjects/TutorialPlayground/', title='Open File', filetypes=(('Text Files', '*.txt'), ('HTML Files', '*.html'), ('Python Files', '*.py'), ('All Files', '*.*')))

    if text_file:
        global open_status_name
        open_status_name = text_file

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

        # Save The File
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()


def save_file():
    global open_status_name

    if open_status_name:
        # Save The File
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

        status_bar.config(text=f'Saved:  {open_status_name}        ')
    else:
        save_as_file()


def cut_text(e):
    global selected
    # Check if Keyboard Shortcut Used
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            # Grab Selected Text  From Text Box
            selected = my_text.selection_get()
            # Delete Selected Text
            my_text.delete('sel.first', 'sel.last')
            # Clear Clipboard then Append
            root.clipboard_clear()
            root.clipboard_append(selected)


def copy_text(e):
    global selected
    # Check to See if  Used Keyboard Shortcut
    if e:
        selected = root.clipboard_get()
    if my_text.selection_get():
        # Grab Selected Text  From Text Box
        selected = my_text.selection_get()
        # Clear Clipboard then Append
        root.clipboard_clear()
        root.clipboard_append(selected)


def paste_text(e):
    global selected
    # Check if Keyboard Shortcut Used
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)

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
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Save As', command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut      (Ctrl+x)', command=lambda: cut_text(False))
edit_menu.add_command(label='Copy   (Ctrl+c)', command=lambda: copy_text(False))
edit_menu.add_command(label='Paste   (Ctrl+v)', command=lambda: paste_text(False))
edit_menu.add_command(label='Undo')
edit_menu.add_command(label='Redo')

# Add Status Bar to Bottom of App
status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

# Edit Bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)



root.mainloop()
