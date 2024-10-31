#Домашнее задание "Циклы". Часть 3

#Задание 1

# x = input("Введите число х: ")
# y = input("Введите число y: ")
# res = int(x) ** int(y)
# print("Результат: ",res)

#Задание 2

# s = input().split(" ")
# numbers = []
# for i in range(int(s[0]), int(s[1]) + 1):
#     num = []
#     for x in str(i):
#         num.append(x)
#     for j in range(10):
#         if num.count(str(j)) == 2:
#             numbers.append(i)
# print(len(numbers))
# print(numbers)


#Задание 3

# s = input().split(" ")
# numbers = []
# count = 0
# for i in range(int(s[0]),int(s[1]) +1):
#     if len(set(str(i))) == len(str(i)):
#         numbers.append(i)
#         count += 1
# print(count+1)
# print(numbers)


#Задание 4

s = input()
num = ""
for i in s:
    if i != "3" and i != "6":
        num += i
print(int(num))






