def multiplication_of_numbers(numbers):  # Задание 1
    multiplication = 1
    i = 1
    if numbers < 1:
        return 0
    while i < numbers:
        multiplication *= i
        i += 1
    return multiplication


print(multiplication_of_numbers(0))


# Задание 2
# Поле засеяли цветами двух сортов на площади S1 и S2. Каждый год
# площадь цветов первого сорта увеличивается вдвое, а площадь второго сорта увеличивается втрое
# Через сколько лет площадь первых сортов будет составлять меньше 10% от площади вторых сортов.

def variety_area(area_1, area_2):
    year = 0
    if area_1 < 0 or area_2 < 0:
        return None
    while area_1 > area_2 * 0.1:
        area_1 *= 2
        area_2 *= 3
        year += 1
    return year


print(variety_area(1, 2))


# Задание 3
def count_and_sum_number(number):
    sum = 0
    count = 0
    while number > 0:
        count += number % 10
        number //= 10
        sum += 1
    return sum, count


print(count_and_sum_number(121))


# Задание 4
# Дано целое число в диапазоне 1–7. Вывести строку — название дня недели, соответствующее данному числу
def age_difference(grandfather_age, grandson_age):
    year = 0
    if grandfather_age <= grandson_age:
        return None
    while grandfather_age > grandson_age * 2:
        year += 1
        grandfather_age += 1
        grandson_age += 1
    return year, grandfather_age, grandson_age


print(age_difference(30, 5))
