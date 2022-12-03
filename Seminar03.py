import random

# 17. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример: - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input())
mult = 1
new_list = [random.randint(-n, n) for _ in range(n)]
print(new_list)

with open('file.txt', 'w', encoding='utf-8') as file:
    count = random.randint(1, n)
    for _ in range(count):
        file.write(f'{random.randint(0, n-1)}' + '\n')

with open('file.txt', 'r', encoding='utf-8') as file:
    index_list = file.read().splitlines()
    for index in index_list:
        mult *= new_list[int(index)]
print(index_list)
print(mult)


# 1. ввести кол-во строк, потом строки. Строки должны записаться в текстовый файл.
# После вводим число, если есть число в файле, то написать ДА


# 1. ввести кол-во строк, потом строки. Строки должны записаться в текстовый файл.
# После вводим число, если есть число в файле, то написать ДА


# КОЛЛЕКЦИИ

# list
some_list = [1, 2, 3, 2, 0, 'fgd', True]
print(f'{some_list} - список')

#tuple
some_tuple = tuple(some_list)
some_tuple2 = (3, 54, 83, 832)
print(some_tuple, some_tuple2, 'кортежи')

#set
some_set = set(some_list)
some_set2 = {2, 3, 4, 9, 10}
some_set2.add(8)
some_set2.remove(3)

#frozenset
some_frozenset = frozenset(some_set)
some_frozenset2 = frozenset((3, 4, 5, 10))

#dict
some_dict = {1: True, 2: 'second'}