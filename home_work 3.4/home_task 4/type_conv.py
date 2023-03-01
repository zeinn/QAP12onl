x = 'Robin Singh'
y = 'I love arrays they are my favorite'
x_1 = x.split()
y_1 = y.split()
print(x_1)
print(y_1)

name = ['Ivan', 'Ivanov']
city = 'Minsk'
country = 'Belarus'


def hello(name_1, city_1, country_1):
    if type(name_1) == list:
        name_2 = ' '.join(name_1)
        return f'Привет {name_2}, добро пожаловать в {city_1}, {country_1}'
    else:
        return name_1


print(hello(name, city, country))

l_1 = ["I", "love", "arrays", "they", "are", "my", "favorite"]


def list_t(a):
    if type(a) == list:
        return " ".join(a)
    else:
        return a


print(list_t(l_1))

new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list.insert(3, 20)
new_list.pop(6)

print(new_list)

a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
ab = {}

for key, value in a.items():
    if key in b:
        ab[key] = [a[key], b[key]]
    else:
        ab[key] = [value, None]

for key, value in b.items():
    if key in a:
        ab[key] = [a[key], b[key]]
    else:
        ab[key] = [None, value]

print(ab)
