numberInput = input("What is the number?")
number = int(numberInput)

if not (number.isdigit()):
    if number == 0:
        print("This number is neither even nor odd")
    elif number % 2 == 0:
        print("The number is even")
    elif number % 2 == 1:
        print("The number is odd")
    else:
        print("Please input a valid number")
else:
    print("Please input a valid number")
