

def sole_survivor0(n: int, k: int) -> int:
    '''
    Функция воплощает алгоритм поиска "единственного выжившего" рекурсией.

    Подаваемые аргументы: число человек в кругу (int n) и счёт выбывающих (int k).
    Возвращаемое значение: номер человека, оставшегося в кругу последним (int).
    '''

    if n == 1:
        return 1
    elif n > 1:
        return (sole_survivor0(n - 1, k) + k - 1) % n + 1  # отмечаем закономерность


def sole_survivor1(n: int, k: int) -> int:
    '''
    Функция воплощает алгоритм поиска "единственного выжившего" циклом.

    Подаваемые аргументы: число человек в кругу (int n) и счёт выбывающих (int k).
    Возвращаемое значение: номер человека, оставшегося в кругу последним (int survivor).
    '''

    element = 0
    
    for i in range(1, n + 1):
        element = (element + k) % i

    survivor = last + 1
    
    return survivor


def sole_survivor2(n: int, k: int) -> int:
    '''
    Функция воплощает алгоритм поиска "единственного выжившего" полным перебором

    Подаваемые аргументы: число человек в кругу (int n) и счёт выбывающих (int k).
    Возвращаемое значение: номер человека, оставшегося в кругу последним (int survivor).
    '''

    circle = [i for i in range(1, n + 1)]  # круг, где человеку отвечает его порядковый номер

    i = 0  # независимая переменная, ведущая счёт на выбывание
    j = 1
    length = n  # нынешняя длина массива
    
    while length > 1:

        if (i + j) % k == 0:
            circle.pop(i % length)
            length = length - 1
            j = j + 1
        else:
            i = i + 1

    survivor = circle[0]


    return survivor


