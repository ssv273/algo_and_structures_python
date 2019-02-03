# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
import string

num_char = int(input('Введите номер буквы в алфавите \n'))
str_list = string.ascii_lowercase
print('Это буква "{}"'.format(str_list[num_char - 1]))