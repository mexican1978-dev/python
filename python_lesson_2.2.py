
# list1 = list(input("Enter: "))
list1 = [input("Enter: ") for i in range(int(input("Enter number of elements: ")))]
if len(list1) % 2 == 0:
    list1[::2], list1[1::2] = list1[1::2], list1[::2]
    print(list1)
else:
    list1[:-1:2], list1[1:-1:2] = list1[1:-1:2], list1[:-1:2]
    print(list1)





