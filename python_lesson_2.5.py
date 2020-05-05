rating = [7, 5, 2, 2, 1]
x = int(input('Enter your rating: '))
i = 0
for rating[i] in rating:
    if rating[i] >= x:
        i += 1
    else:
        break
rating.insert(i, x)
for s in rating:
    print(s, end=', ')



