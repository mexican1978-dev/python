from itertools import cycle, count
for a in count(3):
    if a > 10:
        break
    else:
        print(a)

count = 0
my_list = [1, None, 56 - 5j, 'spam', 3.1415]
for i in cycle(my_list):
    if count == 10:
        break
    print(i)
    count += 1

f

