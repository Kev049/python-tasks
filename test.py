def is_prime(x):
    if x < 2:
        print("Comp")
    else:
        for n in range(2, x - 1):
            if x % n == 0:
                print("Comp")
        print("Prime!")


is_prime(8)
