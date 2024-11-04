#Ж
# print(' '*20, '_'*45)
# i = 1
# while i < 40:
#     print(" "*20, "|", "*" * i if i <= 20 else "*" * (40 - i), " " * (40 - i) if i <=20 else " " * i, "|")
#     i+=1
# print(' ' * 20, '_' * 45)


#E

# print(' '*19, '-'*46)
# i = 1
# while i < 40:
#     if i <= 20:
#         print(" " * 20 + "|", "*" * i, " "* (40 - i*2), "*" * i, "|")
#     else:
#         print(" " * 20 + "|", "*" * (40-i), " " * ((i-20) * 2), "*" * (40-i), "|")
#     i+=1
# print(' ' * 19, '-' * 46)

#ДЗ 13 задание 2

sp = [-1, -2, -4, -5, 0, 3, 5, 6, 63, 4]
pos = 0
neg = 0
nul = 0
for x in sp:
    if x < 0:
        neg += 1
    if x > 0:
        pos += 1
    if x == 0:
        nul += 1
    print(max(sp))
    print(min(sp))
    print(pos, neg, nul)