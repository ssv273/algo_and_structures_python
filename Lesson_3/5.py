'''
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
позицию в массиве.
'''

import random

lst_base = [random.randint(-100, 100) for i in range(50)]
lst = []
for i in lst_base:
    if i < 0:
        lst.append(i)

print('Максимальный отрицательный элемент в данном массиве = {}, его индекс {}'.format(max(lst), lst.index(max(lst))))
