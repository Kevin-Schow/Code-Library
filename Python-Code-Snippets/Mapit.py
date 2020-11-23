# Batch file:
# @py.exe c:Users\<SCRIPT PATH>.py %*
# mapit.bat, mapit.py

# automate the boring stuff
# auto google map search

import webbrowser, sys, pyperclip

sys.argv  # ['mapit.py', '870', 'Valencia', 'St.']

# Check if command line arguements were passed
if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# http://www.google.com/maps/place/<ADDRESS>
webbrowser.open('http://www.google.com/maps/place/' + address)
