'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и
максимальным элементами. Сами минимальный и максимальный элементы в сумму не
включать.
'''

import random

lst_base = [random.randint(-100, 100) for i in range(20)]
print(lst_base)

a_min = lst_base.index(min(lst_base))
b_max = lst_base.index(max(lst_base))

if a_min > b_max:
    a_min, b_max = b_max, a_min

summ = 0
for i in range(a_min + 1, b_max):
    summ += lst_base[i]
print('Сумма элементов между {} и {} = {}'.format(lst_base[a_min], lst_base[b_max], summ))
