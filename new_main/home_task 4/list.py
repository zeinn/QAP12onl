list = ["mama", "papa", "qwe"]
list_numb = [1, 2, 3]

print(list[1])


def new_list(l_1, l_2):
    l_2[-1] = 4
    return l_1, l_2


print(new_list(["mama", "papa", "qwe"], [1, 2, 3]))


def j(l_1, l_2):
    return l_1 + l_2


list_3 = j(list, list_numb)

print(j(["mama", "papa", "qwe"], [1, 2, 3]))


def new_list_1(j):
    return j[::2]


list_4 = new_list_1(list_3)

print(list_4)


def add_el(l_of_el, *args):
    l_of_el += [*args]
    return l_of_el


print(add_el(list_4), "Bob", 15)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = set(a) & set(b)

print(c)

d = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
