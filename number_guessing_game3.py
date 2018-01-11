
"""
number_guessing_game3.py
This is a game, where the user is asked to guess the number which the computer picks randomly.
In version 1.1, "Ask to Play Again" functionality is added.
In this version, "Max Number of Tries" and "Instructions" functionality is added.
@author: Can Akman @ the Laboratory
@version: 11.01.2018_v1.3
"""

import random

print("Welcome to the Guess the Number Game!")
print("""
INSTRUCTIONS:
------------------------------------------------------------------------

 * Computer will randomly pick a secret number between 1 and 25.
 * You have total of 5 tries to guess the number.
 * Computer will hint you where your guess stands vs the secret number.

------------------------------------------------------------------------
""")

#Set up the game variable(s)
numberOfGuesses = 0
playGame = True

#Set up the game loop
while playGame:
	randomNumber = random.randint(1, 10)
	userGuess = eval(input("Please take a guess: "))
	numberOfGuesses = 1

	while userGuess != randomNumber and numberOfGuesses < 5:
		if userGuess > randomNumber:
			numberOfGuesses += 1
			userGuess = eval(input("Your guess is higher than my number. Make another guess: " ))
		if userGuess < randomNumber:
			numberOfGuesses += 1
			userGuess = eval(input("Your guess is lower than my number. Make another guess: "))

	if userGuess == randomNumber:
		print("Good job!. You guessed my number in " + str(numberOfGuesses) + " tries.")
	else:
		print("You have exceeded the maximum number of tries.")
		break

	#Ask the user if they want to play again
	userPlayInput = input("Play again (y/n)? ")
	if userPlayInput == "y":
		playGame = True
	if userPlayInput == "n":
		break

#Bye message, if user does not want to play again		
print("Thanks for playing. Bye!")

