#Домашнее задание "Циклы". часть 3"

#Задание 1

# x = input("Введите число х: ")
# y = input("Введите число y: ")
# res = int(x) ** int(y)
# print("Результат: ",res)

#Задание 2

# s = input().split(" ")
# res = []
# for i in range(int(s[0]),int(s[1])):
#     e = str(i)
#     numbers = []
#     for j in e:
#         numbers.append(str(j))
#     count = 0
#     for x in numbers:
#         if numbers[0] ==x:
#             count +=1
#         if count == 2:
#                 res.append(i)
#                 break
# print(res)
# print(len(res))

# s = input().split(" ")
# res = []
# for i in range(int(s[0]),int(s[1])):
#     e = str(i)
#     numbers = []
#     for j in e:
#         numbers.append(str(j))
#     count = 0
#     k = 0
#     while k < len(numbers):
#         if numbers[0] == numbers [k]:
#             count += 1
#             if count == 2:
#                 res.append(i)
#                 break
#             k += 1
# print(res)
# print(len(res))

#Задание 3

#Задание 4



s = input().split(" ")
res = []
for i in range(int(s[0]),int(s[1])):
    e = str(i)
    numbers = []
    for j in e:
        count = 0
        if e[0] == j:
            count += 1
        if count == 2:
            numbers.append(i)
            break

