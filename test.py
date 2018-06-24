import random

rNumber = random.randint(1, 9)
count = 0

while(True):
    # asking the user to guess the number
    guessNumber = input("Please, type your guess number or 'exit' to stop the game: ")

    # verifying if the user wants to stop
    if guessNumber == 'exit':
        break

    # validating the user guess
    elif rNumber == int(guessNumber):
        count += 1
        print("Congratulations! You have typed {} and the random number is {}".format(guessNumber, rNumber))
        break
    elif int(guessNumber) > rNumber:
        count += 1
        print("Error! Your guess number {} is too high, please try a smaller number".format(guessNumber))
    else:
        count += 1
        print("Error! Your guess number {} is too low, please try a higher number".format(guessNumber))

# verifying how many guesses the user typed and the random number
print('You have typed {} guesses '.format(count))
print('The random number was {}'.format(rNumber))
