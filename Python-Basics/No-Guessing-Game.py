import random

ran = random.randint(1, 10)

tries = 0

while True:
    guess = int(input("Guess the number between 1 and 10: "))
    if(guess == ran):
        print("Congratulations! You guessed the number.")
        tries += 1
        break

    elif (guess < ran ):
        print('Too low! Try again.')
        tries += 1

    elif (guess > ran):
        print('Too high! Try again.')
        tries += 1

    else:
        print("Sorry! You guessed the wrong number.")
        tries += 1
        