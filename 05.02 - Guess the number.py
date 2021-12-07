#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <center><img src='../../BlueSoft_logo.png' width="500" height="208"/></center>
# 
# ___

# # Guess the number challenge
# 
# *Guess the Number* is a classic game for beginners to practice basic programming techniques.
# 
# In this game, the computer thinks of a random number between `1` and `100`. The player has `10` chances to guess the number.
# 
# After each guess, the computer tells the player if it was too high or too low.
# 
# Example:
# ```
# I drew a number between 1 and 100.
# 
# You have 10 guesses left. Take a guess.
# > 50
# Your guess is too high.
# 
# You have 9 guesses left. Take a guess.
# > 25
# Your guess is too low.
# 
# You have 8 guesses left. Take a guess.
# > 37
# Your guess is too low.
# 
# You have 7 guesses left. Take a guess.
# > 42
# Yay! You guessed my number!
# ```

# ## Experimental changes
# 
# After entering the source code and running it a few times, try making experimental changes to it.
# 
# You can also try to figure out how to do the following:
# - Create a *Guess the Letter* variant that gives hints based on the alphabetical order of the player’s guess.
# - Make the hints after each guess say *warmer* or *colder* based on the player’s previous guess.

# In[ ]:


import random

print('Hello, what is your name?')

name = str(input())
answer = random.randint(1, 100)

print('Well, ' + name + ', I am thinking of a number from 1 to 100.')
print('You have only 10 guesses.')
guessesTaken = 0
guessedCorrectAnswer = False

while guessesTaken < 10:
    print('Take a guess.')

    guess = input()
    guessesTaken = guessesTaken + 1

    try:
        if int(guess) == answer:
            guessedCorrectAnswer = True
            print('Good job, ' + name +
                  '! You guessed my number in ' + str(guessesTaken) +
                  (' guess!' if guessesTaken == 1 else ' guesses!'))
            break
        elif int(guess) < answer:
            print('Your guess is too low.')
        else:
            print('Your guess is too high.')
    except ValueError:
        guessesTaken = guessesTaken - 1
        print('You must enter a number.')

if not guessedCorrectAnswer:
    print('Unlucky. The number I was thinking of was ' + str(answer) + '.')


# 
