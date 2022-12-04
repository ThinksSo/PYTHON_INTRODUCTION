from random import randint

# 22 Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
print('\n \t S3 Task 22: Sum of odd positions')
any_list = [randint(1, 10) for _ in range(5)]
sum = 0
print(any_list)
for index in range(1, len(any_list), 2):
    sum += any_list[index]
print(' sum odd pos = ', sum)

# 23 # Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]
print('\n \t S3 Task 22: product of num pairs')
some_list = [randint(1, 10) for _ in range(randint(1, 10))]
print(some_list)
new_list = []
for i in range(0, (len(some_list) - 1) // 2 + 1):
    new_list.append(some_list[i] * some_list[len(some_list) - 1 - i])
print(new_list)


# 24 Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
print('\n \t S3 Task 24: min-max fractional')
numbers = [float((input())) for _ in range(
    int(input('enter number of fractional numbers: ')))]
minim = 1
maxim = 0
for el in numbers:
    if el % 1 < minim and el % 1 != 0:
        minim = el % 1
    else:
        if el % 1 > maxim:
            maxim = el % 1
print(f'max - minim = {round(maxim - minim, 2)}')


# 25 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: - 45 -> 101101, - 3 -> 11 , - 2 -> 10
print('\n \t S3 Task 23: decimal - binary')
decim = int(input('Enter decimal num: '))
bin = ''

while decim > 0:
    bin = str(decim % 2) + bin
    decim = decim // 2
print('=> ', bin)
print('\n')


# 26 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
print('\n \t S3 Task 26: Fibbonachi')
k = int(input('Enter num: '))
fib_list = [0] * (2 * k + 1)
fib_list[k + 1] = 1
for i in range(k + 2, 2 * k + 1):
    fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
for i in range(k - 1, -1, -1):
    fib_list[i] = fib_list[i + 2] - fib_list[i + 1]
print(fib_list)
