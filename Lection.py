# HELLO PYTHON
# INTRODUCTION TO PYTHON
# LESSON 1

print('\n''Hello world')
print('\n')

# типы данных и переменная
# int, float, boolean, str, list, None

# NUMBERS - ЧИСЛА
a = 123             # int
b = 1.23            # float
print(a, "\t", "-", type(a))
print(b, "\t", "-", type(b))
value = 123344
print('\n')

# STRING - СТРОКИ
s = 'Hello world'   # string
print(s)            # вывод строки
print(a, b, s)
print(a, '-', b, '-', s)
print('{} - {} - {}'.format(a, b, s))       # формат
print('{1} - {2} - {0}'.format(a, b, s))    # изменение порядка вывода
print(f'{a} - {b} - {s}')                   # интерполяция
print('\n')

# LOGIC - ЛОГИЧЕСКИЕ ПЕРЕМЕННЫЕ
f = True
print(f)
f = False
print(f)
print('\n')

# ARRAY - МАССИВ/СПИСОК
list_int = [1, 2, 3, 4]
list_str = ['a', '1', 'asd']
print(list_int)
print(list_str)
print('\n')


# INPUT - ВВОД ДАННЫХ
print('Enter x')
x = int(input())
print('Enter y')
y = int(input())
print(x, '+', y, ' = ', x+y)
print('{} {}'.format(x, y))
print(f'{x} {y}')
print('\n')

# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ

a = 12
b = -8      # унарный минус
c = a / b   # по умолчанию деление как для вещественных чисел
print('a/b = ', c)
c = a // b  # деление только целых чисел, без остатка
print('a//b = ', c)
c = a % b   # деление до остатка
print('a%b = ', c)

a = 2
b = 8
c = a ** b  # введение в степень
print('2^8 = ', c)

a = 1.3483745433
b = 3
c = round(a * b, 3)
print('a*b = ', c)

print('\n')

# LOGIC - ЛОГИЧЕСКИЕ ОПЕРАЦИИ

a = 1 < 4 < 9 < 10
b = 1 != 2
c = [1, 2]
d = [1, 2]
print(a, b, c == d)

f = 1 > 2 or 4 < 6
print(f)
list_num = [1, 2, 3, 4]
print('list = ', list_num)
print('2 in list - ', 2 in list_num)

is_odd = list_num[0] % 2 == 0
print(is_odd)
is_odd = not list_num[0] % 2
print(is_odd)

print('\n')

# УПРАВЛЯЮЩИЕ КОНСТРУКЦИИ
# if, elif, else
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a > b:
    print(a, '>', b)
elif b > c:
    print(b, '>', c, ', ', a)
else:
    print(c, '>', a, ', ', b)
print('\n')

# цикл while
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Now stop')
print('->', inverted)
print('\n')

# цикл for
for i in 1, 2, 3, 4, 5:
    print(i**2)
print('\n')

list_new = [1, 2, 3, 4, 5]
for i in list_new:
    print(i)
print('\n')

for i in range(1, 5):
    print(i)

for i in '-qwe-rty-':
    print(i)

print('\n')

# Операции со строками
text = "let's go to cinema"
print(text)
print(len(text))                # 18
print(text[2:8])                # t's go
print(text[len(text)-2:])       # ma
print('go' in text)             # True
print(text.isdigit())           # False
print(text.islower())           # True
print(text.replace('go', 'GO'))
print(text)

print('\n')

# СПИСКИ
numbers = [1, 2, 3, 4, 5]
print(numbers)
ran = range(1, 6)
numbers = list(ran)
print(numbers)
numbers[0] = 10
print(numbers)
print(f'len = {len(numbers)}')
for i in numbers:
    i *= 2
    print(i)
print(numbers)

colors = ['red', 'green', 'blue']
for e in colors:
    print(e)        # red green blue

colors.append('yellow')
print(colors == ['red', 'green', 'blue', 'yellow']) # True
colors.remove('red')    # del colors[0] - удалить элемент
print(colors)

print('\n')

# FUNCTION - ФУНКЦИИ
def f(x):
    if x == 1:
        return 'Int'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(f(arg))
print(type(f(arg)))

arg = 2.3
print(f(arg))
print(type(f(arg)))

arg = 2
print(f(arg))
print(type(f(arg)))

print('\n')
