# Модуль 4. Строки. Списки. Часть 2.

#Задание 1

#Пользователь вводит с клавиатуры арифметическое выражение. Например, 23+12.
#Необходимо вывести на экран результат выражения. В нашем примере это 35.
# Арифметическое выражение может состоять только из трёх частей: число, операция, число.
# Возможные операции: +, -, *, /.

#Задание 2

#В списке целых, заполненном случайными числами, определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчитать количество положительных элементов,
# посчитать количество нулей. Результаты вывести на экран.

#Задание 1

# import re
# s = input("Введите арифметическое значение: ")
# operation = re.findall(r'[(\-/\+*)]', s)
# numbers = re.split(r'[(\-/\+*)]', s.replace(" ", ""))
# nominal = ['*', '/', '-', '+']
# for j in nominal:
#     i = 0
#     temp = 0
#     if j == "*" and j == operation[i]:
#         temp = (float(numbers[i]) * float(numbers[i+1]))
#         print("Результат умножения: ", int(temp))
#     elif j == "/" and j == operation[i]:
#         temp = (float(numbers[i]) / float(numbers[i+1]))
#         print("Результат деления: ", int(temp))
#     elif j == "-" and j == operation[i]:
#         temp = (float(numbers[i]) - float(numbers[i+1]))
#         print("Результат вычетания: ", int(temp))
#     elif j == "+" and j == operation[i]:
#         temp = (float(numbers[i]) + float(numbers[i+1]))
#         print("Результат сложения: ", int(temp))


#Задание 2

from random import randint
s = [randint(-10,10) for i in range(20)]
def f(e):
    return e < 0
n = s.count(0)
p = list(filter(f,s))
print(s)
print("Максимальное значение: ", max(s))
print("Минимальное значение: ",min(s))
print("Количество положительных чисел: ",len(s) - len(p) - n)
print("Количество отрицательных чисел: ",len(p))
print("Количество нулей: ",n)