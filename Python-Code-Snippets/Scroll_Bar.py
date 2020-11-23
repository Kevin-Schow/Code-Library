from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Scroll Bar')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('500x400')

# Create A Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scroll Bar to Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure the Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))

# Create Another Frame Inside Canvas
second_frame = Frame(my_canvas)

# Add that New Frame To A Window In The Canvas
my_canvas.create_window((0,0), window=second_frame, anchor='nw')

for thing in range(100):
    Button(second_frame, text=f'Button {thing}').grid(row=thing, column=0, pady=10, padx=10)





root.mainloop()
