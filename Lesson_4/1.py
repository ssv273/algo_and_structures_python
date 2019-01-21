'''
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в
рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
'''

import cProfile


def sorter(a, b, c):
    lst = sorted(map(float, [a, b, c, ]))
    return lst


def iff(a, b, c):
    if b < a < c or c < a < b:
        return a
    elif a < b < c or c < b < a:
        return b
    else:
        return c


def main():
    a = input('Введите первое число ')
    b = input('Введите второе число ')
    c = input('Введите третье число ')
    print(sorter(a, b, c, ))
    print(iff(a, b, c, ))


cProfile.run('sorter(78,24,658)')
cProfile.run('iff(78,24,658)')
