'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить
среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
среднего.
'''

n = int(input('Введите кол-во предприятий'))
Plants = {}
global_average = 0
for i in range(n):
    average = 0
    print('Предприятие № {}', format(i + 1))
    plant = input('Введите название предприятия:')
    a = int(input('Введите прибыль за 1-й квартал'))
    b = int(input('Введите прибыль за 2-й квартал'))
    c = int(input('Введите прибыль за 3-й квартал'))
    d = int(input('Введите прибыль за 4-й квартал'))
    average = (a + b + c + d) / 4
    Plants[plant] = average
    global_average += average
    print(Plants)
    print(average)

global_average = global_average / n

print('Среднее значение годовой прибыли - {:.2f}'.format(global_average))
print('Предприятия с размером прибыли выше среднего:')
for i in Plants:
    if Plants[i] > global_average:
        print(i)
print('Предприятия с размером прибыли ниже среднего:')
for i in Plants:
    if Plants[i] < global_average:
        print(i)
