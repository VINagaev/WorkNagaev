#Домашнее задание "Циклы". Часть 4

#Задание 1

# s = input("Введите диапозон чисел: ").split(" ")
# numbers = []
# for i in range(int(s[0]), int(s[1])):
#     count = 0
#     j = 1
#     while j <= i:
#         if i % j == 0:
#             count += 1
#         j += 1
#     if count == 2:
#         numbers.append(i)
# print("Простые числа: ", numbers)

#Задание 2

# n=int(input("Введите число: "))
# for i in range(1,11):
#     k=n*i
#     print(n,"*",i,"=",k)

#Задание 3

start = int(input("Введите начальное значение: "))
end = int(input("Введите конечное значение: "))
for i in range(start, end + 1):
    for j in range(1, 11):
        result = i * j
        print(i, "*", j, "=", result)
