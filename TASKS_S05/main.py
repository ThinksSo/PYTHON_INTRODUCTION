# Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension

# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".
print('\n \t Task 38 words delite')
my_text = 'Пора, красавица, проснись: Открой сомкнуты негой взоры \
Навстречу северной Авроры, Звездою севера явись!'
print(my_text)

text_list = list(filter(
    lambda i: 'а' not in i and 'б' not in i and 'в' not in i, my_text.split()))
print(text_list)

# 39. Создайте программу для игры в ""Крестики-нолики"".
print('\n \t Task 39 tic-tac-toe \n')
field = list(range(1, 10))

def game_field(field):
    for i in range(3):
        print(field[0+i*3], '\t', field[1+i*3], '\t', field[2+i*3])
        print('\n')

def win_cell(field):
    win_line = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for j in win_line:
        if field[j[0]] == field[j[1]] == field[j[2]]:
            return field[j[0]]
    return False
   

def take_input(player_symbol):
    valid = False
    while not valid:
        player_answer = input('Cell number for ' + player_symbol + ': ')
        try:
            player_answer = int(player_answer)
        except:
            print('Invalid input')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(field[player_answer-1]) not in "X0"):
                field[player_answer-1] = player_symbol
                valid = True
            else:
                print("Cell is already filled")
        else:
            print("Invalid input. Enter number from 1 to 9 ")


def game(field):
    counter = 0
    win = False
    while not win:
        game_field(field)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("0")
        counter += 1
        if counter > 4:
            turn = win_cell(field)
            if turn:
                print('\n', turn, ' - YOU WIN!')
                win = True
                break
        if counter == 9:
            print('\n, DRAW!')
            break
    game_field(field)

game(field)


# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
print('\n \t Task 40 Zip text from file')


def ziptext(file, zipfile):
    with open(file, 'r', encoding='utf-8') as text:
        with open(zipfile, 'w', encoding='utf-8') as res:
            file_str = text.readline()
            index = 0
            count = 1
            while index < len(file_str) - 1:
                if file_str[index] == file_str[index + 1]:
                    count += 1
                else:
                    res.write(str(count) + file_str[index])
                    count = 1
                index += 1
            res.write(str(count) + file_str[index])
    print(file_str)


def unzip(zipfile, unzipfile):
    with open(zipfile, 'r', encoding='utf-8') as text:
        with open(unzipfile, 'w', encoding='utf-8') as res:
            file_str = text.readline()
            count = 1
            for letter in file_str:
                if letter.isdigit():
                    count = count + int(letter) - 1
                else:
                    res.write(count * letter)
                    count = 1
    print(file_str, '\n')



ziptext('TASKS_S05/file.txt', 'TASKS_S05/zipfile.txt')
unzip('TASKS_S05/zipfile.txt', 'TASKS_S05/unzipfile.txt')
