#Домашнее задание "Операторы ветвлений." Часть 3

#Задание 1

# string = input("Введите число от 1 до 100: ")
# if 0 < int(string) > 100:
#     print("Введеное число вне диапазона")
# else:
#     number = int(string)
#     if number % 3 == 0 and number % 5 != 0:
#         print("Fizz")
#     if number % 5 == 0 and number % 3 != 0:
#         print("Buzz")
#     if number % 15 == 0:
#         print("Fizz Buzz")
#     else:
#         print("Число: ", number)

#Задание 2

# string = input("Введите число и степень: ").split(" ")
# number = int(string[0])
# stepen = int(string[1])
# if 0 <= stepen <=7:
#     result = number ** stepen
#     print("Результат: ", result)

#Задание 3

# string = input("Введите стоимость, с какого оператора, на какой оператор: ").split(" ")
# price = float(string[0])
#
# # mtom = 0 # с мтс на мтс 0.5 руб
# # mtob = 1 # с мтс на билайн 1 руб
# # mtot = 2 # с мтс на теле2 0.9 руб
# # ttot = 3 # с теле2 на теле2 0.6 руб
# # ttob = 4 # с теле2 на билайн 1.1 руб
# # ttom = 5 # с теле2 на мтс 0.9 руб
# # btob = 6 # с билайн на билайн 0.7 руб
# # btom = 7 # с билайн на мтс 1 руб
# # btot = 8 # с билайн на теле2 1.1 руб
#
# if string[1] =="m" and string[2] =="m":
#     result = price * 0.5
#     print("Стоимость разговора: " , result , "руб")
# if string[1] =="m" and string[2] =="b":
#     result = price * 1
#     print("Стоимость разговора: " , result , "руб")
# if string[1] == "m" and string[2] == "t":
#     result = price * 0.9
#     print("Стоимость разговора: " , result , "руб")
# if string[1] =="t" and string[2] =="t":
#     result = price * 0.6
#     print("Стоимость разговора: " , result , "руб")
# if string[1] =="t" and string[2] =="b":
#     result = price * 1.1
#     print("Стоимость разговора: " , result , "руб")
# if string[1] == "t" and string[2] == "m":
#     result = price * 0.9
#     print("Стоимость разговора: " , result , "руб")
# if string[1] =="b" and string[2] =="b":
#     result = price * 0.7
#     print("Стоимость разговора: " , result , "руб")
# if string[1] =="b" and string[2] =="m":
#     result = price * 1
#     print("Стоимость разговора: " , result , "руб")
# if string[1] == "b" and string[2] == "t":
#     result = price * 1.1
#     print("Стоимость разговора: " , result , "руб")

#Задание 4

string = input("Введите уровень продаж трех менеджеров через пробел: ").split(" ")
base = 200 #базовая ставка 200$
percent = 0
prem = 0
status = 0
if int(string[0]) > int(string[1]) > int(string[2]) or int(string[0]) > int(string[2]) > int(string[1]):
    status = 0
    print("Премия 200$ начислена менеджеру №:", status+1)
if int(string[1]) > int(string[2]) > int(string[0]) or int(string[1]) > int(string[0]) > int(string[2]):
    status = 1
    print("Премия 200$ начислена менеджеру №:", status+1)
if int(string[2]) > int(string[1]) > int(string[0]) or int(string[2]) > int(string[0]) > int(string[1]):
    status = 2
    print("Премия 200$ начислена менеджеру №:", status+1)
    print(status)
k = 0
for i in string:
    zp = int(i)
    if 0 < zp < 500:
        percent = 0.03
    elif 500 <= zp < 1000:
        percent = 0.05
    elif zp >= 1000:
        percent = 0.08
    if k == status:
        prem += 200
        print("Зарплата менеджера №",k+1, ": ", base * (1 + percent) + prem)
    else:
        print("Зарплата менеджера №",k+1, ": ", base * (1 + percent))
    k += 1
