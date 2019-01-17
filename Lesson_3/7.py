'''
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть
как равны между собой (оба являться минимальными), так и различаться.
'''

import random

lst_base = [random.randint(-100, 100) for i in range(500)]

min_1 = min(lst_base)
count = 0
for i in lst_base:
    if i == min_1:
        lst_base.remove(i)
        count += 1
print('Наименьший элемент: {}, встречается в этом массиве {} раз'.format(min_1, count))
if count == 1:
    min_2 = min(lst_base)
    print('Второй наименьший элемент: ', min_2)
