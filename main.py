v_1 = -1.6  # Задание 1
v_2 = 2.99
v_3 = int(v_1)
v_4 = int(v_2)

print(v_3)
print(v_4)

str = 'www.my_site.com#about'  # Задание 2
str_1 = str.replace('#', '/')

print(str_1)

str_new = 'stroka'  # Задание 3
str_b = str_new.replace('a', 'ing')

print(str_b)

str_fam = 'Ivanou'  # Задание 4
str_name = 'Ivan'

print(f"{str_name} {str_fam}")

s = input().strip()  # Задание 5
print(s)

school = {'1a': 25, '2c': 18, '3b': 20, '4c': 28, '5a': 31, '6b': 16, '7a': 30, '8d': 15, '9a': 22,
          '10b': 26}  # Задание 6
print(school.get("5a"))

l_1 =  [1,2,3,4,5] # Задание 7
print(l_1 [1]) # вывод 2 символа

str_2 = 'employment' # Задание 8
str_3 = str_2.find('employ')
print(str_3)

x = 'My name is Agent Smith' # Задание 9
print(x [1]) # выводит символ Y
print(x [3], x[6], x[9], x[12], x[15])

l_2 = [1,5,2,9,2,9,1]
uniq_num = list(set(l_2))
print(uniq_num)

