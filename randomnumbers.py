 # random numbers!

import random
import numpy as np
# pip install numpy

number = random.randint(1, 20)
print(number)


# generate 100 random numbers
# put them in a list
# print

listofrandomnumbers = []
for i in range(100):
    n = random.randint(1,20)
    listofrandomnumbers.append(n)

print(listofrandomnumbers)

list2 = [random.randint(1, 20) for i in range(99)]
print(list2)
print("length of list2 is", len(list2))

# compute the sum of them
total=0 # listofrandomnumbers[0] + listofrandomnumebrs[1]+........+listofrandomnumbers[100]
for number in listofrandomnumbers:
    total = total + number
#
print("total: ", total)
totalsum = sum(listofrandomnumbers)


# npnumber = np.random.