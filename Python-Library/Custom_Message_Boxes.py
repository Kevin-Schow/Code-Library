from tkinter import *

root = Tk()
root.title('Custom Message Boxes')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('300x300')


def choice(option):
	pop.destroy()
	if option is 'yes':
		my_label.config(text="You Win!")
	if option is 'no':
		my_label.config(text="Ew!")



def clicker():
	global pop
	pop = Toplevel(root)
	pop.title('Popup')
	pop.geometry('250x150')
	pop.configure(bg='green')

	global popup_photoimage
	popup_photoimage = PhotoImage(file='C:/code/Code-Snippets/Python-Code-Snippets/images/fox.png')

	pop_label = Label(pop, text="Do you like animals?", bg='blue', fg='white', font=('helvetica', 18))
	pop_label.pack(pady=10)

	my_frame = Frame(pop, bg='orange')
	my_frame.pack(pady=5)

	popup_image = Label(my_frame, image=popup_photoimage, borderwidth=10)
	popup_image.grid(row=0, column=0, padx=10)

	yes = Button(my_frame, text='Yes', command=lambda: choice('yes'), bg='green')
	yes.grid(row=0, column=1)

	yes = Button(my_frame, text='No', command=lambda: choice('no'), bg='red')
	yes.grid(row=0, column=2)


my_button = Button(root, text='Click Me!', command=clicker)
my_button.pack(pady=50)

my_label = Label(root, text='')
my_label.pack(pady=20)









root.mainloop()