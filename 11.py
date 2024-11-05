# def print_right_upper_triangle(height):
#     for i in range(height):
#         print(' ' * i + '*' * (height - i))
#
#
# def print_left_lower_triangle2(height):
#     for i in range(height):
#         print('*' * (i + 1) + ' ' * (height + i))
#
#
# def print_triangle_upside_down(height):
#     for i in range(height // 2):
#         print(' ' * i + '*' * (2 * (height // 2 - i) - 1))
#
#
# def print_triangle(height):
#     for i in range(height // 2):
#         print(' ' * (height // 2 - i - 1) + '*' * (2 * i + 1))
#
#
# def print_triangles_simultaneously(height):
#     print_triangle_upside_down(height)
#     print_triangle(height)
#
#
# def print_left_lower_triangle9(height):
#     for i in range(height):
#         print('*' * (height - i) + ' ' * (i - 1))
#
#
# def print_left_lower_triangle10(height):
#     for i in range(height):
#         print(' ' * (height - i - 1) + '*' * (i + 1))
#
#
# while True:
#     print("\nМеню:")
#     print("1. Треугольник в правом верхнем углу")
#     print("2. Треугольник в левом нижнем углу")
#     print("3. Равносторонний треугольник с основанием по верхнему краю")
#     print("4. Равносторонний треугольник с основанием по нижнему краю")
#     print("5. Равносторонние треугольники с основаниями по верхнему и нижнему краям")
#     print("9. Треугольник в верхнем левом углу")
#     print("10. Треугольник в нижнем правом углу")
#     print("0. Выход")
#
#     choice = int(input("Введите свой выбор: "))
#
#     if choice == 1:
#         height = int(input("Введите размер квадрата: "))
#         print_right_upper_triangle(height)
#     elif choice == 2:
#         height = int(input("Введите размер квадрата: "))
#         print_left_lower_triangle2(height)
#     elif choice == 3:
#         height = int(input("Введите размер квадрата: "))
#         print_triangle_upside_down(height)
#     elif choice == 4:
#         height = int(input("Введите размер квадрата: "))
#         print_triangle(height)
#     elif choice == 5:
#         height = int(input("Введите размер квадрата: "))
#         print_triangles_simultaneously(height)
#     elif choice == 9:
#         height = int(input("Введите размер квадрата: "))
#         print_left_lower_triangle9(height)
#     elif choice == 10:
#         height = int(input("Введите размер квадрата: "))
#         print_left_lower_triangle10(height)
#     elif choice == 0:
#         break
#     else:
#         print("Неверный выбор. Пожалуйста, введите число от 0 до 10.")


# for i in range(1, 7, 2):
#     i = ' ' * ((7 - i) // 2) + '*' * i
#     print(i)
# for i in range(7, 0, -2):
#     i = ' ' * ((7 - i) // 2) + '*' * i
#     print(i)
#
# a = 10
# for i in range(a, 0, -1):
#     print('*' * i)
# a = 10
# for i in range(1, a+1):
#     print('*' * i)
# a = 10
# for i in range(2,a):
#     if i == 2:
#         print('*')
#     print('*' + " " * (i-2) + '*')
#     if i == (a - 1):
#         print('*' * a)
# h = int(input('h '))
# w = int(input('w '))
# for i in range(1, h + 1):
#     if i == 1 or i == h:
#         print('*' * w)
#     else:
#         print('*' + " " * (w - 2) + '*')
# def pattern(n):
#     # print upper triangle
#     for i in range(n):
#         for j in range(n - i - 1):
#             # printing spaces
#             print(" ", end=" ")
#
#         for j in range(i + 1):
#             # printing stars
#             print("* ", end="")
#         print()
#
#     # print lower triangle
#     for i in range(n - 1):
#         for j in range(i + 1):
#             # printing spaces
#             print(" ", end=" ")
#
#         for j in range(n - i - 1):
#             # printing stars
#             print("* ", end="")
#         print()
#
#
# # take inputs
# n = int(input('Enter the number of rows: '))
#
# # calling function
# pattern(n)

# n = 7
# n_mid = int((7 + 1) / 2)
# star = '*'
#
# for j in range(1, n_mid + 1):
#     print(star * j)
# for i in range(n_mid - 1, 0, -1):
#     print(star * i)
# print()

elif s == "6":
    for i in range(1, (7 + 1) // 2, 2):
     print((7 + 1) / 2 + "*" * i)

# elif s == "6":
# for i in range(1, 7, 2):
#     print(' ' * ((7 - i) // 2) + '*' * i)