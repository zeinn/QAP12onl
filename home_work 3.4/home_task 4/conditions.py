def first_cond(n):
    if n > 0:
        return n + 1
    else:
        return n


print(first_cond(5))


def find_pos(a, b, c):
    i = 0
    if a > 0:
        i += 1

    if b > 0:
        i += 1

    if c > 0:
        i += 1

    return i


print(find_pos(1, 2, -3))


def num_of_days_in_year(year):
    if year % 4:
        return 365
    elif year % 100:
        return 366
    elif year % 400:
        return 365
    else:
        return 366
print(num_of_days_in_year(1900))


def name_of_day(day):
    if day == 1:
        return "понедельник"
    elif day == 2:
        return "вторник"
    elif day == 3:
        return "среда"
    elif day == 4:
        return "четверг"
    elif day == 5:
        return "пятница"
    elif day == 6:
        return "суббота"
    elif day == 7:
        return "воскресенье"


print(name_of_day(7))


def mass_convertor(unit, value):
    if unit == 1:  # Kg
        return value
    elif unit == 2:  # mcg
        return value * 1e-6
    elif unit == 3:  # mg
        return value * 1e-3
    elif unit == 4:  # T
        return value * 1e3
    elif unit == 5:  # centner
        return value * 1e2


print(mass_convertor(3, 10000))
