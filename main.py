v_1 = -1.6  # Задание 1
v_2 = 2.99
v_3 = int(v_1)
v_4 = int(v_2)

print('число, приведенное к целому типу:', v_3)
print('число, приведенное к целому типу:', v_4)

str_old = 'www.my_site.com#about'
str_new = 'www.my_site.com#about'  # Задание 2
str_new = str_new.replace('#', '/')

print('Перноначальная строка:', str_old)
print('Ррезьтутат с заменой символа:', str_new)

str_new = 'stroka'  # Задание 3
str_b = str_new.replace('a', 'ing')

print('Оконччание добавлено:', str_b)

str_ivanou = 'Ivanou Ivan'  # Задание 4
str_i = str_ivanou.split(" ")[1] + ' ' + str_ivanou.split(" ")[0]
print('Строка из условия:', str_ivanou)
print('Строка после замены слов:', str_i)

s = input('Введите с помощью клавиатуры слово с изначальным и конечным пробелом:').strip()  # Задание 5
print('Пробелы удалены:', s)

school = {'1a': 25, '2c': 18, '3b': 20, '4c': 28, '5a': 31, '6b': 16, '7a': 30, '8d': 15, '9a': 22,
          '10b': 26}  # Задание 6
print('Вывели количество учеников по ключу 5а', school.get("5a"))

l_1 = [1, 2, 3, 4, 5]  # Задание 7
print('Второй символ выведен:', l_1[1])  # вывод 2 символа

str_2 = 'employment'  # Задание 8
str_3 = str_2.find('employ')
print('Строка str_3 входит в строку str_2:', str_3)

x = 'My name is Agent Smith'  # Задание 9
print('Вывели символ по индексу [1]:', x[1])  # выводит символ Y
print('Вывели символы по индексу [3]:, x[6], x[9], x[12], x[15] ', x[3], x[6], x[9], x[12], x[15])

l_2 = [1, 5, 2, 9, 2, 9, 1]  # Задание 10
uniq_num = list(set(l_2))
print('Уникальные числа:', uniq_num)
