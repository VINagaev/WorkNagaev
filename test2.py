string = input("Введите 4 числа через пробел")

print(string)

numbers = string.split(" ")
print(numbers)
summa = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
print(summa)