from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()
root.title('Sound')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('600x550')

# Initialize Pygame Mixer
pygame.mixer.init()

#  Grab  Song Length Time Info
def play_time():
    # Grab Current Elapsed Time of Song
    current_time = pygame.mixer.music.get_pos() / 1000
    # Convert to Time Format
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

    # Get Current Song Tuple Number
    # current_song = song_box.curselection()
    # Grab Song Title from  Playlist
    song = song_box.get(ACTIVE)  # Was 'current_song'
    # Add Directory and .mp3 to Song title
    song = f'C:/Users/haugl/PycharmProjects/TutorialPlayground/Audio/{song}.mp3'

    # Load Song with Mutagen
    song_mut = MP3(song)
    # Get Song Length
    global song_length
    song_length = song_mut.info.length
    # Convert to Time Format
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    # Output Time to Status Bar
    status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}    ')
    # Update Slider Position Value to Current Song Position
    my_slider.config(value=int(current_time))
    # Update Time every second
    status_bar.after(1000, play_time)



# Add Song Function
def add_song():
    song = filedialog.askopenfilename(initialdir='C:/Users/haugl/PycharmProjects/TutorialPlayground/Audio/',
                                      title='Choose A Song', filetypes=(('mp3 Files', '*.mp3'),))

    # Strip Directory Info and .mp3 Extension
    song = song.replace('C:/Users/haugl/PycharmProjects/TutorialPlayground/Audio/', '')
    song = song.replace('.mp3', '')

    # Add Song to List Box
    song_box.insert(END, song)


# Add Many Songs to Playlist
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='C:/Users/haugl/PycharmProjects/TutorialPlayground/Audio/',
                                        title='Choose A Song', filetypes=(('mp3 Files', '*.mp3'),))

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

    # Call play_time function to get song length
    play_time()

    # Update Slider to Position
    slider_position = int(song_length)
    my_slider.config(to=slider_position, value=0)


# Stop Playing Current Song
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    # Clear Status Bar
    status_bar.config(text='')


# Play the Next Song in the Playlist
def next_song():
    # Get Current Song Tuple Number
    next_one = song_box.curselection()
    # Add One to Current Song Number
    next_one = next_one[0] + 1
    # Grab Song Title from  Playlist
    song = song_box.get(next_one)
    # Add Directory and .mp3 to Song title
    song = f'C:/Users/haugl/PycharmProjects/TutorialPlayground/Audio/{song}.mp3'
    # Load and Play Song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # Clear Active Bar In Playlist
    song_box.selection_clear(0, END)
    # Make Next Song  Active
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)


# Play Previous Song in Playlist
def previous_song():
    # Get Current Song Tuple Number
    next_one = song_box.curselection()
    # Add One to Current Song Number
    next_one = next_one[0] - 1
    # Grab Song Title from  Playlist
    song = song_box.get(next_one)
    # Add Directory and .mp3 to Song title
    song = f'C:/Users/haugl/PycharmProjects/TutorialPlayground/Audio/{song}.mp3'
    # Load and Play Song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # Clear Active Bar In Playlist
    song_box.selection_clear(0, END)
    # Make Next Song  Active
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)


# Delete A Song
def delete_song():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()


# Delete All Songs
def delete_all_songs():
    song_box.delete(0, END)
    pygame.mixer.music.stop()


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

# Create Slider Function
def slide(x):
    slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')

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
back_button = Button(controls_frame, image=back_button_img, borderwidth=0, command=previous_song)
forward_button = Button(controls_frame, image=forward_button_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_button_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_button_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_button_img, borderwidth=0, command=stop)

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

# Create Delete Song Menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label='Remove Songs', menu=remove_song_menu)
remove_song_menu.add_command(label='Delete A Song From Playlist', command=delete_song)
remove_song_menu.add_command(label='Delete All Songs From Playlist', command=delete_all_songs)

# Create Status Bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Create Music Position Slider
my_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.pack(pady=30)

# Create Temporary Slider Label
slider_label = Label(root, text='0')
slider_label.pack(pady=10)

root.mainloop()
