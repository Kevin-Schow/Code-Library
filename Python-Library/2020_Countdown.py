from tkinter import *
from datetime import date

root = Tk()
root.title('2020 Countdown')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('500x300')

panic = Label(root, text="DON'T PANIC!", font=('Helvetica', 42), bg='black', fg='green')
panic.pack(pady=20, ipadx=10, ipady=10)

# Get Date
today = date.today()
# Format Date
f_today = today.strftime("%A, %B %d, %Y")
# Output Date
today_label = Label(root, text=f'Today is {f_today}', font=('Helvetica', 16))
today_label.pack(pady=20)

# Countdown
days_in_year = 365
todays_day_number = int(today.strftime("%j"))

# Calculate Days Left In Year
days_left = days_in_year - todays_day_number

# Output Days Left
countdown_label = Label(root, text=f'There are {days_left} days left in 2020.', font=('Helvetica', 20))
countdown_label.pack(pady=20)


root.mainloop()