# WHEN NUMBERS ARE GIVEN
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# print([i for i in a if i in b])


# RANDOMLY GENERATED NUMBERS
import random

aa = random.sample(range(100), 25)
bb = random.sample(range(100), 20)

print([i for i in aa if i in bb])
