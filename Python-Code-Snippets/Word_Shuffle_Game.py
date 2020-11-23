from tkinter import *
from random import choice
from random import shuffle

root = Tk()
root.title('Word Shuffle Game')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('600x400')

my_label = Label(root, text='', font=('Helvetica', 48))
my_label.pack(pady=20)

def shuffler():

    states = ['alabama', 'alaska', 'arizona', 'arkansas', 'california',
              'colorado', 'connecticut', 'delaware', 'florida',
              'georgia', 'hawaii', 'idaho', 'illinois', 'indiana',
              'iowa', 'kansas', 'kentucky', 'louisiana', 'maine',
              'maryland', 'massachusetts', 'michigan', 'minnesota',
              'mississippi', 'missouri', 'montana', 'nebraska',
              'nevada', 'newhampshire', 'newjersey', 'newmexico',
              'newyork', 'northcarolina', 'northdakota', 'ohio',
              'oklahoma', 'oregon', 'pennsylvania', 'rhodeisland',
              'southcarolina', 'southdakota', 'tennessee',
              'texas', 'utah', 'vermont', 'virginia', 'washington',
              'westvirginia', 'wisconsin', 'wyoming']

    global word
    word = choice(states)
    my_label.config(text=word)

    break_apart_word = list(word)
    shuffle(break_apart_word)

    global shuffled_word
    shuffled_word = ''

    for letter in break_apart_word:
        shuffled_word += letter

    my_label.config(text=shuffled_word)

def answer():
    if word == entry_answer.get():
        answer_label.config(text='Correct!')
    else:
        answer_label.config(text='Incorrect.')

entry_answer = Entry(root, font=('Helvetica', 24))
entry_answer.pack(pady=20)

my_button = Button(root, text='Pick another word', command=shuffler)
my_button.pack(pady=20)

answer_button = Button(root, text='Answer', command=answer)
answer_button.pack()

answer_label = Label(root, text='', font=('Helvetica', 18))
answer_label.pack(pady=20)


shuffler()
root.mainloop()
