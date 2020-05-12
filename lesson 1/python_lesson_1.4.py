x = int(input('Enter your number: '))
max_num = 0
a = x % 10
while x != 0:
    if a > max_num:
        max_num = a
        x = x // 10
        a = x % 10
    else:
        x = x // 10
        a = x % 10
print(max_num)





