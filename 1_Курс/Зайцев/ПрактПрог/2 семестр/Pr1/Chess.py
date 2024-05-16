def diagonal_attack(z, a, xm, ym, xpl, ypl, white_move, lub=False):
    k = []
    if z != xm and a != ym:
        z += xpl
        a += ypl
        if board[z][a] != ' . ':
            if board[z][a].isupper() != white_move and ((board[z][a] == ' q ' or board[z][a] == ' Q ' or board[z][
                a] == ' b ' or board[z][a] == ' B ' or board[z][a] == ' k ' or board[z][a] == ' K ' or board[z][
                                                             a] == ' P ' and ypl == 1 or board[z][
                                                             a] == ' p ' and ypl == -1) or lub == True):
                k = [z, a]
            z = xm
    while z != xm and a != ym:
        z += xpl
        a += ypl
        if board[z][a] != ' . ':
            if board[z][a].isupper() != white_move and (lub == True or white_move == True and (
                    board[z][a] == ' Q ' or board[z][a] == ' B ') or white_move == False and (
                                                                board[z][a] == ' q ' or board[z][a] == ' b ')):
                k = [z, a]
            break
    if lub == False:
        if k == []:
            return (True)
        else:
            return (False)
    else:
        return (k)


def straight_attack(x, y, white_move, k=8, z=1, lub=False):
    a = [[], []]
    if x + z != k:
        if board[x + z][y] != ' . ' and board[x + z][y].isupper() != white_move and (
                board[x + z][y] == ' k ' or board[x + z][y] == ' K '):
            a[0] = [x + z, y]
        else:
            for i in range(x + z, k, z):
                if board[i][y] != ' . ':
                    if board[i][y].isupper() != white_move and (lub == True or white_move == True and (
                            board[i][y] == ' Q ' or board[i][y] == ' R ') or white_move == False and (
                                                                        board[i][y] == ' q ' or board[i][y] == ' r ')):
                        a[0] = [i, y]
                    break

    if a[0] != [] and lub == False:
        return (False)
    if y + z != k:
        if board[x][y + z] != ' . ' and board[x][y + z].isupper() != white_move and (
                board[x][y + z] == ' k ' or board[x][y + z] == ' K '):
            a[1] = [x, y + z]
        else:
            for i in range(y + z, k, z):
                if board[x][i] != ' . ':
                    if board[x][i].isupper() != white_move and (lub == True or white_move == True and (
                            board[x][i] == ' Q ' or board[x][i] == ' R ') or white_move == False and (
                                                                        board[x][i] == ' q ' or board[x][i] == ' r ')):
                        a[1] = [x, i]
                    break

    if lub == False:
        if a[1] != []:
            return (False)
        else:
            return (True)
    return (a)


def horse_attack(x, y, white_move, lub=False):
    a = []

    for i in range(8):
        for k in range(8):

            if (white_move == False and board[i][k] == ' N ' or white_move == True and board[i][k] == ' n ') and (
                    (abs(i - x) == 1 and abs(k - y) == 2) or (abs(i - x) == 2 and abs(k - y) == 1)):
                if lub == True:
                    a.append([i, k])
                else:
                    return (False)

    if lub == False:
        return (True)
    else:
        return (a)


def straight_check(xp, xv, yp, yv):
    if yv == yp:
        if xp < xv:
            xp += 1
            for i in range(xp, xv):
                if board[i][yp] != ' . ':
                    return (False)
        else:
            xv += 1
            for i in range(xv, xp):
                if board[i][yp] != ' . ':
                    return (False)
    else:
        if yp < yv:
            yp += 1
            for i in range(yp, yv):
                if board[xp][i] != ' . ':
                    return (False)
        else:
            yv += 1
            for i in range(yv, yp):
                if board[xp][i] != ' . ':
                    return (False)

    return (True)


def diagonal_check(xp, xv, yp, yv):
    if xp > xv:
        el = -1
    else:
        el = 1
    if yp > yv:
        elv = -1
    else:
        elv = 1
    yp += elv
    xp += el
    while yp != yv:
        if board[xp][yp] != ' . ':
            return (False)
        yp += elv
        xp += el
    return (True)


def board_show():
    print(
        '\nP - Пешка; K - Король; Q - Королева; R - Ладья; N - Конь; B - Слон;\n    a  b  c  d  e  f  g  h\n  ┌────────────────────────┐')
    for i in range(7, -1, -1):
        vuv = str(i + 1) + ' │'
        for k in range(8):
            vuv += board[k][i]
        vuv += '│ ' + str(i + 1)
        print(vuv)
    print('  └────────────────────────┘\n    a  b  c  d  e  f  g  h\n')


