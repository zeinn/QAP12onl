# Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B включительно.


def range_sum(a, b):
    c = 0
    for i in range(a, b + 1):
        c += i
    return c


print(range_sum(2, 5))

# Найти произведение положительных, сумму и количество отрицательных из 10 введенных целых значений.
# def sum_natural(a, b)

name_and_result = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17,
}

def best_result(swimmers):
    for key, value in swimmers.items():
        if value == min(swimmers.values()):
            return key, min(swimmers.values())

print(best_result(name_and_result))