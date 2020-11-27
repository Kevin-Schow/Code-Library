import random

print('What is your name?')
name = input()

print (f'Well {name}, I am thinking of a number between 1-20.')
secret_number = random.randint(1, 20)

for guesses_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    
    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('your guess is too high.')
    else:
        break  # Correct guess
    
if guess == secret_number:
    print(f'Good job {name}, you guessed my number in {guesses_taken} guesses!')
else:
    print('Incorrect.  My secret number was ' + secret_number)
    print(f'You took {guesses_taken} guesses')
