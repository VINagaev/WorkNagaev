#домашние задания
# задание 1
#вариант1
# string = input("введиет числа через пробел и знак").split(" ")
# number1 = float(string[0])
# number2 = float(string[1])
# number3 = float(string[2])
# znak = string[3]
# if znak == "+":
#     result = number1 + number2 + number3
#     print(result)
# elif znak == "*":
#     result = number1 * number2 * number3
#     print(result)
# elif znak == "-":
#     result = number1 - number2 - number3
#     print(result)
# elif znak == "/":
#     result = (number1 / number2 / number3).__format__(".4f")
#     print(result)
# else:
#     print("введены некорректные файлы")
#
# вариант 2
# string = input("введиет числа через пробел и знак")
# print(eval(string))
# задание 2


# string = input("введите три числа").split(" ")
# numbers = []
# for i in string:
#     numbers.append(int(i))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers) / len(numbers))

#задание 3
string = input("введите кол-во метров и величину").split(" ")
number1 = float(string[0])
znak = string[1]
if znak == "m":
    result = (number1 * 0.000621).__format__(".5f")
    print("Милли:", result)
elif znak == "d":
    result = (number1 * 39.3701).__format__(".5f")
    print("Дюймы:", result)
elif znak == "y":
    result = (number1 * 1.09361).__format__(".5f")
    print("Ярды:", result)

else:
    print("введены некорректные файлы")

print("hello")