def move_delay(xpb, ypb, xvb, yvb, white_move, time=''):
    def attack_check(x, y, white_move):

        if diagonal_attack(x, y, 7, 7, 1, 1, white_move) == False:
            return (False)
        if diagonal_attack(x, y, 7, 0, 1, -1, white_move) == False:
            return (False)
        if diagonal_attack(x, y, 0, 7, -1, 1, white_move) == False:
            return (False)
        if diagonal_attack(x, y, 0, 0, -1, -1, white_move) == False:
            return (False)
        if straight_attack(x, y, white_move, k=-1, z=-1) == False:
            return (False)
        if straight_attack(x, y, white_move) == False:
            return (False)
        if horse_attack(x, y, white_move) == False:
            return (False)
        return (True)

    def move(xp, yp, xv, yv, xpb, ypb, xvb, yvb):
        moves_count.append([xpb, ypb, xvb, yvb, board[xv][yv]])
        el = 1
        if board[xv][yv] == ' k ' or board[xv][yv] == ' K ':
            el = 2
        board[xv][yv] = board[xp][yp]
        board[xp][yp] = ' . '
        return (el)

    if ypb.isdigit() == True and ypb != '0' and ypb != '9' and yvb.isdigit() == True and yvb != '0' and yvb != '9' and (
            xvb in board_bv) and (xpb in board_bv):
        yp = int(ypb) - 1
        yv = int(yvb) - 1
        xp = board_bv[xpb]
        xv = board_bv[xvb]
        if board[xp][yp] == ' . ':
            print('Вы трогаете воздух!')
        elif board[xp][yp].isupper() != white_move:
            print('Нельзя двигать чужую фигуру!')
        elif board[xv][yv] != ' . ' and board[xv][yv].isupper() == white_move and (
                board[xv][yv] != ' r ' and board[xp][yp] != ' k ' and board[xv][yv] != ' R ' and board[xp][
            yp] != ' K '):
            print('Нельзя есть свою фигуру')
        elif yp == yv and xv == xp:
            print('Так и замерзнуть можно, не стойте на месте!')
        else:
            el = board[xp][yp].lower()

            if el == ' p ' and ((xp == xv and board[xv][yv] == ' . ' and (
                    yv - yp == 1 and white_move == True or yp - yv == 1 and white_move == False) or (
                                         yp == 1 and white_move == True and yv == 3 or yp == 6 and white_move == False and yv == 4)) or (
                                        board[xv][yv] != ' . ' and abs(xv - xp) == 1 and (
                                        yv - yp == 1 and white_move == True or yp - yv == 1 and white_move == False))):
                if yv == 0 or yv == 7:
                    if time == '':
                        while white_move == True and el != ' Q ' and el != ' R ' and el != ' N ' and el != ' B ' or white_move == False and el != ' q ' and el != ' r ' and el != ' n ' and el != ' b ':
                            el = ' ' + (input('Пешка дошла до базы врага. Кем ей стать (регистр важен): ')) + ' '
                            if white_move == True and el != ' Q ' and el != ' R ' and el != ' N ' and el != ' B ' or white_move == False and el != ' q ' and el != 'r' and el != ' n ' and el != ' b ':
                                print('Пешка не может стать выбранной фигурой.')
                    else:
                        el = ' ' + time + ' '
                    board[xv][yv] += el
                    board[xp][yp] = el
                return (move(xp, yp, xv, yv, xpb, ypb, xvb, yvb))
            elif (el == ' r ' or el == ' q ') and ((xp == xv or yp == yv) and straight_check(xp, xv, yp, yv) == True):
                if el == ' r ':
                    if xp == 0 and yp == 0:
                        castling[1] = False
                    elif xp == 7 and yp == 0:
                        castling[2] = False
                    elif xp == 0 and yp == 7:
                        castling[4] = False
                    elif xp == 7 and yp == 7:
                        castling[5] = False
                return (move(xp, yp, xv, yv, xpb, ypb, xvb, yvb))
            elif el == ' n ' and (
                    abs(xv - xp) == 1 and abs(yp - yv) == 2 or abs(xv - xp) == 2 and abs(yp - yv) == 1) or (
                    el == ' b ' or el == ' q ') and (
                    abs(xv - xp) == abs(yp - yv) and diagonal_check(xp, xv, yp, yv) == True):
                return (move(xp, yp, xv, yv, xpb, ypb, xvb, yvb))
            elif el == ' k ' and ((abs(xv - xp) == 1 or abs(yp - yv) == 1) and (abs(xv - xp) < 2 and abs(yp - yv) < 2)):
                if white_move == True:
                    castling[0] = False
                else:
                    castling[3] = False
                return (move(xp, yp, xv, yv, xpb, ypb, xvb, yvb))
            if el == ' k ' and (
                    white_move == True and board[xv][yv] == ' R ' or white_move == False and board[xv][yv] == ' r '):
                if white_move == True and castling[0] == True and yv == 0 and straight_check(xp, xv, yp,
                                                                                             yv) == True and attack_check(
                        xp, yp, white_move) == True and (
                        xv == 0 and castling[1] == True and attack_check(2, yp, white_move) == True and attack_check(3,
                                                                                                                     yp,
                                                                                                                     white_move) == True or xv == 7 and
                        castling[2] == True and attack_check(5, yp, white_move) == True and attack_check(6, yp,
                                                                                                         white_move) == True):
                    moves_count.append([xpb, ypb, xvb, yvb, ' o o'])
                    castling[0] = False
                elif white_move == False and castling[3] == True and yv == 7 and straight_check(xp, xv, yp,
                                                                                                yv) == True and attack_check(
                        xp, yp, white_move) == True and (
                        xv == 0 and castling[4] == True and attack_check(2, yp, white_move) == True and attack_check(3,
                                                                                                                     yp,
                                                                                                                     white_move) == True or xv == 7 and
                        castling[5] == True and attack_check(5, yp, white_move) == True and attack_check(6, yp,
                                                                                                         white_move) == True):
                    moves_count.append([xpb, ypb, xvb, yvb, ' o o'])
                    castling[3] = False
                else:
                    print('Рокировка невозможна!')
                    return (0)
                if xv == 0:
                    board[2][yp] = board[xp][yp]
                    board[3][yp] = board[xv][yp]
                else:
                    board[6][yp] = board[xp][yp]
                    board[5][yp] = board[xv][yp]
                board[xp][yp] = ' . '
                board[xv][yv] = ' . '
                return (1)
            elif el == ' p ' and board[xv][yv] == ' . ' and moves_count[moves_count[0]][3] == str(yp + 1) and ((
                                                                                                                       yp == 4 and yv == 5 and white_move == True and
                                                                                                                       moves_count[
                                                                                                                           moves_count[
                                                                                                                               0]][
                                                                                                                           1] == '7' and
                                                                                                                       board[
                                                                                                                           board_bv[
                                                                                                                               moves_count[
                                                                                                                                   moves_count[
                                                                                                                                       0]][
                                                                                                                                   2]]][
                                                                                                                           4] == ' p ') or (
                                                                                                                       yp == 3 and yv == 2 and white_move == False and
                                                                                                                       moves_count[
                                                                                                                           moves_count[
                                                                                                                               0]][
                                                                                                                           1] == '2' and
                                                                                                                       board[
                                                                                                                           board_bv[
                                                                                                                               moves_count[
                                                                                                                                   moves_count[
                                                                                                                                       0]][
                                                                                                                                   2]]][
                                                                                                                           3] == ' P ')) and \
                    moves_count[moves_count[0]][2] == xvb and abs(xv - xp) == 1:
                if white_move == True:
                    board[xv][yv] += 'p'
                    board[board_bv[moves_count[moves_count[0]][2]]][4] = ' . '
                else:
                    board[xv][yv] += 'P'
                    board[board_bv[moves_count[moves_count[0]][2]]][3] = ' . '
                return (move(xp, yp, xv, yv, xpb, ypb, xvb, yvb))
            else:
                print('Так ходить нельзя!')
    else:
        print('Некорректный ввод координат.')
    return (0)


