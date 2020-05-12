i = 0
products, prices, numbers, measures = [], [], [], []
analytics = {'Name': products, 'Price': prices, 'Number': numbers, 'Measure': measures}
answer = ''
while answer != 'Нет':
    answer = input("Хотите совершить покупку?  (Да/Нет/Не знаю): ")
    if answer == 'Да':
        print('Отлично!!!')
        a = input('Введите название товара: ')
        b = int(input('Укажите цену: '))
        c = int(input('Количество: '))
        d = input('Укажите единицу измерения: ')
        i += 1
        products.append(a)
        prices.append(b)
        numbers.append(c)
        measures.append(d)
    elif answer == 'Нет':
        print('До свидания.')
        break
    else:
        print('Подумайте еще...')
print(f'Название: {products}\nЦена:{prices}\nКоличество: {numbers}\nЕдиница измерения: {measures} ')


