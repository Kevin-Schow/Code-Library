from tkinter import *
from PIL import ImageTk, Image
from random import randint

root = Tk()
root.title('Geography Flashcards')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('500x600')


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
    my_label = Label(state_capitals_frame, text='Capitals').pack()


# Hide all previous frames
def hide_all_frames():
    # Loop through and destroy children
    for widget in state_frame.winfo_children():
        widget.destroy()
    for widget in state_capitals_frame.winfo_children():
        widget.destroy()
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

# Create Frames
state_frame = Frame(root, width=500, height=500, bg='aliceblue')
state_capitals_frame = Frame(root, width=500, height=500)

root.mainloop()
