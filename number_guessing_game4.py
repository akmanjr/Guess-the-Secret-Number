
"""
number_guessing_game4.py
This is a game, where the user is asked to guess the number which the computer picks randomly.
In version 1.1, "Ask to Play Again" functionality is added.
In version 1.2, "Max Number of Tries" and "Instructions" functionality is added.
In this version, the name of the game adjusted, "Score Keeping" functionality added.
@author: Can Akman @ the Laboratory
@version: 11.01.2018_v1.4
"""

import random

print("Welcome to the Find the Secret Number Game!")
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
playerScore = 0
computerScore = 0

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
		print("Good job!. You found the secret number in " + str(numberOfGuesses) + " tries.")
		playerScore += 1
	else:
		print("You have exceeded the maximum number of tries.")
		computerScore += 1

	#Ask the user if they want to play again
	userPlayInput = input("Play again (y/n)? ")
	if userPlayInput == "y":
		playGame = True
	if userPlayInput == "n":
		break

#Bye message, if user does not want to play again		
print("Player: " + str(playerScore))
print("Computer: " + str(computerScore))
if playerScore > computerScore:
	print("You beat the computer!")
elif playerScore < computerScore:
	print("Sorry, the computer won. You need to try harder next time.")
else:
	print("It is a draw.")
print("Thanks for playing. Bye!")