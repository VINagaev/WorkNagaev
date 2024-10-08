#Домашнее задание "Операторы ветвлений. часть 1"
#Задание 1

# string = input("Введите три числа через пробел и знак (+ или *): ").split(" ")
# number1 = float(string[0])
# number2 = float(string[1])
# number3 = float(string[2])
# znak = string[3]
# if znak == "+":
#      result = number1 + number2 + number3
#      print("Сумма чисел: " , result)
# elif znak == "*":
#      result = number1 * number2 * number3
#      print("Произведение чисел: " , result)
# else:
#      print("Введены некорректные данные")

#Задание 2

# string = input("Введите три числа через пробел: ").split(" ")
# numbers = []
# for i in string:
#     numbers.append(int(i))
# print("Масимальное значение: " , max(numbers))
# print("Минимальное значение: " , min(numbers))
# print("Среднеарифметическое значение: " , sum(numbers) / len(numbers))

#Задание 3

string = input("Введите через пробел кол-во метров и величину преобразования(m-мили, d-дюймы y-ярды): ").split(" ")
number1 = float(string[0])
vel = string[1]
if vel == "m":
    result = (number1 * 0.000621).__format__(".2f")
    print("Кол-во метров в миллях:", result)
elif vel == "d":
    result = (number1 * 39.3701).__format__(".2f")
    print("Кол-во метров в дюймах:", result)
elif vel == "y":
    result = (number1 * 1.09361).__format__(".2f")
    print("Кол-во метров в ярдах:", result)
else:
    print("Введены некорректные данные")