#Работа в классе 21.10.24

# customers=['Bob','Anna','Joe','Bill','Nick']
# list2 = [i for i in customers if i!=customers[1]]
# print(list2)

#Разбор дз №9

# st = input().split(" ")
# ev = 0
# ev_n = []
# od = 0
# od_n = []
# nine = 0
# nine_n = []
# for i in range(int(st[0]), int(st[1])):
#  if i % 2 ==0:
#   ev += 1
#   ev_n.append(i)
#   if i % 2 !=0:
#    od += 1
#    od_n.append(i)
#    if i % 9 == 0:
#     nine += 1
#     nine_n.append(i)
# print("Колличество четных: ", ev, "ср. арифм.: ", sum(ev_n) / ev)
# print("Колличество не четных: ", od, "ср. арифм.: ", sum(od_n) / od)
# print("Колличество кратных 9: ", nine, "ср. арифм.: ", sum(nine_n) / nine)

st = input().split(" ")
even = [i for i in range(int(st[0]), int(st[1])) if i % 2 == 0]
odds = [i for i in range(int(st[0]), int(st[1])) if i % 2 != 0]
int9 = [i for i in range(int(st[0]), int(st[1])) if i % 9 == 0]
print("kol-vo 4et: ", len(even), "sr.arefm: ", sum(even) / len(even))
print("kol-vo ne 4et: ", len(odds), "sr.arefm: ", sum(odds) / len(odds))
print("kol-vo 9: ", len(int9), "sr.arefm: ", sum(int9) / len(int9))