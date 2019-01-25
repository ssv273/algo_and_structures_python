'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое
число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''


import collections


def conversion(a):
    a = list(str.upper(a))
    c = []
    dec = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ]
    hexx = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    dh_dict = dict(zip(hexx, dec))
    for el in a:
        c.append(dh_dict[el])
    return c


def reconversion(a):
    c = []
    dec = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    hexx = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    dh_dict = dict(zip(dec, hexx))
    for el in a:
        c.append(dh_dict[el])
    return c


def hexa(r):  # список приводим к основанию 16
    for el in range(len(r))[::-1]:
        if r[el] >= 16:
            r[el - 1] = r[el - 1] + r[el] // 16
            r[el] = r[el] % 16
    return r

def appleft(m, l):
    q = l - len(m)
    m = collections.deque(m, l)
    for i in range(q):
        m.appendleft(0)
    return list(m)


def summ(x, y):
    return list(map(lambda a, b: a + b, x, y))


a1 = input('Введите первое число в hex формате:  ')
b1 = input('Введите второе число в hex формате:  ')
a = conversion(a1)
b = conversion(b1)

if len(b) > len(a):
    a, b = b, a

# перемножаем списки
r2 = []
z = min(len(a), len(b)) - 1  # определяем количество сдвигов
for i in b:
    r3 = [0]
    for f in a:
        r3.append(i * f)
        # print(i)
    for e in range(z):  # делаем сдвиг
        r3.append(0)
    r2.append(r3)
    z -= 1
# переводим получившийся список в основание 16
res_hexlist = []
for f in r2:
    res_hexlist.append(hexa(f))

# определяем длины списков, чтобы уравнять их длины
max_len = 0
for el in r2:
    if len(hexa(el)) > max_len:
        max_len = len(hexa(el))

# уравниваем длины списков
for z in range(len(res_hexlist)):
    res_hexlist[z] = appleft(res_hexlist[z], max_len)

# теперь складывем их
# создаем результирующий список
rezz = []
rezz = appleft(rezz, max_len)

# теперь складываем его со списками, которые получились в результате умножения
for h in range(len(res_hexlist)):
    rezz = summ(rezz, res_hexlist[h])
# переводим в основание 16
rezz = hexa(rezz)
print('Произведение введенных чисел = ',reconversion(rezz))

# теперрь сложение сделаем
# для начала уравняем их длины
# т.к. у нас b всегда меньше или = а, то
b = appleft(b,len(a))
# теперь передадим их в функцию сложения
summ_rez = summ(a,b)
# и результат приводим к основанию 16
summ_rez = hexa(summ_rez)
print('Сумма введенных чисел = ',reconversion(summ_rez))