init_f = open('text_6.txt', 'r')
subj = {}
for line in init_f:
    subject, hours = line.split(':')
    for i in hours.split():
        if i != '-':
            subj[subject] = subj.get(subject, 0) + int(i.split('(')[0])
print(f'Total hours for subjects: \n{subj}')

