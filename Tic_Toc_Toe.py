playing_area = ([' ', 1, 2, 3],
                [1, '-', '-', '-'],
                [2, '-', '-', '-'],
                [3, '-', '-', '-']
                )


# Вывод поля
def area_output():
    for i in range(4):
        for j in range(4):
            print(playing_area[i][j], end=' ')
        print()


# Основной код игры
def the_game():
    global k

    if k == 'x':
        print(f'{player_x} ваш ход')
        x = int(input('Выберите колонку в которую хотите установать символ '))
        y = int(input('Выберите столбец в которую хотите установать символ '))
        if playing_area[x][y] != '-':
            area_not_empty()
        else:
            playing_area[x][y] = 'x'
            area_output()
            check_win_condition()

        k = 'o'
        return 0

    if k == 'o':
        print(f'{player_o} введите номер поля на который хотите установить символ')
        x = int(input())
        y = int(input())
        if playing_area[x][y] != '-':
            area_not_empty()
        else:
            playing_area[x][y] = 'o'
            area_output()
            check_win_condition()

        k = 'x'
        return 0


# Проверка пустое ли поле
def area_not_empty():
    print('Данная клетка занята, выберите другую')
    return the_game()


# Проверка условий победы
def check_win_condition():
    global count

    if all([
        playing_area[1][1] == playing_area[1][2],
        playing_area[1][1] == playing_area[1][3],
        playing_area[1][1] != '-'
    ]):
        winner()
    elif all([
        playing_area[2][1] == playing_area[2][2],
        playing_area[2][1] == playing_area[2][3],
        playing_area[2][1] != '-'
    ]):
        winner()
    elif all([
        playing_area[3][1] == playing_area[3][2],
        playing_area[3][1] == playing_area[3][3],
        playing_area[3][1] != '-'
    ]):
        winner()
    elif all([
        playing_area[1][1] == playing_area[2][1],
        playing_area[1][1] == playing_area[3][1],
        playing_area[1][1] != '-'
    ]):
        winner()
    elif all([
        playing_area[1][2] == playing_area[2][2],
        playing_area[1][2] == playing_area[3][2],
        playing_area[1][2] != '-'
    ]):
        winner()
    elif all([
        playing_area[1][3] == playing_area[2][3],
        playing_area[1][3] == playing_area[3][3],
        playing_area[1][3] != '-'
    ]):
        winner()
    elif all([
        playing_area[1][1] == playing_area[2][2],
        playing_area[1][1] == playing_area[3][3],
        playing_area[1][1] != '-'
    ]):
        winner()
    elif all([
        playing_area[1][3] == playing_area[2][2],
        playing_area[1][3] == playing_area[3][1],
        playing_area[1][3] != '-'
    ]):
        winner()
    elif count == 9:
        winner()



# Вывод победителя
def winner():
    global not_win
    if k == 'x':
        print(f"{player_x} выиграл игру")
        not_win = False
    elif k == 'o'
        print(f"{player_o} выиграл игру")
        not_win = False
    else:
        print('Ничья')



# Начало игры
print('''Добро пожаловать в игру, крестики-нолики''')
player1_symbol = input("Игрок 1, выберите каким символом вы будете играть 'x' или 'o': ")

if player1_symbol == 'x':
    print(f'Игроку 2 достался символ "o"')
    player_x = 'Игрок 1'
    player_o = 'Игрок 2'
else:
    print(f'Игроку 2 достался символ "x"')
    player_x = 'Игрок 2'
    player_o = 'Игрок 1'

# Цикл отвечающий за ход игры
count = 1
not_win = True
k = 'x'
area_output()
while not_win:
    the_game()
    count += 1

print('Спасибо за игру!')