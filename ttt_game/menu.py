import pygame
from button_object import button


# класс, который наследует поведение класса button, предназначен для описания поведения кнопки play

class play_button(button):
    """
    screen: экран, на котором будет отрисована кнопка

    image: картинка кнопки

    rect: создание области из картинки

    rect.x: расположение кнопки по оси x

    rect.y: расположение кнопки по оси y

    rect.width: ширина области в пикселях

    rect.height: высота области в пикселях
    """

    def __init__(self, screen):
        super().__init__(screen)
        self.image = pygame.image.load('pictures/play.png')
        self.rect.x = 475
        self.rect.y = 200
        self.rect.width = 250
        self.rect.height = 100

    # описание наследуемых методов было приведено в файле button_object.py

    def button_show(self):
        super().button_show()

    def is_clicked(self, event):
        super().is_clicked(event)

    def return_to_false(self):
        super().return_to_false()


# класс, который наследует поведение класса button, предназначен для описания поведения кнопки settings

class settings_button(button):
    """
    screen: экран, на котором будет отрисована кнопка

    image: картинка кнопки

    rect: создание области из картинки

    rect.x: расположение кнопки по оси x

    rect.y: расположение кнопки по оси y

    rect.width: ширина области в пикселях

    rect.height: высота области в пикселях
    """

    def __init__(self, screen):
        super().__init__(screen)
        self.image = pygame.image.load('pictures/settings.png')
        self.rect.x = 475
        self.rect.y = 330
        self.rect.width = 250
        self.rect.height = 100

    # описание наследуемых методов было приведено в файле button_object.py

    def button_show(self):
        super().button_show()

    def is_clicked(self, event):
        super().is_clicked(event)

    def return_to_false(self):
        super().return_to_false()


# класс, который наследует поведение класса button, предназначен для описания поведения кнопки exit

class exit_button(button):
    """
    screen: экран, на котором будет отрисована кнопка

    image: картинка кнопки

    rect: создание области из картинки

    rect.x: расположение кнопки по оси x

    rect.y: расположение кнопки по оси y

    rect.width: ширина области в пикселях

    rect.height: высота области в пикселях
    """

    def __init__(self, screen):
        super().__init__(screen)
        self.image = pygame.image.load('pictures/exit.png')
        self.rect.x = 475
        self.rect.y = 460
        self.rect.width = 250
        self.rect.height = 100

    # описание наследуемых методов было приведено в файле button_object.py

    def button_show(self):
        super().button_show()

    def is_clicked(self, event):
        super().is_clicked(event)

    def return_to_false(self):
        super().return_to_false()


"""
Функция получает на вход параметр 'a' и экран, на котором будут созданы кнопки
Функция предназначена для создания объектов кнопок если мы находимся в меню
В противном случае мы создаем новую област и следующие объекты будут появляться на ней
"""


def menu_show(a, screen):
    if a == 0:
        play = play_button(screen)
        play.button_show()

        settings = settings_button(screen)
        settings.button_show()

        exit = exit_button(screen)
        exit.button_show()
    elif a == 1:
        return pygame.Surface((1200, 800))

    return play, settings, exit
