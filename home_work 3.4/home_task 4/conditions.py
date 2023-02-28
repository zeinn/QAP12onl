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

year = 1200

if year % 4 != 0:
    print('не Високосный год: 365 дней ', year)
elif year % 100 != 0:
    print('Високосный год: 366 дней', year)
elif year % 400 != 0:
    print('не Високосный год:365 дней ', year)
else:
    print('Високосный год: 366 дней', year)


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


print(name_of_day(5))
