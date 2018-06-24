num = int(input("Choose any number: "))
numArray = range(1, num)
divisArray = []

for i in numArray:
    if num % i == 0:
        divisArray.append(i)
    else:
        continue

print(divisArray)
