def palindrome(givenWord):

    givenWord = givenWord.lower()
    length = len(givenWord)
    value = True
    i = 0

    for i in range(length):
        if givenWord[i] != givenWord[length - (1 + i)]:
            value = False

    if value == False:
        print("This word isn't a Palindrome")
    else:
        print("This word is a Palindrome!")


palindrome("deleveled")
