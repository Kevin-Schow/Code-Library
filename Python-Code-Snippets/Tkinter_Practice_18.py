from tkinter import *

root = Tk()
root.title('Menus -- Delete Frame Children')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('400x400')

my_menu = Menu(root)
root.config(menu=my_menu)


def our_command():
    my_label = Label(root, text='You clicked me')


def file_new():
    hide_all_frames()
    file_new_frame.pack(fill='both', expand=1)
    my_label = Label(file_new_frame, text='NEW').pack()


def edit_cut():
    hide_all_frames()
    edit_cut_frame.pack(fill='both', expand=1)
    my_label = Label(edit_cut_frame, text='CUT').pack()

    dummy_button = Button(edit_cut_frame, text='fake').pack(pady=10)
    child_label = Label(edit_cut_frame, text=edit_cut_frame.winfo_children())
    child_label.pack(pady=10)

    # print(edit_cut_frame.winfo_children()))


# Hide all Frames
def hide_all_frames():
    # Loop through children in each frame and destroy them
    for widget in file_new_frame.winfo_children():
        widget.destroy()

    for widget in edit_cut_frame.winfo_children():
        widget.destroy()

    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()


# create a Menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=file_new)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

# Create an Edit menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut', command=edit_cut)
edit_menu.add_command(label='Copy', command=our_command)

# Create an Option menu item
option_menu = Menu(my_menu)
my_menu.add_cascade(label='Options', menu=option_menu)
option_menu.add_command(label='Find', command=our_command)
option_menu.add_command(label='Find Next', command=our_command)

# Create Frames
file_new_frame = Frame(root, width=400, height=400, bg='red')
edit_cut_frame = Frame(root, width=400, height=400, bg='blue')

root.mainloop()
