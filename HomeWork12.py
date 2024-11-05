#Домашнее задание "Строки. Списки." Часть 1

#Задание 1

# s = input("Введите текст: ").lower().replace(" ", "")
# print(s)
# rev_s = s[::-1]
# print(rev_s)
# if s == rev_s:
#     print("Строка является полиндромом")
# else:
#     print("Строка не является полиндромом")

#Задание 2

# s = input("Введите текст: ")
# rez_s = input("Введите список зарезервированных слов через пробел: ").split()
# for i in rez_s:
#     s = s.replace(i, i.upper())
# print("Измененный текст: ", s)

#Задание 3

import re
s = input("Введите текст: ")
znak = re.split(r'[(.!?]', s)
kol = len(znak)
print("Количество предложений в тексте:", kol - 1)

