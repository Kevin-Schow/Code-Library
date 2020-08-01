is_proper_password = False

while not is_proper_password:
    is_num = False
    is_alpha = False

    username = input('Enter your username: ')
    password = input('Enter your password: ')
    for symbol in password:
        if symbol.isnumeric():
            is_num = True
        if symbol.isalpha():
            is_alpha = True
    if is_num and is_alpha and (len(password) >= 6):
        is_proper_password = True
    else:
        print('Please enter a proper password with at least one letter and one number.')

hidden_password = ('*' * len(password))

print(f'{username}\'s password {hidden_password} is a proper password.')
