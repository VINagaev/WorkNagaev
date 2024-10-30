import pandas as pd
import re


# list = [134,152,522,5213]
#
# d = {
#     0: "toyota",
#     1: "lexus",
#     4: "geely",
#     "car" : "honda",
#     "car2" : "bmw"
# }
# # print(d.get(1))
# # print(d["car"])
# # d["car"] = "audi"
# # d.pop("car2")
# # print(d)
#
# print(d.keys())                                 #вывод ключей
# print(d.values())                               #вывод значение ключей.
# print(len(d))                                   #длина словаря.
# e = d.copy()                                    # (copy - копирует словарь)
# print(e.pop("car"))                             # pop - удаляет значение
# print(e)                                        # вывод значений без удаленного значения.
#
# for keys, value in d.items():
#     if keys == "car":
#         print(keys, " : ", value)


# c = (1,2,3,4,5,6,7,8,9,1)
# # print(set(c))                          # преобразование в словарь
# # f = set(c)
# # f.add(10)
# # print(f)
#
# print(c.index(5))                       # индекс в картеже
# print(c.count(1))                       # количество значений в картеже
# print(len(c))                           # длина кортежа
# print(max(c))                           # максимальное значение в картеже
# print(min(c))                           # минимальное значение в картеже



# keys = (1,2,3,4,5,6,7,8,9,1)
# value = ['a','b','c','d','e','f','g','h']
# d1 = {}
# for keys, value in zip(keys, value):
#     d1[keys] = value
# print(d1)

# df = pd.DataFrame()
# print(df)

#Регулярные выражения

# s= input("Введите логин: ")
# pattern = "(user)|(admin)+"
# st = re.search(pattern, s)
# print(st)
# if not st:
#     print("логин верный", s)

#задание из яндекса
# найти нибольшее число в массиве, являешееся полным квадратом некоторого числа
# num = []
# s = input().split(" ")
# max_square = 0
# for i in range(int(s[0]), int(s[1])):
#     sqrt = int(i ** 0.5)
#     print(sqrt*sqrt)
#     if i == sqrt * sqrt:
#         num.append(i)
# print(num)

num = []
s = input().split(" ")
max_square = 0
for i in range(int(s[0]), int(s[1])):
    sqrt = int(abs(i ** 0.5)
    print(sqrt*sqrt)
    if abs(i) == sqrt * sqrt:
        num.append(i)
print(num)