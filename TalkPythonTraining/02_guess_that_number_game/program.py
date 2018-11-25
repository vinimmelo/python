import random

print('-----------------------------------')
print('       GUESS THAT NUMBER GAME')
print('-----------------------------------')

the_number = random.randint(0, 100)

player = input("Player, what's your name? ")
guess = -50

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)
    if guess < the_number:
        print("Sorry {1}, your guess of {0} was too LOW".format(guess, player))
    elif guess > the_number:
        print("Sorry {1}, your guess of {0} was too HIGH".format(guess, player))
    else:
        print("Excelent work {1}, you won, it was {0}.".format(guess, player))

print('Done!')

