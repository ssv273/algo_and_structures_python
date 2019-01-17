'''
Найти максимальный элемент среди минимальных элементов столбцов матрицы
'''

import numpy
import random

# Зададим для начала размер матрицы

a = int(input('Задайте количество строк в матрице '))
b = int(input('Задайте количество столбцов в матрице '))
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
