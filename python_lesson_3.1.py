def my_func():
    try:
        val_1 = int(input("Enter dividend: "))
        val_2 = int(input("Enter divisor: "))
    except ZeroDivisionError:
        return "На ноль делить нельзя!!!"
    except ValueError:
        return 'Не вводите строку!!!'
    quotient = val_1 / val_2
    return quotient


print(my_func())
