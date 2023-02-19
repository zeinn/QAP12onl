str = 'Helloworld'

print(str[0], str[-1], str[2], str[-3])

str_new = str.replace('world', 'Belarus')  # замена слова

print(str_new)

str_1 = 'HimynameZein'

print(str_1[:8], str_1[4:8])

first = ""
for i in range(len(str_1)):  # символы с индексами кратными трем
    if i % 3 == 0:
        print(i)
        first += str_1[i]
print(first)

print(str_1[:: -1])  # переворот строки

name = "my name is name"
new_name = name.split()
new_name[3] = "Evgeni"  # Замена слова
print(' '.join(new_name))

test_tring = "Hello world!"
print(test_tring.find('w'))  # Поиск полодения символа 'w'
print(test_tring.count('l'))  # Колиство символов 'l' в строке "Hello world!"
print(test_tring.find('Hello', 0, 6))  # Проверить начинается ли строка с подстроки: “Hello”
print(test_tring.find('qwe', -1, -7))  # Проверить заканчивается ли строка подстрокой: “qwe”
