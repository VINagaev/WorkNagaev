#Работа в классе
#разбор домашнего задания №5.
import datetime
import calendar
import re

#Задание 1
#Вариант 1

# string = input("введите номер дня: ")
# if string == "1":
#     print("Понедельник")
# elif string == "2":
#     print("Вторник")
# elif string == "3":
#     print("Среда")
# elif string == "4":
#     print("Четверг")
# elif string == "5":
#     print("Пятница")
# elif string == "6":
#     print("Суббота")
# elif string == "7":
#     print("Воскресенье")
# else:
#     print("день не соответствует")

#Задание 1
#Вариант 2

# string = input("введите номер дня: ")
# print(list(calendar.day_name)[int(string)]) #дни недели


#Задание 2
#Вариант 2

# print(list(calendar.month_name)[int(string)]) #месяца

#Задание 3

# string = input("Введите число: ")
# if int(string) > 0:
#     print("Number is positive")
# elif int(string) < 0:
#     print("Number is negative")
# else:
#     print("Number is equal to zero")


#Вариант 2

# string = input("Введите число: ")
# if float(string) > 0:
#         print("Number is positive")
# elif float(string) < 0:
#         print("Number is negative")
# else:
#         print("Number is equal to zero")

#Вариант 3
# string = input("Введите число: ")
# if string.isdigit():
#     if float(string) > 0:
#      print("Number is positive")
#     elif float(string) < 0:
#      print("Number is negative")
#     else:
#      print("Number is equal to zero")
# else:
#      print("error")

#Вариант 4 с дробями

# string = input("Введите число: ")
# print(string.find("."))
# if string.isdigit() or (string.find(".")) > -1:
#     if float(string) > 0:
#      print("Number is positive")
#     elif float(string) < 0:
#      print("Number is negative")
#     else:
#      print("Number is equal to zero")
# else:
#      print("error")

#Вариант 5 убирает символы и оставляет цифры и точки

# string = input("Введите число: ")
# print(re.sub(r'[^.\d]', "", string))
# number = re.sub(r'[^.\d]', "", string)
# if float(number) > 0:
#     print("Number is positive")
# elif float(string) < 0:
#     print("Number is negative")
# else:
#      print("Number is equal to zero")



#Вариант 6

# string = input("Введите число: ")
# number = [0, 0]
# print(re.findall(r'[-+^.]?\d+', string))
# numbers = re.findall(r'[-+^.]?\d+', string)
# try:
#     number[0] = float(numbers[0])
# except:
#     number[0] = 0
# try:
#     number[1] = float(numbers[1])
# except:
#     number[1] = 0
# ish = number[0] + number[1]
# print(ish)
# if float(ish) > 0:
#     print("Number is positive")
# elif float(ish) < 0:
#     print("Number is negative")
# else:
#      print("Number is equal to zero")


#Задание 4

# string = input("").split(" ")
# if int(string[0]) == int(string[1]):
#     print("Числа равны", string[0])
# else:
#     if int(string[0]) > int(string[1]):
#         print("1 число: ", int(string[1]))
#         print("2 число: ", int(string[0]))
#     else:
#         print("1 число: ", int(string[0]))
#         print("2 число: ", int(string[1]))

#Вариант 2 (сортировка пузырьковая)

# string = input().split(" ")
# numbers=[]
# for i in string:
#     numbers.append(int(i))
#     numbers.sort()
# print(numbers)

# сортировка реверс
# string = input().split(" ")
# numbers=[]
# for i in string:
#     numbers.append(int(i))
#     numbers.sort(reverse=True)
# print(numbers)