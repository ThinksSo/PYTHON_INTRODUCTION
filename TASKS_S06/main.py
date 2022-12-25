# Задача 5: Дан список интов, повторяющихся элементов в списке нет.
# Нужно преобразовать это множество в строку,
# сворачивая соседние по числовому ряду числа в диапазоны.
# Примеры: [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"; [1,4,3,2] => "1-4"; [1,4] => "1,4"
print('\n \t Task 5 Range list')


def range_list(num_list):
    print('original list', '\t', num_list)
    num_list.sort()
    new_list = []
    print('sorted list', '\t', num_list)
    first = -1
    last = -2
    for i in num_list:
        if i != last + 1:
            if first != -1:
                new_list.append(f'{last}') if first == last else new_list.append(
                    f'{first} - {last}')
            first = i
        last = i
    new_list.append(f'{last}') if first == last else new_list.append(
        f'{first} - {last}')
    print('result', '\t'*2, new_list, '\n')


numbers = [1, 4, 5, 2, 3, 9, 8, 11, 0]
range_list(numbers)

numbers = [1, 4, 3, 2]
range_list(numbers)

numbers = [1, 4]
range_list(numbers)


# Задача 6: Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB BBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
print('\n \t Task 6 RLE')


def zip_text(srt_list):
    if type(srt_list) == str:
        print(srt_list)
        index = 0
        count = 1
        zip_list = ''
        while index < len(srt_list) - 1:
            if srt_list[index] == srt_list[index + 1]:
                count += 1
            else:
                zip_list += (str(count) + srt_list[index])
                count = 1
            index += 1
        zip_list += (str(count) + srt_list[index])
        print(zip_list, '\n')
    else:
        print("It's not a string \n")

text = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB BBBBBBBBBBBBBBBBBBBBBBBB'
zip_text(text)

text = 'aadddgfgggssss uuuu pppppp'
zip_text(text)

num = 123,34
zip_text(num)
