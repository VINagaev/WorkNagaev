# def test13():
#     print("OK")
# test13(

import re
s = input()
result = eval(s)
print(result)
op = re.findall(r'[(\-/\+*)]', s)
print(op)
numbers = re.split(r'[(\-/\+*)]', s.replace(" ",""))
print(numbers)
i = 0
result = 0
res = []
j = 0
isk = []
while j < len(numbers):

    if op[j] == "/":
        res.append(int(numbers[j]) / int(numbers[j+1]))
        numbers.pop(j)
        print(numbers)
        numbers.pop(j)
        print(numbers)
        numbers.insert(j, res[0])
        print(numbers)
        op.pop(j)
        print(numbers)
        j = 0
        res.clear()
    if op[j] == "*":
        res.append(int(numbers[j]) / int(numbers[j + 1]))
        numbers.pop(j)
        print(numbers)
        numbers.pop(j)
        print(numbers)
        numbers.insert(j, res[0])
        print(numbers)
        op.pop(j)
        print(numbers)
        j = 0
        res.clear()
    j += 1
print(op, numbers)
result2 = []
h = 0
while h < len(numbers):
    if op[j] == "+":
        result2.append(int(numbers[h]) + int(numbers[h + 1]))
        numbers.pop(h)
        numbers.pop(h)

