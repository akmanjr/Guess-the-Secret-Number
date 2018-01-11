
"""
number_guessing_game.py
This is a game, where the user is asked to guess the number which the computer picks randomly.
@author: Can Akman @ the Laboratory
@version: 11.01.2018_v1.0
"""

import random

print("Welcome to the Guess the Number Game!")

#Set up the game variable(s)
numberOfGuesses = 1


#Set up the game loop
randomNumber = random.randint(1, 10)
print(randomNumber)

userGuess = eval(input("Please take a guess: "))
print(userGuess)

while userGuess != randomNumber:
	if userGuess > randomNumber:
		numberOfGuesses += 1
		userGuess = eval(input("Your guess is higher than my number. Make another guess: " ))
	if userGuess < randomNumber:
		numberOfGuesses += 1
		userGuess = eval(input("Your guess is lower than my number. Make another guess: "))

print("Good job!. You guessed my number in " + str(numberOfGuesses) + " tries.")