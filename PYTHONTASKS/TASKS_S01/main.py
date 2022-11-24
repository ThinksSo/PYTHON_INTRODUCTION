import math

# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным. Пример: 6 -> да, 7 -> да, 1 -> нет
print('\n \t S1 Task 01: day of week')
daysOfWeek = ["Monday", "Tuesday", "Wednesday",
              "Thursday", "Friday", "Saturday", "Sunday"]
dayNum = int(input('Enter day number from 1 to 7: ')) - 1

if dayNum < 0 or dayNum > 6:
    print("invalid input")
elif dayNum == 5 or dayNum == 6:
    print(f"{daysOfWeek[dayNum]} - day off!!!")
else:
    print(daysOfWeek[dayNum], '- go to work')


# 2. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('\n \t S1 Task 02: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            print(x, y, z, ' -> ', end='\t')
            statem1 = not (x or y or z)
            statem2 = not x and not y and not z
            if statem1 == statem2:
                print('True')
            else:
                print('False')


# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  которой находится эта точка (или на какой оси она находится).
# Пример: # - x=34; y=-30 -> 4, # - x=2; y=4-> 1, # - x=-34; y=-30 -> 3
print('\n \t S3 Task 03: The axis')
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
if x == 0 and y == 0:
    print('Error')
elif x == 0 or y == 0:
    print('On the axis')
elif x > 0 and y > 0:
    print(x, ', ', y, ' -> 1')
elif x > 0 and y < 0:
    print(x, ', ', y, ' -> 2')
elif x < 0 and y < 0:
    print(x, ', ', y, ' -> 3')
else:
    print(x, ', ', y, ' -> 4')


# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
print('\n \t S3 Task 04: The axis')
axis = int(input('enter a quarter axis: '))
if axis < 1 or axis > 4:
    print("invalid input")
elif axis == 1:
    print(axis, ' ->  x > 0, y > 0')
elif axis == 2:
    print(axis, ' ->  x > 0, y < 0')
elif axis == 3:
    print(axis, ' ->  x < 0, y < 0')
else:
    print(axis, ' ->  x > 0, y < 0')


# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример: # - A (3,6); B (2,1) -> 5,09, A (7,-5); B (1,-1) -> 7,21
print('\n \t S3 Task 5: line length')
x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
ac = y2 - y1
bc = x2 - x1
print(round(math.sqrt(ac ** 2 + bc ** 2), 2))
print('\n')
