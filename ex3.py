a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# newArray = [0]
#
# for num in a:
#     if num < 5:
#         newArray.append(num)
# print(newArray)

inputNum = int(input("Choose a number"))

for num in a:
    if num < inputNum:
        print(num)
    else:
        continue
