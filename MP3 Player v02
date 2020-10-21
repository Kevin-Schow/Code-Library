from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title('Sound')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('600x400')

# Initialize Pygame Mixer
pygame.mixer.init()

# Add Song Function
def add_song():
    song = filedialog.askopenfilename(initialdir='C:/Users/haugl/PycharmProjects/TutorialPlayground/Audio/', title='Choose A Song', filetypes=(('mp3 Files', '*.mp3'), ))

    # Strip Directory Info and .mp3 Extension
    song = song.replace('C:/Users/haugl/PycharmProjects/TutorialPlayground/Audio/', '')
    song = song.replace('.mp3', '')

    # Add Song to List Box
    song_box.insert(END, song)

# Add Many Songs to Playlist
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='C:/Users/haugl/PycharmProjects/TutorialPlayground/Audio/', title='Choose A Song', filetypes=(('mp3 Files', '*.mp3'), ))

    # Loop thru song list and replace directory info and .mp3
    for song in songs:
        song = song.replace('C:/Users/haugl/PycharmProjects/TutorialPlayground/Audio/', '')
        song = song.replace('.mp3', '')
        song_box.insert(END, song)


# Play Selected Song
def play():
    song = song_box.get(ACTIVE)
    song = f'C:/Users/haugl/PycharmProjects/TutorialPlayground/Audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

# Stop Playing Current Song
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

# Create Global Pause Variable
global paused
paused = False

# Pause and Unpause the Current Song
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        # Unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        # Pause
        pygame.mixer.music.pause()
        paused = True


# Create Playlist Box
song_box = Listbox(root, bg='black', fg='green', width=60, selectbackground='gray', selectforeground='black')
song_box.pack(pady=20)

# Define Player Control Buttons Images
back_button_img = PhotoImage(file='c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/Icons/back.png')
forward_button_img = PhotoImage(file='c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/Icons/forward.png')
play_button_img = PhotoImage(file='c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/Icons/play.png')
pause_button_img = PhotoImage(file='c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/Icons/pause.png')
stop_button_img = PhotoImage(file='c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/Icons/stop.png')

# Create Player Control Frame
controls_frame = Frame(root)
controls_frame.pack()

# Create Player Control Buttons
back_button = Button(controls_frame, image=back_button_img,  borderwidth=0)
forward_button = Button(controls_frame, image=forward_button_img,  borderwidth=0)
play_button = Button(controls_frame, image=play_button_img,  borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_button_img,  borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_button_img,  borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=2)
forward_button.grid(row=0, column=1, padx=2)
play_button.grid(row=0, column=2, padx=2)
pause_button.grid(row=0, column=3, padx=2)
stop_button.grid(row=0, column=4, padx=2)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label='Add Songs', menu=add_song_menu)
add_song_menu.add_command(label='Add One Song to Playlist', command=add_song)
# Add Many Songs to Playlist
add_song_menu.add_command(label='Add Many Songs to Playlist', command=add_many_songs)



root.mainloop()
