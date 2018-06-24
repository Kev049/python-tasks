p = input("What's your name?")
p2 = input("What's your name?")

p = p.title()
p2 = p2.title()

while True:

    first = input("Do you want to play? Type y for yes or n for no.")
    first = first.lower()

    if first == 'n':
        print("Bye!")
        break

    elif first == 'y':

        dec1P = input("%s, choose 'rock', 'paper' or 'scissors'" % p)
        dec2P = input("%s, choose 'rock', 'paper' or 'scissors'" % p2)

        dec1P = dec1P.lower()
        dec2P = dec2P.lower()

        if dec1P == dec2P:
            print("No one wins")
            # RUN FUNCTION HERE

        elif dec1P == 'rock':
            if dec2P == 'paper':
                print("%s wins!" % p2)
            elif dec2P == 'scissors':
                print("%s wins!" % p)

        elif dec1P == 'paper':
            if dec2P == 'scissors':
                print("%s wins!" % p2)
            elif dec2P == 'rock':
                print("%s wins!" % p)

        elif dec1P == 'scissors':
            if dec2P == 'rock':
                print("%s wins!" % p2)
            elif dec2P == 'paper':
                print("%s wins!" % p)

        else:
            print("Please choose 'rock', 'paper', or 'scissors'")

    else:
        print("Please type y or n")
