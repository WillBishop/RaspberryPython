#############################################################################
###                                                                       ###
### A number guessing game in Python.                                     ###
### Copyright (C) 2017 lenku                                              ###
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
# get user's desired name
username = input('Welcome! Who might you be?\n')
print('\nWell %s, we are going to play a guessing game. You will type in 2 numbers, and that will be the guessing range.' % username)

# begin playing
play = 'y'
while play[0] == 'y':

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
            print("That's not a number... Try again.")

    # get second number
    while True:
        try:
            print('Enter a second number:')
            number2 = int(input())
            break
        # handle string to integer exception
        except ValueError:
            print("That's not a number... Try again.")

    print()

    # pick random number between 2 numbers chosen by user
    if number1 < number2:
        number = random.randint(number1, number2)
        print('Okay, %s, I am thinking of a number.\nIt is between %d and %d.' % (username, number1, number2))
    else:
        number = random.randint(number2, number1)
        print('Okay, ' + username + ', I am thinking of a number.')
        print('It is between ' + str(number2) + ' and ' + str(number1) + '.')


    # allow user to guess as long as the number of guesses is no more than 5
    while guesses < 5:
        try:
            print('\nTake a guess:')
            guess = int(input())
            guesses += 1
            if guess > number:
                print('\nYour guess is too high.\nYou have %d guesses left!' % (5 - guesses))
            elif guess < number:
                print('\nYour guess is too low.\nYou have %d guesses left!' % (5 - guesses))
            # if the guess was equal to the number
            else:
                break
        # handle string to integer exception
        except ValueError:
            print("That's not a number... Try again.")

    # if the user's guess was correct
    if guess == number:
        print('\nCongratulations, %s!' % username)
        if guesses != 1:
            print('You guessed the number in %d guesses!' % guesses)
        else:
            print('You guessed the number in 1 guess!')
    # if the user did not guess the number
    else:
        print("\nYour 5 guesses are up and you didn't guess the number...\nThe number was %d!\nBetter luck next time!" % number)

    # ask to play again
    while True:
        print('\nWould you like to play again? (yes/no)')
        # set input to lowercase
        play = input().lower()
        if play[0] != 'y' and play[0] != 'n':
            print("That's not the answer I'm looking for...")
        else:
            break

print('\nThank you for playing, %s\nSee you next time!' % username)
