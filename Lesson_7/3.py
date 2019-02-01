'''
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите
в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в
одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то
используйте метод сортировки, который не рассматривался на уроках.
'''

import random
from datetime import datetime


def time(func):
    def t(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        print(datetime.now() - start, end='')
        return res
    return t


@time
def sorted_array(a):
    """
    Для начала потренируемся на отсортированном массиве
    """
    a = sorted(a)
    return a[len(a) // 2]
    # по условию у нас количество элементов всегда нечетное, но на тот случай если условие изменится

    # if len(a) % 2 == 1:
    #     return a[len(a) // 2]
    # else:
    #     return (a[len(a) // 2 - 1] + a[len(a) // 2]) / 2


@time
# Теперь на неотсортированном
def quick_select_median(l, op_el_choice=random.choice):
    """
    Функция получает на вход список чисел, определяет случайный опорный элемент
    :return: k-й элемент массива l, т.к. нам нужна медиана, то ее индекс будет = len(l)/2 или среднее между двумя значениями, если кол-во элементов в массиве четное
    """
    return quick_select(l, len(l) / 2, op_el_choice)
    # по условию у нас количество элементов всегда нечетное, но на тот случай если условие изменится

    # if len(l) % 2 == 1:
    #     return quick_select(l, len(l) / 2, op_el_choice)
    # else:
    #     return (quick_select(l, len(l) // 2 - 1, op_el_choice) + quick_select(l, len(l) // 2, op_el_choice)) / 2


def quick_select(l, k, op_el_choice):
    '''
    Функция выбирает k-й элемент
    :param l: это массив чисел
    :param k: индекс
    :param op_el_choice: это функция выбора опорного элемента, по умолчанию выбирает случайный
    :return: k-й элемент массива l
    '''
    if len(l) == 1:
        return l[0]

    op_el = op_el_choice(l)  # выбираем случайно опорный элемент, т.к. эту переменную мы описали в родительской функции
    # Делим входящий список на группы
    # в первой группе числа меньше опорного элемента
    lesser_elems = [el for el in l if el < op_el]
    # во второй группе числа больше опорного элемента
    great_elems = [el for el in l if el > op_el]
    # в третьей группе  сам опорный элемент, или несколько их, если они равны
    op_els = [el for el in l if el == op_el]

    # мы знаем что одна из этих групп содержит медиану
    if k < len(
            lesser_elems):  # если в списке чисел, которые меньше опорного элемента есть k или больше чисел, то рекурсивно обходим этот список в поисках k-го элемента
        return quick_select(lesser_elems, k, op_el_choice)
    elif k < len(lesser_elems) + len(op_els):  # это и есть медиана
        return op_els[0]
    else:  # иначе обходим список больших элементов, и вместо k ищем k-len(lesser_elems)
        return quick_select(great_elems, k - len(lesser_elems) - len(op_els), op_el_choice)


m = int(input('Введите натуральное число для определения размера массива  '))
arr = [random.randint(-100, 100) for i in range(2 * m + 1)]
print(' сек  - время поиска медианы в отсортированном массиве. \n Медиана = {}'.format(sorted_array(arr)))
print(' сек  - время поиска медианы в несортированном массиве. \n Медиана = {}'.format(quick_select_median(arr)))
