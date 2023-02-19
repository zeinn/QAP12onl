school = {'1а': 16, '1б': 20, '2a': 18, '3а': 17, '4a': 23,
          '4б': 15, '5а': 20, '6a': 19, '7а': 19, '8a': 21}

for _class, _count in school.items():
    print(f'{_class} - {_count}')

school['1б'] = 19
school['1а'] = 17
school['7а'] = 20

school.update({'9б': 25, '10a': 19})

school.pop('4б')

print()
for _class, _count in school.items():
    print(f'{_class} - {_count}')
