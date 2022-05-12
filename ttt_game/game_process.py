import pygame
import ctypes
from coords_compare import check_position

# Класс, отвечающий за все, что происходит с игровым полем

class grid:

    def __init__(self, screen):

        """
        screen: экран, на котором будет отрисовано поле для игры

        imgae: поле которое будет отрисовано

        rect: создание области из картинки

        rect.x: расположение поля по оси x

        rect.y: расположение поля по оси y

        rect.width: ширина поля в пикселях

        rect.height: высота поля в пикселях

        if_clicked: была ли нажата кнопка в пределах поверхности поля
        P.S (см. описание к функции click_where())

        is_finished: завершилась ли игра

        row: строка в матрице, которая представляет поле игры
        P.S (см. описание ttt_matrix и функции win_check())

        col: столбец в матрице, которая представляет поле игры
        P.S (см. описание ttt_matrix и функции win_check())

        ttt.matrix: матрица, представляющая поле игры.Изначально выглядит так: [[-1, -1, -1],
                                                                                [-1, -1, -1],
                                                                                [-1, -1, -1]]
        В зависимости от изменений на поле (игрок сделал ход) матрица меняется.
        Если игрок (см. описание player) 'o' поставил нолик в центр, то матрица будет выглядеть так:
        [[-1, -1, -1],
         [-1, o, -1],
         [-1, -1, -1]]

         player: либо 'o' либо 'x'. Первый ход всегда делает крестик.
         Каждый ход значение player меняется, чтобы походил другой игрок

         cross_image: картинка крестика

         circle_image: картинка нолика

         x: расположение курсора мышки на оси x
         P.S (см. описании функции click_where())

         x: расположение курсора мышки на оси y
         P.S (см. описании функции click_where())
        """

        self.screen = screen
        self.image = pygame.image.load('pictures/grid.png')
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 50
        self.rect.width = 700
        self.rect.height = 700
        self.is_clicked = False
        self.is_finished = False
        self.row = -1
        self.col = -1
        self.center_coordsx = [250, 502, 747]
        self.center_coordsy = [66, 295, 535]
        self.ttt_matrix = [[-1 for j in range(3)] for i in range(3)]
        self.player = 'cross'
        self.cross_image = pygame.image.load('pictures/cross.png')
        self.rect_cross = self.cross_image.get_rect()
        self.circle_image = pygame.image.load('pictures/circle.png')
        self.rect_circle = self.circle_image.get_rect()
        self.x = 0
        self.y = 0

    """
    event: событие, которое произошло (клик мышкой, перемещений курсора и т.д.)
    Функция, отвечающая за клики мышки по игровому полю.
    Каждый вызов функции она проверяет кликнул ли пользователь
    Если да, то получаем координаты мышки и проверяем, попали ли они
    В игровое поле. Если да, то запоминаем, в какую клетку мы попали
    И меняем значение переменной, отвечающей за клики по полю
    """

    def click_where(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.x, self.y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed():
                if self.rect.collidepoint(self.x, self.y):
                    self.row, self.col = check_position(self.x, self.y)
                    self.is_clicked = True

    """
    Отрисовываем игровое поле
    """

    def grid_show(self):
        self.screen.blit(self.image, self.rect)

    """
    Функция, отвечающая за рисование фигур в тех местах, в которых нажал игрок на поле
    Сначала мы 'делаем ход' в нашей матрице игрового поля, а потом
    Проверяем были ли клик по полю и в зависимости от игрока рисуем соответствующую
    Фигуру. После этого возвращаем переменную, отвечающую за клики по полю в исходное состояние
    """

    def draw_figures(self):
        if (self.ttt_matrix[self.row][self.col] == -1) and self.is_clicked:

            if self.player == 'cross':
                self.ttt_matrix[self.row][self.col] = 'x'
                self.player = 'circle'
                self.rect_cross.x = self.center_coordsx[self.col]
                self.rect_cross.y = self.center_coordsy[self.row]
                self.rect_cross.width = 200
                self.rect_cross.height = 200
                self.screen.blit(self.cross_image, self.rect_cross)
                self.is_clicked = False

            else:
                self.ttt_matrix[self.row][self.col] = 'o'
                self.player = 'cross'
                self.rect_circle.x = self.center_coordsx[self.col]
                self.rect_circle.y = self.center_coordsy[self.row]
                self.rect_circle.width = 200
                self.rect_circle.height = 200
                # self.screen = pygame.Surface((1200, 800))
                self.screen.blit(self.circle_image, self.rect_circle)
                self.is_clicked = False

    """
    Функция, для проверки конца игры (была выстроена победная комбинация/ничья)
    Если все элементы на одной из выйгрышных комбинаций совпали/закончились клетки, то мы выводим окно
    С информацией о том, кто выйграл. И меняем значение переменной, отвечающей за конец игры
    """

    def win_check(self):
        # эту функцию автору было лень оптимизировать

        # проверка горизонтальных линий
        if self.ttt_matrix[0][0] == self.ttt_matrix[0][1] == self.ttt_matrix[0][2] and (
                self.ttt_matrix[0][0] != -1) and (not self.is_finished):
            self.draw_figures()
            pygame.display.flip()
            ctypes.windll.user32.MessageBoxW(0, "победил - {}".format(self.ttt_matrix[0][0]), "Конец игры", 1)
            self.is_finished = True
        if self.ttt_matrix[1][0] == self.ttt_matrix[1][1] == self.ttt_matrix[1][2] and (
                self.ttt_matrix[1][0] != -1) and (not self.is_finished):
            self.draw_figures()
            pygame.display.flip()
            ctypes.windll.user32.MessageBoxW(0, "победил - {}".format(self.ttt_matrix[1][0]), "Конец игры", 1)
            self.is_finished = True
        if self.ttt_matrix[2][0] == self.ttt_matrix[2][1] == self.ttt_matrix[2][2] and (
                self.ttt_matrix[2][0] != -1) and (not self.is_finished):
            self.draw_figures()
            pygame.display.flip()
            ctypes.windll.user32.MessageBoxW(0, "победил - {}".format(self.ttt_matrix[2][0]), "Конец игры", 1)
            self.is_finished = True

        # проверка вертикальных линий
        if self.ttt_matrix[0][0] == self.ttt_matrix[1][0] == self.ttt_matrix[2][0] and (
                self.ttt_matrix[0][0] != -1) and (not self.is_finished):
            self.draw_figures()
            pygame.display.flip()
            ctypes.windll.user32.MessageBoxW(0, "победил - {}".format(self.ttt_matrix[0][0]), "Конец игры", 1)
            self.is_finished = True
        if self.ttt_matrix[0][1] == self.ttt_matrix[1][1] == self.ttt_matrix[2][1] and (
                self.ttt_matrix[0][1] != -1) and (not self.is_finished):
            self.draw_figures()
            pygame.display.flip()
            ctypes.windll.user32.MessageBoxW(0, "победил - {}".format(self.ttt_matrix[0][1]), "Конец игры", 1)
            self.is_finished = True
        if self.ttt_matrix[0][2] == self.ttt_matrix[1][2] == self.ttt_matrix[2][2] and (
                self.ttt_matrix[0][2] != -1) and (not self.is_finished):
            self.draw_figures()
            pygame.display.flip()
            ctypes.windll.user32.MessageBoxW(0, "победил - {}".format(self.ttt_matrix[0][2]), "Конец игры", 1)
            self.is_finished = True

        # проверка главной диагонали
        if self.ttt_matrix[0][0] == self.ttt_matrix[1][1] == self.ttt_matrix[2][2] and (
                self.ttt_matrix[0][0] != -1) and (not self.is_finished):
            self.draw_figures()
            pygame.display.flip()
            ctypes.windll.user32.MessageBoxW(0, "победил - {}".format(self.ttt_matrix[0][0]), "Конец игры", 1)
            self.is_finished = True
        # проверка дополнительной диагонали
        if self.ttt_matrix[0][2] == self.ttt_matrix[1][1] == self.ttt_matrix[2][0] and (
                self.ttt_matrix[0][2] != -1) and (not self.is_finished):
            self.draw_figures()
            pygame.display.flip()
            ctypes.windll.user32.MessageBoxW(0, "победил - {}".format(self.ttt_matrix[0][2]), "Конец игры", 1)
            self.is_finished = True
        # проверка на ничью
        if (-1 not in self.ttt_matrix[0]) and (-1 not in self.ttt_matrix[1]) and (-1 not in self.ttt_matrix[2]) and (
                not self.is_finished):
            self.draw_figures()
            pygame.display.flip()
            ctypes.windll.user32.MessageBoxW(0, "победила дружба", "Конец игры", 1)
            self.is_finished = True

