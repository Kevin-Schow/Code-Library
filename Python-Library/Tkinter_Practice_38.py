from tkinter import *
import pygame

root = Tk()
root.title('Sound')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('600x400')

pygame.mixer.init()

def play():
    pygame.mixer.music.load('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/alien.wav')
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()

my_button = Button(root, text='Play Song', font=('Helvetica', 32), command=play)
my_button.pack(pady=20)

stop_button = Button(root, text='Stop', command=stop)
stop_button.pack(pady=20)



root.mainloop()
