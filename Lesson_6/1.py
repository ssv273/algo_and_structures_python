"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
from memory_profiler import profile
from pympler import asizeof


@profile()
def finder(n):
    lst = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                # если делитель найден, число не простое.
                break
        else:
            lst.append(i)
    return lst


@profile()
def eratosfen(n):
    a = [i for i in range(n + 1)]
    a[1] = 0
    lst = []
    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
    print(len(lst))
    return lst


a = finder(1000)
b = eratosfen(1000)
print(asizeof.asizeof(a))
print(asizeof.asizeof(b))

# Windows 10, 64-bit
# Python 3.7
# первая функция занимает 21,7 мб памяти
# вторая 21,8
# список а занимает 3416 b, список b столько же

import numpy
import random

# Зададим для начала размер матрицы

# a = int(input('Задайте количество строк в матрице '))
# b = int(input('Задайте количество столбцов в матрице '))
a = 5
b = 9
# Вариант №1
# Создаем пустой массив
matrix = numpy.zeros((a, b), int)
# заполняем его значениями
for i in range(a):
    for j in range(b):
        matrix[i][j] = random.randint(0, 50)
print(matrix)
# теперь создаем список из минимальных элементов столбцов
min_list = []
for el in range(b):
    min_list.append(numpy.min(matrix[:, el]))
print('\n', min_list, 'Это минимальные значения по столбцам')
# ну и сответственно выводим его
print('Максимальное значение среди них = ', max(min_list))
print(asizeof.asizeof(min_list))

# Вариант №2

mat = []
# Создаем матрицу
for i in range(a):
    string = []
    for j in range(b):
        string.append(random.randint(0, 50))
        print('%3d' % string[j], end='')
    mat.append(string)
    print('')
# Создаем список, в который будем заносить минимальные элементы по столбцам
min_list2 = []
# определяем минимальные элементы по столбцам
for i in range(b):
    min_l = []
    for j in range(a):
        min_l.append(mat[j][i])
    min_list2.append(min(min_l))

print(min_list2, 'минимальные значения по столбцам  ')
print('Максимальное среди них = {}'.format(max(min_list2)))
print(asizeof.asizeof(min_list2))

# Windows 10, 64-bit
# Python 3.7
# список min_list занимает 248 b, список min_list2 - 232 b
# странно, но вроде и тот и другой списки, а почему-то первый больше памяти занимает