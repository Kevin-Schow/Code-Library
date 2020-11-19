# Regular Expression code VS non Regex code for finding a phone number

import re
message = 'Call me at 415-555-1234 tomorrow, or at 415-555-9999 the next day.'

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phone_num_regex.findall(message))

# ================================================================

def is_phone_number(text): # 415-555-1234
    if len(text) != 12:
        return False #Not phone number sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # No area code
        if text[3] != '-':
            return False #Missing dash
        for i in range (4, 7):
            if not text[i].isdecimal():
                return False #No first 3 digits
        if text[7] != '-':
            return False  # Missing second dash
        for i in range (8, 12):
            if not text[i].isdecimal():
                return False  # Missing last 4 digits
        return True


message = 'Call me at 415-555-1234 tomorrow, or at 415-555-9999 the next day.'
foundNumber = False
for i in range (len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')
