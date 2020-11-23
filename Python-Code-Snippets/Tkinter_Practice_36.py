from tkinter import *

root = Tk()
root.title('Get Current Height and Width')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('600x400')

def info():
    dimension_label = Label(root, text=root.winfo_geometry())
    dimension_label.pack(pady=20)

    height_label = Label(root, text='Height: ' + str(root.winfo_height()))
    height_label.pack(pady=20)
    width_label = Label(root, text='Width: ' + str(root.winfo_width()))
    width_label.pack(pady=20)


my_button = Button(root, text='Click Me', command=info)
my_button.pack(pady=20)




root.mainloop()
