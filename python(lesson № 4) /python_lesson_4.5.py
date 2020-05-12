from functools import reduce
gen_list = [el for el in range(100, 1001) if el % 2 == 0]
print(gen_list)
print(reduce(lambda x, y: x + y, gen_list))
