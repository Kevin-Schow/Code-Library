# Phone and Email Scraper
#! python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(
((\d\d\d) | (\(\d\d\d\)))?    #area code (optional)
(\s|-)                        # first seperator
\d\d\d                        # first 3 digits
-                             # seperator
\d\d\d\d                      # last 4 digits
(((ext(\.)?\s)|x)             # extension word(optional)
(\d{2,5}))?                   # extension number(optional)
)
''', re.VERBOSE)

# Create a regex for emails
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+               # name
@                             # @ symbol
[a-zA-Z0-9_.+]+               # domain name
''', re.VERBOSE)

# Get text off clipboard
text = pyperclip.paste()

# extract email/phone from the text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email.phone from clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
