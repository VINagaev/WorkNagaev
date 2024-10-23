#Работа в классе 23.10.24

# customers=['Bob','Anna','Joe','Bill','Nick']
# # print(customers[2:4])
# # print(customers[2:4][1])
# # print(customers[2:4][1][0])
# result=""
# for i in customers:
#     result += i + " "
#     print(i)
# print(result.rstrip(" ").split(" ")[:3])


# matrix=[[1,2,3],[4,5,6],[7,8,9],[10,[11,[13,15,16],14],12]]
# print(matrix[3][1][1][2])


# a1 = 10
# b1 = 20
# matrix=[[1,2,3],[4,5,6],[7,8,9],[a1,[13,14,[15,16,"OK"]],12,b1]]
# search = "OK"
# for i in matrix:
#     print("ypoBeHb 1", i)
#     if search in i:
#         print("HaIIIJIu OK")
#         break
#     else:
#         for vtoroy in i:
#             print("2 yPoDeHb", vtoroy)
#             if search == vtoroy:
#                 print("HaIIIJIu OK")
#                 break
#             else:
#                 if type(vtoroy) is list:
#                     for tretiy in vtoroy:
#                         print(tretiy)
#                         if search == vtoroy:
#                             print("HaIIIJIu OK")
#                             break
#                         else:
#                             if type(tretiy) is list:
#                                 for chetv in tretiy:
#                                     print(chetv)
#                                     if search == chetv:
#                                         print("HaIIIJIu OK")
#                                         break


# разбор дз
# задание 3

# while True:
#     chislo = int(input())
#     if chislo == 7:
#         print("Good bye!")
#         break
#     elif chislo > 0:
#         print("positive")
#     elif chislo < 0:
#         print("negative")
#     elif chislo == 0:
#         print("zero")

# задание 1 дз 10

string = input().split(" ")
numbers = []
for i in range(int(string[0]), int(string[1])):
    count = 0
    j = 1
    while j <= i:
        if i % j == 0:
            count += 1
        j += 1
    if count == 2:
        numbers.append(i)
print("простые числа: ", numbers)
