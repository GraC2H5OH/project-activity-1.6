import sys

import pygame
from menu_functions.settings_function import settings_section, back_button
from menu_functions.exit_function import exit_func
from menu import menu_show
from game_process import *
from idle_kill import kill

pygame.init()
# создаем окно с размерами 1200x800
screen = pygame.display.set_mode((1200, 800))

# задаем название и иконку
pygame.display.set_caption('tic-tac-toe')
pygame.display.set_icon(pygame.image.load('pictures/icon.bmp'))

# указываем количество кадров в секунду
fps = 60

# Функция, отвечающая за запуск игры
def run():

    """
    clock: объект для помощи отслеживания времени
    Но в нашем случае для фиксирования значения fps

    menu_parameter: если 0, возвращает объекты кнопок меню
    Если 1, Вовзращает новую область для отрисовки

    grd: объект игрового поля

    f: переменная, для работы приложения

    Если True, приложение работает

    Если False, приложение закрывается если было запущено

    Или не открывается если не было запущено

    play: объект кнопки для игры

    exit: объект кнопки для выхода из игры

    settings: объект кнопки для вывода информации об игре и команде
    """

    clock = pygame.time.Clock()
    global screen
    menu_parameter = 0
    grd = grid(screen)
    kl = 0
    f = True
    while f:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = False
        try:
            play, settings, exit = menu_show(menu_parameter, screen)
        except TypeError:
            screen = menu_show(menu_parameter, screen)

        """
        Если мы нажали play, то весь экран очищается и выводится игровое поле
        Все время мы отслеживаем, нажал ли игрок по игровому полю
        И все время мы отслеживаем есть ли на поле выйгрышная комбинация
        Если есть/ничья, то мы выводим об этом сообщение и закрываем игру
        """
        play.is_clicked(event)
        if play.is_pressed:
            menu_parameter = 1
            screen.fill((0, 0, 0))
            grd.grid_show()
            grd.click_where(event)
            grd.draw_figures()
            grd.win_check()
            if grd.is_finished:
                kill()
                sys.exit()


        """
        Если мы нажали settings, то мы очищаем весь экран и выводим информацию на экран
        Также, мы проверяем были ли нажата кнопка назад, которая приводит к закрытию игры
        """

        settings.is_clicked(event)
        if settings.is_pressed:
            menu_parameter = 1
            settings_section(screen).text()
            back_b = back_button(screen)
            back_b.button_show()
            back_b.is_clicked(event)
            if back_b.is_pressed:
                kill()
                sys.exit()

        """
        Если была нажата кнопка exit, то игра закрывается
        """

        exit.is_clicked(event)
        if exit.is_pressed and (menu_parameter == 0):
            exit_func()
            kill()
        pygame.display.flip()
        clock.tick(fps)
