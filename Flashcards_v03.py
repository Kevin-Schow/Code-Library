from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random

root = Tk()
root.title('Geography Flashcards')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('500x600')


# Create Flashcard Randomization
def math_random():
    # generate random number
    global num_1
    global num_2
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    global add_image1
    global add_image2
    card1 = 'c:/Users/haugl/PycharmProjects/TutorialPlayground/Flashcard Numbers/' + str(num_1) + '.png'
    card2 = 'c:/Users/haugl/PycharmProjects/TutorialPlayground/Flashcard Numbers/' + str(num_2) + '.png'
    add_image1 = ImageTk.PhotoImage(Image.open(card1))
    add_image2 = ImageTk.PhotoImage(Image.open(card2))

    # Put Flashcard Images on Screen
    add_1.config(image=add_image1)
    add_2.config(image=add_image2)


# Create Addition Answer Function
def answer_add():
    answer = num_1 + num_2
    if int(add_answer.get()) == answer:
        response = 'Correct! ' + str(num_1) + ' + ' + str(num_2) + ' = ' + str(answer)
    else:
        response = 'Incorrect. ' + str(num_1) + ' + ' + str(num_2) + ' = ' + str(answer) + ' Not ' + add_answer.get()

    answer_message.config(text=response)
    add_answer.delete(0, 'end')
    math_random()


# Create Addition Math Flashcard Function
def add():
    hide_all_frames()
    add_frame.pack(fill='both', expand=1)

    add_label = Label(add_frame, text='Addition Flashcards', font=('Helvetica', 18)).pack(pady=15)
    pic_frame = Frame(add_frame, width=400, height=300)
    pic_frame.pack()

    # generate random number
    global num_1
    global num_2
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    # Create 3 Labels inside pic frame
    global add_1
    global add_2
    add_1 = Label(pic_frame)
    add_2 = Label(pic_frame)
    math_sign = Label(pic_frame, text='+', font=('Helvetica', 28))

    # Grid Labels
    add_1.grid(row=0, column=0)
    math_sign.grid(row=0, column=1)
    add_2.grid(row=0, column=2)

    global add_image1
    global add_image2
    card1 = 'c:/Users/haugl/PycharmProjects/TutorialPlayground/Flashcard Numbers/' + str(num_1) + '.png'
    card2 = 'c:/Users/haugl/PycharmProjects/TutorialPlayground/Flashcard Numbers/' + str(num_2) + '.png'
    add_image1 = ImageTk.PhotoImage(Image.open(card1))
    add_image2 = ImageTk.PhotoImage(Image.open(card2))

    # Put Flashcard Images on Screen
    add_1.config(image=add_image1)
    add_2.config(image=add_image2)

    # Create Answer Box and Button
    global add_answer
    add_answer = Entry(add_frame, font=('Helvetica', 18))
    add_answer.pack(pady=50)

    add_answer_button = Button(add_frame, text='Answer', command=answer_add)
    add_answer_button.pack()

    global answer_message
    answer_message = Label(add_frame, text='', font=('Helvetica', 18))
    answer_message.pack(pady=20)