def figures_replace(end_place, start_place):
    end_place += start_place
    if moves_count[0] >= end_place and end_place >= 0:
        if end_place < start_place:
            for i in range(start_place, end_place, -1):
                if len(moves_count[i][4]) == 3:
                    board[board_bv[moves_count[i][0]]][int(moves_count[i][1]) - 1] = board[board_bv[moves_count[i][2]]][
                        int(moves_count[i][3]) - 1]
                    board[board_bv[moves_count[i][2]]][int(moves_count[i][3]) - 1] = moves_count[i][4]
                elif moves_count[i][4] == ' o o':
                    if i % 2 == 1:
                        board[board_bv[moves_count[i][0]]][0] = ' K '
                        board[board_bv[moves_count[i][2]]][0] = ' R '
                        castling[0] = True
                        if moves_count[i][2] == '0':
                            castling[1] = True
                        else:
                            castling[2] = True
                    else:
                        board[board_bv[moves_count[i][0]]][7] = ' k '
                        board[board_bv[moves_count[i][2]]][7] = ' r '
                        castling[3] = True
                        if moves_count[i][2] == '0':
                            castling[4] = True
                        else:
                            castling[5] = True
                    if moves_count[i][2] == 0:
                        board[2][int(moves_count[i][1]) - 1] = ' . '
                        board[3][int(moves_count[i][1]) - 1] = ' . '
                    else:
                        board[6][int(moves_count[i][1]) - 1] = ' . '
                        board[5][int(moves_count[i][1]) - 1] = ' . '
                elif moves_count[i][4][3:] == 'p' or moves_count[i][4][3:] == 'P':
                    board[board_bv[moves_count[i - 1][2]]][int(moves_count[i - 1][3]) - 1] = moves_count[i][4][3:]
                    board[board_bv[moves_count[i][0]]][int(moves_count[i][1]) - 1] = board[board_bv[moves_count[i][2]]][
                        int(moves_count[i][3]) - 1]
                    board[board_bv[moves_count[i][2]]][int(moves_count[i][3]) - 1] = ' . '
                else:
                    if start_place % 2 == 1:
                        board[board_bv[moves_count[i][0]]][int(moves_count[i][1]) - 1] = ' P '
                    else:
                        board[board_bv[moves_count[i][0]]][int(moves_count[i][1]) - 1] = ' p '
                    board[board_bv[moves_count[i][2]]][int(moves_count[i][3]) - 1] = moves_count[i][4][:3]
        else:
            for i in range(start_place + 1, end_place + 1, 1):
                if len(moves_count[i][4]) == 4 and moves_count[i][4][3] != 'p' and moves_count[i][4][3] != 'P':
                    time = moves_count[i][4][3]
                else:
                    time = ''
                if i % 2 == 1:
                    move_delay(moves_count[i][0], moves_count[i][1], moves_count[i][2], moves_count[i][3], True,
                               time=time)
                else:
                    move_delay(moves_count[i][0], moves_count[i][1], moves_count[i][2], moves_count[i][3], False,
                               time=time)
                del (moves_count[moves_count[0] + 1])
    else:
        print('Вы не можете туда пойти!')


