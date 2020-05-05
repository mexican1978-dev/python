name = input()
i = 0
for word in name.split():
    i += 1
    print(i, word.capitalize()[:10])
