def isPrime():
    num = int(input("Choose a number: "))
    numArray = range(1, num)

    for i in numArray:
        numVal = True
        if num % i == 0:
            numVal = False
        else:
            continue

    if numVal == True:
        print("That's a prime number!")
    else:
        print("That's a composite number")


isPrime()
