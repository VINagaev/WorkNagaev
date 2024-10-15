#Домашнее задание "Введение в Python. часть 3"

#Задание 1

# string = input("введите 3 числа через пробел: ")
# print("введеные числа:" , string)
# numbers = string.split (" ")
# print("Ответ: " , f"{numbers[0]}{numbers[1]}{numbers[2]}")

#Задание 2

# string = input("введите 4 числа: ")
# proiz = int(string[0]) * int(string[1]) * int(string[2]) * int(string[3])
# print("Произведение чисел:" , proiz)

#Задание 3

# string = float(input("Введите количество метров: "))
# print(string , "метров это: ")
# print(f"{string*10} дециметров")
# print(f"{string*100} сантиметров")
# print(f"{string*1000} миллиметров")
# print(f"{string/1609} миль")

#Задание 4

# a = float(input("Введите основание треугольника: "))
# h = float(input("Введите высоту треугольника: "))
# s = a*h/2
# print("Площадь треугольника = :", s)

# Задание 5

string = input("Введите четырехзначное число: ")
print("Отраженное число: " , string[::-1])