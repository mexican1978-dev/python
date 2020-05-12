old_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
next_list = [a for a in old_list if old_list.count(a) < 2]
print(next_list)