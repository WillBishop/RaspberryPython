#############################################################################
###                                                                       ###
### A number guessing game in Python.                                     ###
### Copyright (C) 2016  lenku                                             ###
###                                                                       ###
### This program is free software: you can redistribute it and/or modify  ###
### it under the terms of the GNU General Public License as published by  ###
### the Free Software Foundation, either version 3 of the License, or     ###
### (at your option) any later version.                                   ###
###                                                                       ###
### This program is distributed in the hope that it will be useful,       ###
### but WITHOUT ANY WARRANTY; without even the implied warranty of        ###
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         ###
### GNU General Public License for more details.                          ###
###                                                                       ###
### You should have received a copy of the GNU General Public License     ###
### along with this program.  If not, see <http://www.gnu.org/licenses/>. ###
###                                                                       ###
#############################################################################

### IMPORTS
import random

### VARIABLES
# No variables

# intro
print('Welcome! Who might you be?')
# get user's desired name
username = input()
print()
print('Well, ' + username + ', we are going to play a guessing game.')

# begin playing
play = 'y'
while play == 'y' or play == 'yes':

    print()

    guesses = 0
    # get first number
    while True:
        try:
            print('Enter a number:')
            number1 = int(input())
            break
        # handle string to integer exception
        except ValueError:
            print('That\'s not a number... Try again.')

    # get second number
    while True:
        try:
            print('Enter a second number:')
            number2 = int(input())
            break
        # handle string to integer exception
        except ValueError:
            print('That\'s not a number... Try again.')

    print()

    # pick random number between 2 numbers chosen by user
    if number1 < number2:
        number = random.randint(number1, number2)
        print('Okay, ' + username + ', I am thinking of a number.')
        print('It is between ' + str(number1) + ' and ' + str(number2) + '.')
    else:
        number = random.randint(number2, number1)
        print('Okay, ' + username + ', I am thinking of a number.')
        print('It is between ' + str(number2) + ' and ' + str(number1) + '.')

    print()

    # allow user to guess as long as the number of guesses is no more than 5
    while guesses < 5:
        try:
            print('Take a guess:')
            guess = int(input())
            guesses += 1
            if guess > number:
                print('Your guess is too high.')
            elif guess < number:
                print('Your guess is too low.')
            # if the guess was equal to the number
            else:
                break
        # handle string to integer exception
        except ValueError:
            print('That\'s not a number... Try again.')

    print()

    # if the user's guess was correct
    if guess == number:
        print('Congratulations, ' + username + '!')
        if guesses != 1:
            print('You guessed the number in ' + str(guesses) + ' guesses!')
        else:
            print('You guessed the number in 1 guess!')
    # if the user did not guess the number
    else:
        print('Your 5 guesses are up and you didn\'t guess the number...')
        print('Better luck next time!')

    # ask to play again
    while True:
        print('Would you like to play again? (yes/no)')
        # set input to lowercase
        play = input().lower()
        if play != 'y' and play != 'yes' and play != 'n' and play != 'no':
            print('That\'s not the answer I\'m looking for...')
        else:
            break

# exit
print()

print('Thank you for playing, ' + username + '!')
print('See you next time!')
