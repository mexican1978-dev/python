from random import randint

summary = ' '.join([str(randint(1, 1000)) for _ in range(100000)])
integers = open('task_5_file.txt', 'w+')
integers.write(summary)
integers.seek(0)

print(sum(map(int, integers.readline().split())))
integers.close()