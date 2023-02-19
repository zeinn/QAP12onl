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


def list(a):
    if type(a) == list:
        return " ".join(a)
    else:
        return a


print(list(l_1))
