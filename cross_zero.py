def check_coord(user_str):
    if len(user_str) != 3 or ' ' not in user_str:
        print("Неправильный ввод, попробуйте ещё раз")
        return None
    users_coord = user_str.split()
    if not all(map(str.isdigit, users_coord)):
        print("Координаты должны быть числами")
        return None
    a, b = map(int, users_coord)
    if a < 0 or a > 2 or b < 0 or b > 2:
        print('Координаты должны быть от 0 до 2')
        return None
    if lst[a+1][b+1] != '-':
        print("Эта клетка занята!")
        return None
    else:
        return a, b


def check_matrix(matrix):
    res = []
    for row in matrix:
        res.extend([all(map(lambda d: d == 'X', row)), all(map(lambda d: d == 'O', row))])
    return any(res)


def check_diagonal(matrix):
    res = []
    res1 = []
    for i in range(3):
        res.append(matrix[i][i])
        res1.append(matrix[2-i][i])
    return any([all(map(lambda d: d == 'X', res)), all(map(lambda d: d == 'O', res)),
                all(map(lambda d: d == 'X', res1)), all(map(lambda d: d == 'O', res1))])


def show_area(user_list):
    for i in user_list:
        print(*i)


def check_winner(user_list):
    check_list = list(zip(*user_list[1:]))[1:]
    check_list_2 = list(zip(*check_list))
    return check_matrix(check_list) or check_matrix(check_list_2) or check_diagonal(check_list)


lst = [
    [' ', 0, 1, 2],
    [0, '-', '-', '-'],
    [1, '-', '-', '-'],
    [2, '-', '-', '-'],
]
l_0 = sum(lst, [])
count = 0
while '-' in l_0:
    # for i in lst:
    #     print(*i)
    show_area(lst)
    print('Ход нолика!' if count % 2 else 'Ход крестика!')
    user_coord = input("Введите через пробел координаты по горизонтали и по вертикали:")
    if not check_coord(user_coord):
        continue
    else:
        x, y = check_coord(user_coord)
    lst[x+1][y+1] = 'O' if count % 2 else 'X'
    l_0 = sum(lst, [])
    if check_winner(lst):
        print("Вы победили!!!")
        # for i in lst:
        #     print(*i)
        show_area(lst)
        print("Игра окончена!!!")
        break
    count += 1
else:
    print('Ничья!')
    show_area(lst)
    print("Игра окончена!!!")
print('-'*30)






