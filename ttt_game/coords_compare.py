"""
Функция, предназначенная для поиска позиции в матрице игрового поля
В которую необходимо поместить 'ход' игрока
"""

def check_position(x, y):
    # автору было лень писать нормальную реализацию
    row = -1
    col = -1
    x_variants = [[256, 463], [497, 702], [730, 947]]
    if 52 <= y <= 266:
        row = 0
    elif 295 <= y <= 501:
        row = 1
    else:
        row = 2

    for i, j in enumerate(x_variants):
        if j[0] <= x <= j[1]:
            col = i

    return row, col