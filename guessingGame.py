# this is a number guessing game
import random
secretNumber =random.randint(1,20)
print("hey there I Want you to guess a number between 1 to 20")
for guessesTaken in range(1,5):
    print("take a guess")
    guess = int(input())
    if guess < secretNumber:
        print("guess is too low ")
    elif guess > secretNumber:
        print("guess is too high")
    else:
        break

if guess == secretNumber:
        print("Good job! you guessed my number in " + str(guessesTaken) + "guesses")
else:
        print("Nope! the secret numbers was" + str(secretNumber))
