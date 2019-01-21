'''
2. Написать два алгоритма нахождения i-го по счёту простого числа.
● Без использования Решета Эратосфена;
● Использовать алгоритм решето Эратосфена
'''

import cProfile

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
    return lst

cProfile.run('finder(55555)')
cProfile.run('eratosfen(55555)')