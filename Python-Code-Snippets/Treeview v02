from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Treeview')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('500x600')


def add_record():
    global count
    my_tree.insert(parent='', index='end', iid=count, text='', values=(name_box.get(), id_box.get(), favorite_box.get()))
    count += 1

    # Clear Boxes
    name_box.delete(0, END)
    id_box.delete(0, END)
    favorite_box.delete(0, END)


def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)


def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)


def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)


my_tree = ttk.Treeview(root)

# Define Our Columns
my_tree['columns'] = ('Name', 'ID', 'Favorite')

# Format Columns
my_tree.column('#0', width=0, stretch=NO)
my_tree.column('Name', anchor=W, width=140)
my_tree.column('ID', anchor=CENTER, width=100)
my_tree.column('Favorite', anchor=W, width=140)

# Create Headings
my_tree.heading('#0', text='', anchor=W)
my_tree.heading('Name', text='Name', anchor=W)
my_tree.heading('ID', text='ID', anchor=CENTER)
my_tree.heading('Favorite', text='Favorite', anchor=W)

# Add Data
data = [
    ['Anne', 1, 'Oysters'],
    ['Kevin', 2, 'Sushi'],
    ['Mark', 3, 'Chicken'],
    ['Katie', 4, 'Cupcakes'],
    ['Trine', 5, 'Pizza']
]

global count
count = 0
for record in data:
    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]))
    count += 1


# Add Data
# my_tree.insert(parent='', index='end', iid=0, text='', values=('Anne', 1, 'Oysters'))
# my_tree.insert(parent='', index='end', iid=1, text='', values=('Kevin', 2, 'Sushi'))
# my_tree.insert(parent='', index='end', iid=2, text='', values=('Mark', 3, 'Chicken'))
# my_tree.insert(parent='', index='end', iid=3, text='', values=('Katie', 4, 'Cupcakes'))
# my_tree.insert(parent='', index='end', iid=4, text='', values=('Trine', 5, 'Pizza'))
# my_tree.insert(parent='', index='end', iid=5, text='', values=('Nicolai', 6, 'Burgers'))

# Add Child Data
# my_tree.insert(parent='', index='end', iid=6, text='', values=('Leif', 1.2, 'Reindeer'))
# my_tree.move('6', '0', '0')

# Pack To Screen
my_tree.pack(pady=20)

add_frame = Frame(root)
add_frame.pack(pady=20)

# Labels
nl = Label(add_frame, text='Name')
nl.grid(row=0, column=0)

il = Label(add_frame, text='ID')
il.grid(row=0, column=1)

tl = Label(add_frame, text='Favorite')
tl.grid(row=0, column=2)

# Entry Boxes
name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame)
id_box.grid(row=1, column=1)

favorite_box = Entry(add_frame)
favorite_box.grid(row=1, column=2)

# Buttons
add_record = Button(root, text='Add Record', command=add_record)
add_record.pack(pady=20)

remove_all = Button(root, text='Remove All Records', command=remove_all)
remove_all.pack(pady=10)

remove_one = Button(root, text='Remove One Selected', command=remove_one)
remove_one.pack(pady=10)

remove_many = Button(root, text='Remove Many Selected', command=remove_many)
remove_many.pack(pady=10)

root.mainloop()
