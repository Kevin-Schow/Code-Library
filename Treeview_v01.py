from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Treeview')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('500x500')


my_tree = ttk.Treeview(root)

# Define Our Columns
my_tree['columns'] = ('Name', 'ID', 'Favorite')

# Format Columns
my_tree.column('#0', width=0, stretch=NO)
my_tree.column('Name', anchor=W, width=120)
my_tree.column('ID', anchor=CENTER, width=80)
my_tree.column('Favorite', anchor=W, width=120)

# Create Headings
my_tree.heading('#0', text='', anchor=W)
my_tree.heading('Name', text='Name', anchor=W)
my_tree.heading('ID', text='ID', anchor=CENTER)
my_tree.heading('Favorite', text='Favorite', anchor=W)

# Add Data
my_tree.insert(parent='', index='end', iid=0, text='', values=('Anne', 1, 'Oysters'))
my_tree.insert(parent='', index='end', iid=1, text='', values=('Kevin', 2, 'Sushi'))
my_tree.insert(parent='', index='end', iid=2, text='', values=('Mark', 3, 'Chicken Nuggets'))
my_tree.insert(parent='', index='end', iid=3, text='', values=('Katie', 4, 'Cupcakes'))
my_tree.insert(parent='', index='end', iid=4, text='', values=('Trine', 5, 'Pizza'))
my_tree.insert(parent='', index='end', iid=5, text='', values=('Nicolai', 6, 'Burgers'))

# Add Child Data
my_tree.insert(parent='', index='end', iid=6, text='', values=('Leif', 1.2, 'Reindeer'))
my_tree.move('6', '0', '0')

# Pack To Screen
my_tree.pack(pady=20)


root.mainloop()
