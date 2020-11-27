import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Kevin Schow'
email['to'] = 'Kevinschow@gmail.com'
email['subject'] = 'Test Email'

email.set_content('Hello and welcome to our subscriber list!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('Kevinschow@gmail.com', 'password')
    smtp.send_message(email)
    print('Email Sent!')
