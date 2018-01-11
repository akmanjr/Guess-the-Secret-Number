
"""
number_guessing_game2.py
This is a game, where the user is asked to guess the number which the computer picks randomly.
In this version, "Ask to Play Again" functionality is added.
@author: Can Akman @ the Laboratory
@version: 11.01.2018_v1.1
"""

import random

print("Welcome to the Guess the Number Game!")

#Set up the game variable(s)
numberOfGuesses = 1
playGame = True


#Set up the game loop
while playGame:
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

	#Ask the user if they want to play again
	userPlayInput = input("Play again (y/n)? ")
	if userPlayInput == "y":
		playGame = True
	if userPlayInput == "n":
		break
#Bye message, if user does not want to play again		
print("Thanks for playing. Bye!")

