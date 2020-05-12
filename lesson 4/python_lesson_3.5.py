def my_func():
    i = 0
    while True:
        numbers = input('Enter numbers separated by spaces: ').split()
        for num in numbers:
            try:
                if num == '#':
                    return f'Total summary: {i}. Over!!!'
                else:
                    i += int(num)
            except ValueError:
                print('Please: enter number or #')
        print(f'Summary: {i}')


print(my_func())
