'''
Найти максимальный элемент среди минимальных элементов столбцов матрицы
'''

import numpy
import random


# Зададим для начала размер матрицы

a = int(input('Задайте количество строк в матрице '))
b = int(input('Задайте количество столбцов в матрице '))

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
