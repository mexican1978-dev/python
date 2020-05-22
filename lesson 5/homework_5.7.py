import json

money = {}
mid = {}
earn = 0
middle_money = 0
s = 0
with open('text_7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        money[name] = int(earning) - int(damage)
        if money.setdefault(name) >= 0:
            earn = earn + money.setdefault(name)
            s += 1
    if s != 0:
        middle_money = earn / 1
        print(f'Middle money - {middle_money:.2f}')
    else:
        print(f'Nothing. All have nothing')
    pr = {'middle earning': round(middle_money)}
    money.update(mid)
    print(f'Earned every company - {money}')

with open('text_7.txt', 'r', encoding='utf-8') as my_file:
    js_str = json.dumps(money)
    print(f'Create file json with content: \n'
          f'{js_str}')