board_bv = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
rus_tr = {'Ф': 'Q', 'Л': 'R', 'К': 'N', 'С': 'B'}
obr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

command = ''

while command != 'Конец':

    command = input('Введите "Играть" для начала игры, "Конец" для окончания: ')
    board = [[' R ', ' P ', ' . ', ' . ', ' . ', ' . ', ' p ', ' r '],
             [' N ', ' P ', ' . ', ' . ', ' . ', ' . ', ' p ', ' n '],
             [' B ', ' P ', ' . ', ' . ', ' . ', ' . ', ' p ', ' b '],
             [' Q ', ' P ', ' . ', ' . ', ' . ', ' . ', ' p ', ' q '],
             [' K ', ' P ', ' . ', ' . ', ' . ', ' . ', ' p ', ' k '],
             [' B ', ' P ', ' . ', ' . ', ' . ', ' . ', ' p ', ' b '],
             [' N ', ' P ', ' . ', ' . ', ' . ', ' . ', ' p ', ' n '],
             [' R ', ' P ', ' . ', ' . ', ' . ', ' . ', ' p ', ' r ']]

    castling = [True, True, True, True, True, True]
    white_move = True
    moves_count = [0]
    move_number = -1
    repeat = True

    if command == 'Играть':
        while command != 'Выход':
            if repeat == True:
                board_show()
                if white_move == True:
                    print('Ход:', moves_count[0] + 1, 'Ходит белый.')
                else:
                    print('Ход:', moves_count[0] + 1, 'Ходит чёрный.')
                print(
                    'Введите координаты хода через пробел (латинские буквы поля откуда выполняется ход и куда. Для рокировки переместите короля на место ладьи), Выход')
            else:
                if move_number % 2 == 0:
                    print('Всего ходов: ' + str(moves_count[0] + 1) + ' Cейчас ' + str(
                        move_number + 1) + ' ход. Белые\nВведите команду: Вперёд (кол-во ходов), Продолжить, Выход')
                else:
                    print('Всего ходов: ' + str(moves_count[0] + 1) + ' Cейчас ' + str(
                        move_number + 1) + ' ход. Чёрные\nВведите команду: Вперёд (кол-во ходов), Продолжить, Выход')

            command = input('Ввод: ')
            if len(command) == 5 and command[2] == ' ' and repeat == True:
                command = move_delay(command[0], command[1], command[3], command[4], white_move)
                if command == 1:
                    if white_move == True:
                        white_move = False
                    else:
                        white_move = True
                    moves_count[0] += 1
                elif command == 2:
                    print('Король умер, да здравствует король!')
                    if white_move == True:
                        print('Белые победили\n')
                    else:
                        print('Чёрные победили\n')
                    command = 'Выход'
            elif command != 'Выход':
                print('Команда не распознана')