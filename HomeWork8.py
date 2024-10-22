#Домашнее задание "Циклы". часть 1"

#Задание 1

# string = input("Введите начало и конец диапазона через пробел: ").split(" ")
# begin = int(string[0])
# end = int(string[1])
# result = ""
# for i in range(begin, end):
#     if i % 7 == 0 and i != 0:
#         result += str(i) + ","
# print("Числа кратные семи: ",result)

#Задание 2

# string = input("Введите начало и конец диапозона через пробел:").split(" ")
# begin = int(string[0])
# end = int(string[1])
#
# result = ""
# for i in range(begin, end+1):
#     result += str(i) + ","
# print("Все числа дапозона: ",result)
#
# result = ""
# j = end
# for i in range(begin, end + 1):
#     result += str(j) + ","
#     j -= 1
# print("Все числа дапозона в убыващем порядке: ",result)
#
# result = ""
# for i in range(begin, end):
#     if i % 7 == 0 and i != 0:
#         result += str(i) + ","
# print("Все числа, кратные семи: ",result)
#
# count = 0
# for i in range(begin, end+1):
#     if i % 5 == 0 and i != 0:
#         count+=1
# print("Количество чисел, кратных пяти: ",count)

#Задание 3

string = input().split(" ")
begin = int(string[0])
end = int(string[1])
result = ""
for number in range(begin, end + 1):
    if number % 3 == 0 and number % 5 != 0:
        result += "Fizz: " + str(number) + ", "
    elif number % 5 == 0 and number % 3 != 0:
        result += "Buzz: " + str(number) + ", "
    elif number % 15 == 0:
        result += "Fizz Buzz: " + str(number) + ", "
    else:
        result += "Число: " + str(number) + ", "
print(result)