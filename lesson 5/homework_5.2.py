i = 0
with open('text_2.txt', 'r') as book:
    for a in book:
        i += 1
        a_letter = a.split(' ')
        print(a, 'Слов в строке: ', len(a_letter))
    print('Всего строк: ', i)
