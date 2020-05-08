def my_funk(x, y):
    y = abs(y)
    if y == 0:
        return 1
    else:
        return my_funk(x, y - 1) * x


print(1 / (my_funk(2, -6)))
