# 11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#     *Пример: Для N = 5: 1, -3, 9, -27, 81
print('\n \t S3 Task 11')
n = int(input('Enter n: '))
for i in range(n):
    print((-3) ** i, end=', ')
print('\n')


# 12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# *Пример:*  Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
print('\n \t S3 Task 12')
some_dict = {}
n = int(input('Enter number: '))
for i in range(1, n + 1):
    some_dict[1] = 3 * i + 1
print(some_dict)
print('\n')

# 13. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
print('\n \t S3 Task 13')
str1 = input('Enter first string: ')
str2 = input('Enter second string: ')
print(str1.count(str2) or str2.count(str1))
print('\n')

# s1 = input()
# s2 = input()
# ind = 0
# c = 0
# while ind < len (s1):
#     if s1[ind: ind + len(s2)] == s2:
#         c += 1
#         ind += len(s2)
#     else:
#         ind += 1
# print(c)