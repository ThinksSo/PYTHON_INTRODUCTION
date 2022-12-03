# Анонимные, lambda функции
def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)


print('lambda функции')
calc(lambda x, y: x+y, 4, 5)
print('--------------------------------')


# List Comprehension
even_list = [i for i in range(1, 21) if i % 2 == 0]
print('List Comprehension')
print(even_list)
print('--------------------------------')


# В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38 Получить: [(2, 4), (8, 64), (38, 1444)]
path = '/Users/oleg/Documents/ПРОГРАММЫ/PYTHONPROG/HelloPython/numbers.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e**2))
print('Even numbers from file')     # [(2, 4), (8, 64), (38, 1444)]
print(out)
print('--------------------------------')


# Анонимные, lambda функции
def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


# Функция filter

# data = '1 2 3 5 8 15 23 38'.split()
# data = select(int, data)
# data = where(lambda e: not e % 2, data)
# data = list(select(lambda e: (e, e**2), data))
# print(data)
# print('--------------------------------')

data_list = [x for x in range(10)]
result = list(filter(lambda x: not x % 2, data_list))

print('Функция filter')
print(result)
print('--------------------------------')

# Функция map
data = '1 2 3 5 8 15 23 38'.split()
data = list(map(int, data))
data = list(filter(lambda e: not e % 2, data))
data = list(map(lambda e: (e, e**2), data))
print('Функция map')
print(data)
print('--------------------------------')


new_data = list(map(int, input('Enter numbers with space: ').split()))
print(new_data)
print('--------------------------------')


# Функция zip
users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6']
ids = [3, 5, 7, 8, 12, 2]
age = [17, 34, 23, 45, 29, 44]

all_data = list(zip(users, ids, age))
print('Функция zip')
print(all_data) # [('user1', 3, 17), ('user2', 5, 34), ('user3', 7, 23), ('user4', 8, 45), ('user5', 12, 29), ('user6', 2, 44)]
print('\n')
