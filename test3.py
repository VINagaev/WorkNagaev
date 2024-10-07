#Классное задание 1

# string= input()
# numbers = string.split(" ")
# if len(numbers) == 4:
#     result = int(numbers[0]) * int(numbers[1]) * int(numbers[2]) * int(numbers[3])
#     print("* " , result)
# elif len(numbers) == 3:
#     result = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
#     print("+ " , result)
# elif len(numbers) <= 1:
#     print("данные не введены")
# else:
#     result = (float(numbers[0]) / float(numbers[1])).__format__(".4f")
#     print("/ " , result)
#     print("Введено 1 или 2 числа")

#Классное задание 2

# string= input()
# numbers = string.split(" ")
# integer = len(numbers)
# if numbers[0] == "":
#     print("пустая строка")
#     integer = 0
# match integer:
#     case 4:
#         result = int(numbers[0]) * int(numbers[1]) * int(numbers[2]) * int(numbers[3])
#         print(result)
#     case 3:
#         result = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
#         print(result)
#     case 2:
#         result = (float(numbers[0]) / float(numbers[1])).__format__(".4f")
#         print(result)
#     case 1:
#         print("Введено 0 или 1 число")
#     case 0:
#         print("Не Введено число")

#Классное задание 3

# a = 0
# while a < 5:
#     print("Мы в цикле")
#     print(a)
#     a = a + 1
#     if a == 3:
#         a = a + 1
# else:
#     print("Конец цикла")
#     b = 10
#     while b >= 0
#     print(b)
#     b = b - 1

#Классное задание 4

# for i in range(10,20,2):
#     print(i)

#Классное задание 5

for i in range(1,10):
    if  i % 3 == 3:
        break
    print(i)
else:
    print("End")












