var_int = 10
var_float = 8.4
var_str = 'No'
big_int = var_int * 3.5 # увеличение  в 3.5 раз
var_float -=1 # уменишение на единицу
var_int /= var_float
big_int /= var_float # разделение переменн
var_str = var_str*2 + "Yes"*3 # изменение строки
print('Результат работы над переменными', var_float, var_int, var_str, big_int)