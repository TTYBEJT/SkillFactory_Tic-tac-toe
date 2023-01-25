print("""Правила игры: Нужно собрать 3 знака в ряд (по горизонтали, вертикали или диагонали),
при этом нужно помешать противнику сделать то же самое.
Это игровое поле, игроки ходят по очереди, можно выбирать значение 1, 2 или 3 (строка или столбец).
 Первый ходит игрок Х 
 """)
Play = True


def print_board():
    for row in board:
        print(" | ".join(row[0:4]) + " |")
        print("_______________")


def test(i):
    if i.isdigit():
        if 0 < int(i) < 4:
            return False
        else:
            print("Введены неправильные данные. Используются значения 1, 2 и 3. Попробуй выбрать одно из них")
            return True
    else:
        print("Шуточки? Давай работать с Цифрами 1, 2 и 3. Попробуй выбрать одну из этих цифр")
        return True


def Win():
    '''player_trio = [player, player, player]
    combo_1, combo_2, combo_3, combo_4, \
    combo_5, combo_6, combo_7, combo_8 = \
        [board[1][1], board[2][1], board[3][1]], \
        [board[1][1], board[1][2], board[1][3]], \
        [board[2][1], board[2][2], board[2][3]], \
        [board[3][1], board[3][2], board[3][3]], \
        [board[1][2], board[2][2], board[3][2]], \
        [board[1][3], board[2][3], board[3][3]], \
        [board[1][1], board[2][2], board[3][3]], \
        [board[1][3], board[2][2], board[3][1]]
    #    combo = [combo_1, combo_2, combo_3, combo_4, combo_5, combo_6, combo_7, combo_8]'''
    if any(x == [player, player, player] for x in
           [[board[1][1], board[2][1], board[3][1]], [board[1][1], board[1][2], board[1][3]],
            [board[2][1], board[2][2], board[2][3]], [board[3][1], board[3][2], board[3][3]],
            [board[1][2], board[2][2], board[3][2]], [board[1][3], board[2][3], board[3][3]],
            [board[1][1], board[2][2], board[3][3]], [board[1][3], board[2][2], board[3][1]]]):
        return True
    else:
        return False


def Yes_or_no():
    print("Играем еще раз? ( Y (Да) или N (Нет) )")
    Ans = input()
    if Ans == "Y":
        return True
    elif Ans == "y":
        return True
    else:
        return False


def Game():
    while True:
        global player
        print_board()

        print(f"Игрок {player} выбери ячейку (строка)")
        row = input("Строка: ")
        res = test(row)
        if res:
            continue

        row = int(row)

        print(f"Игрок {player} выбери ячейку (столбец)")
        col = input("Столбец: ")
        res = test(col)
        if res:
            continue

        col = int(col)

        if board[row][col] != '-':
            print("Эта ячейка занята. Попробуй другую")
            continue

        board[row][col] = player

        win = Win()
        if win:
            print_board()
            print(f"Победил игрок {player}")
            print("Игра окончена")
            break

        else:
            if player == "X":
                player = "O"
            else:
                player = "X"


while Play:
    board = [[' ', '1', '2', '3'], ['1', '-', '-', '-'], ['2', '-', '-', '-'], ['3', '-', '-', '-']]
    player = "X"
    Game()
    Play = Yes_or_no()
