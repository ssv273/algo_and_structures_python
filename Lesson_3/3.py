'''
В массиве случайных целых чисел поменять местами минимальный и максимальный
элементы.
'''

import random

lst_base = set(random.randint(-100, 100) for i in range(50))
lst = list(lst_base)
a = max(lst)
b = min(lst)
ind_a = lst.index(a)
ind_b = lst.index(b)
print('В данном массиве чисел максимальное число {:4d} стоит на {:4d} позиции\n'
      '                      а минимальное число {:4d} стоит на {:4d} позиции '.format(a, ind_a, b, ind_b))

print('Заменяем их')

lst[ind_a], lst[ind_b] = b, a
ind_a = lst.index(a)
ind_b = lst.index(b)
print('                Теперь максимальное число {:4d} стоит на {:4d} позиции\n'
      '                     а минимальное число  {:4d} стоит на {:4d} позиции '.format(a, ind_a, b, ind_b))
