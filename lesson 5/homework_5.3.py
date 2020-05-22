with open('text_3.txt', 'r') as report:
    money, low_level = [], []
    earn = report.read().split('\n')
    for d in earn:
        d = d.split()
        if float(d[1]) < 20000:
            low_level.append(d[0])
        money.append(d[1])
print(f'Middle: \n{sum(map(float, money)) / len(money)}')
print(f'Who earned less 20000: \n{low_level}')


