from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from random import randint

root = Tk()
root.title('Random Winner Picker')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('400x400')


def pick():
    entries = ['Kevin', 'Anne', 'Casey', 'Mark', 'Katie', 'Donovan', 'Katerbrie']
    entries_set = set(entries)
    unique_entries = list(entries_set)
    our_number = len(unique_entries) - 1
    rando = randint(0, our_number)

    winnerLabel = Label(root, text=unique_entries[rando], font=('Helvetica', 18))
    winnerLabel.pack(pady=50)


topLabel = Label(root, text='Winner!', font=('Helvetica', 24))
topLabel.pack(pady=20)

winButton = Button(root, text='Pick a Winner!', font=('Helvetica', 24), command=pick)
winButton.pack(pady=20)

root.mainloop()
