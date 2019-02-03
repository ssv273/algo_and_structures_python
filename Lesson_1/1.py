# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
num = str(input('Введите трехзначное число'))
num_list = list(map(int, num))
op = 1
for i in num_list:
    op = op * int(i)
print('Произведение чисел = {}'.format(op))
b = sum(num_list)
print('Сумма чисел = {}'.format(b))