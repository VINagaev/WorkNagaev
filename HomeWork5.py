#Домашнее задание "Операторы ветвлений. часть 2"

#Задание 1

# day = int(input("Введите номер дня недели (от 1 до 7): "))
# if day == 1:
#     print("Понедельник")
# elif day == 2:
#     print("Вторник")
# elif day == 3:
#     print("Среда")
# elif day == 4:
#     print("Четверг")
# elif day == 5:
#     print("Пятница")
# elif day == 6:
#     print("Суббота")
# elif day == 7:
#     print("Воскресенье")
# else:
#     print("Некорректно введено значение")

#Задание 2

# month = int(input("Введите номер месяца (от 1 до 12): "))
# if month == 1:
#     print("Январь")
# elif month == 2:
#     print("Февраль")
# elif month == 3:
#     print("Март")
# elif month == 4:
#     print("Апрель")
# elif month == 5:
#     print("Май")
# elif month == 6:
#     print("Июнь")
# elif month == 7:
#     print("Июль")
# elif month == 8:
#     print("Август")
# elif month == 9:
#     print("Сентябрь")
# elif month == 10:
#     print("Октябрь")
# elif month == 11:
#     print("Ноябрь")
# elif month == 12:
#     print("Декабрь")
# else:
#     print("Некорректно введено значение")

# Задание 3

# string = int(input("Введите число: "))
# if string > 0:
#     print("Number is positive")
# elif string < 0:
#     print("Number is negative")
# elif string == 0:
#     print("Number is equal to zero")

# Задание 4

a = float(input("введите число a: "))
b = float(input("введите число b: "))
if a == b:
    print("число" , a , "= числу" , b)
else:
    print("Минимальное число: " , min([a, b]))
    print("Максимальное число: ", max([a, b]))