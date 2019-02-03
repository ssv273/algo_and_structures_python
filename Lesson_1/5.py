#5.	Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

import string

char_1 = input('Введите первую букву ')
char_2 = input('Введите вторую букву ')

str_lst = string.ascii_lowercase
ind_1 = str_lst.index(char_1)
ind_2 = str_lst.index(char_2)
print('Между этими буквами находятся следующие буквы : ',
      str_lst[ind_1 + 1:ind_2] if ind_1 < ind_2 else str_lst[ind_2 + 1:ind_1])