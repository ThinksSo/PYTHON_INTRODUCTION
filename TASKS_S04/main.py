import math
from random import randint


# 30 Вычислить число c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
print('\n \t S4 Task 30: Number with given precision')
num_pi = math.pi
print(num_pi)
precise = len(input('Enter d (0.0...1: ')) - 2
res = round(num_pi, precise)
print(res)


# 31 Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
print('\n \t S4 Task 31: Prime factors')


def prime(a):
    k = 0
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            k = k + 1
    if (k <= 0):
        return a
    else:
        return 0


n = int(input('Enter number: '))
pf = []
for i in range(1, n):
    if n % i == 0:
        pf.append(i)
        n = n / i
    else:
        i += 1

new_pf = []
for j in range(len(pf)):
    if prime(pf[j]) != 0:
        new_pf.append(pf[j])

# print(pf)
print(new_pf)


# 32 Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
print('\n \t S4 Task 32: Unique')
num_list = [randint(1, 10) for _ in range(randint(5, 10))]
print(num_list)

count = 0
unique_num = []
for c in range(len(num_list)):
    if num_list.count(num_list[c]) == 1:
        unique_num.append(num_list[c])
print(unique_num)


# 33 Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# 35 Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
print('\n \t S4 Task 35: Polynomials addition')

# 2x^2 + 4x + 5 = 0
# x^2 + 2x + 5 = 0

# import os
# print (os.getcwd())

with open('file1.txt', 'r', encoding='utf8') as file:
    p1 = file.read()
with open('file2.txt', 'r', encoding='utf8') as file:
    p2 = file.read()

print(p1)
print(p2)

# Функция сложения. Варинат 1
# def poly_add(p1, p2):
#     i = 0
#     su = 0
#     j = 0
#     result = []
#     if len(p1) == 0:
#         return p2
#     if len(p2) == 0:
#         return p1
#     while i < (len(p1)-1) and j < (len(p2)-1):
#         if int(p1[i][1]) == int(p2[j][1]):
#             su = p1[i][0]+p2[j][0]
#             if su != 0:
#                 result.append((su, p1[i][1]))
#             i = i+1
#             j = j+1
#         elif p1[i][1] > p2[j][1]:
#             result.append((p1[i]))
#             i = i+1
#         elif p1[i][1] < p2[j][1]:
#             result.append((p2[j]))
#             j = j+1
#     if p1[i:] != []:
#         for k in p1[i:]:
#             result.append(k)
#     if p2[j:] != []:
#         for k in p2[j:]:
#             result.append(k)
#     print(result)

# Функция сложения. Варинат 2
# def poly_add(x, y):
#     result = []
#     min_len = min(len(x), len(y))
#     for i in range(min_len):
#         if x[i][1] == y[i][1]:
#             r = x[i][0] + y[i][0]
#         if r != 0:
#             result.append((r, x[i][1]))
#         if x[i][1] != y[i][1]:
#             result.append((y[i]))
#             result.append((x[i]))
#     print(result)

# poly_add(p1, p2)
