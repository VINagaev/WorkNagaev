# Задание 4


# string = input().split(" ")
# number = []
# volume_all = []
# for i in string:
#     volume_all.append(int(i))
# premia = 200
# max_volume = 0
# print(string)
#
# for i in string:
#     volume = int(i)
#     zp = 200
#     max_volume = max(max_volume, volume)
#     if 0 < volume <500:
#         zp *= 1.03
#     elif 500 <= zp <= 1000:
#         zp *= 1.05
#     elif volume > 1000:
#         zp *= 1.08
# count_max = 0
# for i in string:
#     max_volume = max(volume_all)
#     if max_volume == int(i):
#         count_max += 1
#     print("количество максимальных значений: ",count_max)
# k = 0
# for i in string:
#     max_volume = max(volume_all)
#     print(max_volume)
#     if max_volume == int(i):
#         print("max volume", i)
#         number[k] += premia / count_max
#         k += 1
#         print(number)





#dz 8 nomer 1

# string = input().split(" ")
# begin = int(string[0])
# end = int(string[1])
# result = ""
# for i in range(begin, end):
#     if i % 7 == 0 and i != 0:
#         result += str(i) + ","
# print(result)

#nomer 2

# string = input().split(" ")
# begin = int(string[0])
# end = int(string[1])

# result = ""
# for i in range(begin, end):
#     result += str(i) + " "
# print(result)

#на убывание
# result = ""
# j = end
# for i in range(begin, end + 1):
#     result += str(i) + " "
#     j -= 1
# print(result)

#кратные 7
# result = ""
# for i in range(begin, end):
#     if i % 7 == 0 and i != 0:
#         result += str(i) + ","
# print(result)

#кол-во цифр кратны 5
# count = 0
# for i in range(begin, end+1):
#     if i % 5 == 0 and i != 0:
#         count+=1
# print(count)


#zadanie 3
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
        result += "Fizz Buzz" + str(number) + ", "
    else:
        result += "Число: " + str(number) + ", "