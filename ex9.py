import random

num = random.randint(1, 9)
count = 0

# GOES ON FOREVER UNTIL USER TYPES 'EXIT'
# while True:
#
#     guess = (input("What's your guess?"))
#
#     if guess == 'exit':
#         print("Bye!")
#         break
#
#     else:
#         guess = int(guess)
#         guessedNum = False
#
#         if guess < num:
#             print("That's a little too low" + '\n')
#             count += 1
#         elif guess > num:
#             print("That's a little too high" + '\n')
#             count += 1
#         elif guess == num:
#             print("You guessed it!" + '\n')
#             guessedNum = True
#
#         if guessedNum == True:
#             num = random.randint(1, 9)

# ONLY 1 ROTATION BUT COUNTS NO. OF GUESSES
while (True):

    guess = (input("What's your guess?"))

    # 1
    if guess == 'exit':
        break

    # blah blah blah
    elif num == int(guess):
        count += 1
        print("You guessed it!" + '\n')
        break
    elif int(guess) > num:
        count += 1
        print("That's a little too high" + '\n')
    else:
        count += 1
        print("That's a little too low" + '\n')


print('You have typed {} guesses '.format(count))