# Create Randomizing State Function
def random_state():
    # Create a List of State Names
    global our_states
    our_states = ['alabama', 'alaska', 'arizona', 'arkansas', 'california',
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

    # generate random number
    global rando
    rando = randint(0, len(our_states) - 1)
    state = 'States/' + our_states[rando] + '.png'

    # Create our State Images
    global state_image
    state_image = ImageTk.PhotoImage(Image.open(state))
    show_state.config(image=state_image, bg='aliceblue')


# Create State Capital Answers
def state_capital_answer():
    if capital_radio.get() == our_state_capitals[answer]:
        response = 'Correct! ' + our_state_capitals[answer].title() + ' is the capital of ' + answer.title()
    else:
        response = 'Incorrect. ' + our_state_capitals[answer].title() + ' is the capital of ' + answer.title()
    answer_label_capitals.config(text=response)


# Create  Answer Function
def state_answer():
    answer = answer_input.get()
    answer = answer.replace(' ', '')

    # Determine if our answer is right or wrong
    if answer.lower() == our_states[rando]:
        response = 'Correct!  ' + our_states[rando].capitalize()
    else:
        response = 'Incorrect.  ' + our_states[rando].capitalize()
    answer_label.config(text=response)

    # Clear Entry Box
    answer_input.delete(0, 'end')
    random_state()


# Create States Flashcard Function
def states():
    # Hide Previous Frames
    hide_all_frames()
    state_frame.pack(fill='both', expand=1)
    # my_label = Label(state_frame, text='States').pack()

    '''
    # Create a List of State Names
    global our_states
    our_states = ['alabama', 'alaska', 'arizona', 'arkansas', 'california',
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

    # generate random number
    global rando
    rando = randint(0, len(our_states)-1)
    state = 'States/' + our_states[rando] + '.png'

    # Create our State Images
    global state_image
    state_image = ImageTk.PhotoImage(Image.open(state))
    '''
    global show_state
    show_state = Label(state_frame)
    show_state.pack(pady=15)
    random_state()

    # Create Answer Input Box
    global answer_input
    answer_input = Entry(state_frame, font=('Helvetica', 18), bd=2)
    answer_input.pack(pady=15)

    # Create  a Button to Answer Question
    answer_button = Button(state_frame, text='Answer', command=state_answer)
    answer_button.pack(pady=5)

    # Create Button to Randomize State Images
    rando_button = Button(state_frame, text='Pass', command=states)
    rando_button.pack(pady=10)

    # Create a Label to tell if correct or not
    global answer_label
    answer_label = Label(state_frame, text='', font=('Helvetica', 18), bg='aliceblue')
    answer_label.pack(pady=15)


# Create State Capitals Flashcard Function
def state_capitals():
    # Hide Previous Frames
    hide_all_frames()
    state_capitals_frame.pack(fill='both', expand=1)
    # my_label = Label(state_capitals_frame, text='Capitals').pack()

    global show_state
    show_state = Label(state_capitals_frame)
    show_state.pack(pady=15)

    global our_states
    our_states = ['alabama', 'alaska', 'arizona', 'arkansas', 'california',
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

    global our_state_capitals
    our_state_capitals = {
        'alabama': 'montgomery',
        'alaska': 'juneau',
        'arizona': 'phoenix',
        'arkansas': 'littlerock',
        'california': 'sacramento',
        'colorado': 'denver',
        'connecticut': 'hartford',
        'delaware': 'dover',
        'florida': 'tallahassee',
        'georgia': 'atlanta',
        'hawaii': 'honolulu',
        'idaho': 'boise',
        'illinois': 'springfield',
        'indiana': 'indianapolis',
        'iowa': 'desmoines',
        'kansas': 'topeka',
        'kentucky': 'frankfort',
        'louisiana': 'batonrouge',
        'maine': 'augusta',
        'maryland': 'annapolis',
        'massachusetts': 'boston',
        'michigan': 'lansing',
        'minnesota': 'saintpaul',
        'mississippi': 'jackson',
        'missouri': 'jeffersoncity',
        'montana': 'helena',
        'nebraska': 'lincoln',
        'nevada': 'carsoncity',
        'newhampshire': 'concord',
        'newjersey': 'trenton',
        'newmexico': 'santafe',
        'newyork': 'albany',
        'northcarolina': 'raleigh',
        'northdakota': 'bismarck',
        'ohio': 'columbus',
        'oklahoma': 'oklahomacity',
        'oregon': 'salem',
        'pennsylvania': 'harrisburg',
        'rhodeisland': 'providence',
        'southcarolina': 'columbia',
        'southdakota': 'pierre',
        'tennessee': 'nashville',
        'texas': 'austin',
        'utah': 'saltlakecity',
        'vermont': 'montpelier',
        'virginia': 'richmond',
        'washington': 'olympia',
        'westvirginia': 'charleston',
        'wisconsin': 'madison',
        'wyoming': 'cheyenne'
    }

    global rando
    rando = randint(0, len(our_states) - 1)

    # print(our_state_capitals[our_states[rando]])
    global answer
    answer = our_states[rando]

    answer_list = []
    count = 1
    while count < 4:
        rando = randint(0, len(our_states) - 1)
        if count == 1:
            answer = our_states[rando]
            global state_image
            state = 'states/' + our_states[rando] + '.png'
            state_image = ImageTk.PhotoImage(Image.open(state))
            show_state.config(image=state_image)
        answer_list.append(our_states[rando])
        our_states.remove(our_states[rando])
        random.shuffle(our_states)
        count += 1

    random.shuffle(answer_list)

    global capital_radio
    capital_radio = StringVar()
    capital_radio.set(our_state_capitals[answer_list[0]])

    capital_radio_button1 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[0]].title(),
                                        variable=capital_radio, value=our_state_capitals[answer_list[0]]).pack()
    capital_radio_button2 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[1]].title(),
                                        variable=capital_radio, value=our_state_capitals[answer_list[1]]).pack()
    capital_radio_button3 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[2]].title(),
                                        variable=capital_radio, value=our_state_capitals[answer_list[2]]).pack()

    # Add A Pass Button
    pass_button = Button(state_capitals_frame, text='Pass', command=state_capitals)
    pass_button.pack(pady=15)

    # Create Answer Button
    capital_answer_button = Button(state_capitals_frame, text='Answer', command=state_capital_answer)
    capital_answer_button.pack(pady=15)

    # Create Answer Label
    global answer_label_capitals
    answer_label_capitals = Label(state_capitals_frame, text='', font=('helvetica', 18))
    answer_label_capitals.pack(pady=15)


# Hide all previous frames
def hide_all_frames():
    # Loop through and destroy children
    for widget in state_frame.winfo_children():
        widget.destroy()
    for widget in state_capitals_frame.winfo_children():
        widget.destroy()
    for widget in add_frame.winfo_children():
        widget.destroy()

    add_frame.pack_forget()
    state_frame.pack_forget()
    state_capitals_frame.pack_forget()


# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create menu items
states_menu = Menu(my_menu)
my_menu.add_cascade(label='Geography', menu=states_menu)
states_menu.add_command(label='States', command=states)
states_menu.add_command(label='State Capitals', command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label='Exit', command=root.quit)

# Math Flashcard Menu
math_menu = Menu(my_menu)
my_menu.add_cascade(label='Math', menu=math_menu)
math_menu.add_command(label='Addition', command=add)

# Create Frames
state_frame = Frame(root, width=500, height=500, bg='aliceblue')
state_capitals_frame = Frame(root, width=500, height=500)

# Addition Frame
add_frame = Frame(root, width=500, height=500)

root.mainloop()
