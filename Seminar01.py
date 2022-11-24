# 1. Программа принимает на вход два числа и проверяет, является ли одно квадратом другого
# Option 1.1
num1 = int(input('Enter first number '))
num2 = int(input('Enter second number '))
if num1 ** 2 == num2 or num2 ** 2 == num1:
    print('Yes')
else:
    print('No')
print('\n')

# Option 1.2
num1, num2 = map(int, input('Enter two numbers ').split(', '))
if num1 ** 2 == num2 or num2 ** 2 == num1:
    print('Yes')
else:
    print('No')

# 2. Программа находит минимальное из 5 чисел
# Option 2.1
numbers = []
for _ in range(5):
    n = int(input('Enter a number '))
    numbers.append(n)
max_num = numbers[0]
for elem in numbers:
    if elem > max_num:
        max_num = elem
print(f'max = {max_num} \n')

# Option 2.2
maxx: int = int(input('Enter a number '))
for _ in range(4):
    n = int(input())
    if n > maxx:
        maxx = n
print(f'max = {maxx} \n')

# Option 2.3
print(max(list(map(int, input('Enter a number ').split(', ')))))


# 3. Программа, которая на вход принимает число N и выводит числа от -N до N
# Option 3.1
n = int(input('Enter range: '))
for i in range(-n, n+1):
    print(i, end=', ')

# Option 3.2
n = int(input('Enter range: '))
print(*list(range(-n, n + 1)), sep=', ')
print('\n')

# Option 3.3
str_num = int(input('Enter range: '))
for i in range(-str_num, str_num+1):
    str_num = str(i) + ', '
print(str_num[:-2])


# 4. Программа, которая принимает на вход дробь и показывать первую цифру дробной части числа
number_new = float(input())
if number_new % 1 != 0:
    number_new *= 10
    number_new = int(number_new)
    print(' -> ', number_new % 10)
else:
    print('No')


# 5. Программа принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
n = int(input('Enter a number '))
if (n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
    print('Yes')
else:
    print('No')
