from sys import argv

title, pay_for_hour, how_many_hours, add = argv


def my_func():
    x = int(pay_for_hour)
    y = int(how_many_hours)
    z = int(add)
    result = x * y + z
    return f'You have earned for this month: {result}'


print(my_func())
