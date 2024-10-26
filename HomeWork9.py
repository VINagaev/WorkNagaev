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

# s = input().split(" ")
# count = 0
# for num in range(int(s[0]),int(s[1])):
#     if len(set(str(num))) == len(str(num)):
#         count += 1
# print(count+1)


#Задание 4








count = 0
for i in range(100, 1000):
    num = str(i)
    if num[0] == num[1] or num[0] == num[2] or num[1] == num[2]:
        count += 1
print(count)







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

