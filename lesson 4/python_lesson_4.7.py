from itertools import count
from math import factorial


def fact():
    for a in count(1):
        yield factorial(a)


x = int(input('Enter: '))
i = 0
for el in fact():
    if i < x:
        print(el)
        i += 1
    else:
        break






