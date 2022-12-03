from random import randint

# 22 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# any_list = [randint(1, 10) for _ in range(5)]
# sum = 0
# print(any_list)
# for index in range(1, len(any_list), 2):
#     sum += any_list[index]
# print(sum)


# 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]

# some_list = [randint(1, 10) for _ in range(5)]
# new_list = []
# for i in range(0, (len(some_list) - 1) // 2 + 1):
#     new_list.append(some_list[i] * some_list[len(some_list) - 1 - i])
# print(new_list)

# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# other_list = [(input()) for _ in range(int(input()))]
# minim = 1
# maxim = 0
# for el in other_list:
#     if el % 1 < minim and el % 1 != 0:
#         minim = el % 1
#     else:
#         if el % 1 > maxim:
#             max = el % 1
# print(minim)
# print(maxim)


# another_list = [(input()) for _ in range(int(input()))]
# minim = 1
# maxim = 0
# for el in another_list:
#     if '.' in el:
#         if float('0.' + el.split('.')[i]) < minim:
#             minim = float('0.' + el.split('.')[i])
#         else:
#             if float('0.' + el.split('.')[i]) > maxim:
#                 maxim = float('0.' + el.split('.')[i])
# print(maxim - minim)


# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# n = int(input())
# out_str = ''
# print(bin(n)[2:])

# while n != 0:
#     out_str = str(n % 2) + out_str
#     n //= 2
# print(out_str)


# 26.

# k = int(input())
# k_list = [0] * (2 * k + 1)
# k_list[k + 1] = 1
# for i in range(k + 2, 2 * k + 1):
#     k_list[1] = k_list[i - 1] + k_list[i - 2]
# for i in range(k - 1, -1, -1):
#     k_list[1] = k_list[i + 2] - k_list[i + 1]
# print(k_list)


# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

any_str = input('Enter numbers in line with space: ')
# int_list = any_str.split()
int_list = list(map(int, any_str.split()))
# for ind in range(9, len(int_list)):
#     int_list[ind] = int(int_list[ind])
print(max(int_list))
print(min(int_list))


# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
#  2) с помощью дополнительных библиотек Python

# Option 1:
import math
a = float(input("Введите значение a= "))
b = float(input("Введите значение b= "))
c = float(input("Введите значение c= "))
D = b ** 2 - 4 * a * c
print(D)
if D < 0:
  print("Корней нет")
elif D == 0:
  x = -b / 2 * a
  print (x)
else:
  x1 = (-b + math.sqrt(D)) / (2 * a)
  x2 = (-b - math.sqrt(D)) / (2 * a)
  print(x1)
  print(x2)

# Option 2:
import sympy
a = float(input("Введите значение a= "))
b = float(input("Введите значение b= "))
c = float(input("Введите значение c= "))
x = sympy.Symbol('x')
print(sympy.solve(a * x ** 2 + b * x + c))


# адайте два числа. 
# Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
a = int(input())
b = int(input())
print(sympy.lcm(a, b))
