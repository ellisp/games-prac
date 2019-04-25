
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

want_to_play = True

while want_to_play:

    number = random.randint(1, 20)
    print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

    for guessesTaken in range(6):
        print('Take a guess.')
        guess = input()
        guess = int(guess)

        if guess < number:
            print('Your guess is too low.')

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken + 1)
        print('Good job, ' + myName + '! You guesed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number) + '.')

    print('Want to play again?')
    ans = input()
    if ans == 'No':
        want_to_play = False
        
    
