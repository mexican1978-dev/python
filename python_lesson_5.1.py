book = open('text.txt', 'w', encoding='utf-8')
a = input('Enter text: ')
while a:
    book.writelines(a)
    a = input('Enter text: ')
    if not a:
        break

book.close()
book = open('text.txt', 'r', encoding='utf-8')
print(book.readlines())
book.close()
