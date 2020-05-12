from itertools import islice, count, cycle
for c in islice(count(), 3, 11):
    print(c)

my_list = [1, None, 56 - 5j, 'spam', 3.1415]
a = cycle(my_list)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
