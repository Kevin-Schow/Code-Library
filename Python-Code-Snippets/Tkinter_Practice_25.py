from tkinter import *

root = Tk()
root.title('Canvas')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('500x500')

my_canvas = Canvas(root, width=300, height=200, bg='white')
my_canvas.pack(pady=20)

# rectangle coordinates = top left, bottom right
my_canvas.create_rectangle(50, 150, 250, 50, fill='blue')

# my_canvas.create_line(x1, y1, x2, y2, fill='color')
my_canvas.create_line(0, 100, 300, 100, fill='red')
my_canvas.create_line(150, 0, 150, 200, fill='purple')

my_canvas.create_oval(50, 150, 250, 50, fill='cyan')




root.mainloop()
