'''
Определить, какое число в массиве встречается чаще всего
'''

import random
import collections



lst_base = [random.randint(-100, 100) for i in range(1000)]

# Вариант №1
print('Вариант №1')
x = collections.Counter(lst_base).most_common(1)
print('Число {} встречается {} раз\n'.format(x[0][0],x[0][1]))

# Вариант №2
print('Вариант №2')
repeat = []
global_max_repeat = 0
global_number = 0
for el in lst_base:
    max_repeat = 0
    number = 0
    for i in lst_base:
        if el == i:
            max_repeat += 1
            number = el
    if max_repeat > global_max_repeat:
        global_max_repeat = max_repeat
        global_number = el
for a in range(len(lst_base)):
    if lst_base[a] == global_number:
        repeat.append(a)
print('В данном массиве чаще всего встречается число {}\n'
      'Оно встречается {} раз\n'
      'на следующих местах{}'.format(global_number, global_max_repeat, repeat))


