from random import shuffle

# 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: # - 6782 -> 23, # - 0,56 -> 11
print('\n \t S2 Task 14: the sum of the digits in a number')
num = input('Enter number: ')
sum = 0
for i in num:
    if i == '.' or i == ',' or i == '-':
        continue
    else:
        sum += int(i)
print('-> ', sum)


# 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
print('\n \t S2 Task 15: Factorial')
n = int(input('N = '))
mult_list = []
mult = 1
for i in range(1, n + 1):
    mult *= i
    mult_list.append(mult)
print(mult_list)


# 16. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
print('\n \t S2 Task 16')
num = int(input('n = '))
num_list = {}
sum_list = 0
for i in range(1, num + 1):
    value = round((1 + 1 / i) ** i, 3)
    num_list[i] = value
    sum_list += value
print(num_list, ' -> ', sum_list)


# 18. Реализуйте алгоритм перемешивания списка.
print('\n \t S2 Task 18 List shuffle')
some_lst = []
some_lst_length = int(input('Enter list length: '))
for i in range(some_lst_length):
    some_lst.append(str(input(f'Enter {i+1} element: ')))
print('Initial list ', some_lst)
shuffle(some_lst)
print('Shuffle list ', some_lst)
