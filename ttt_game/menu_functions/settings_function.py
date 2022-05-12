import pygame

# Описание цветов, которые мы будем использовать для отрисовки надписей

teamlead_colour = (214, 22, 22)
dev_colour = (42, 214, 22)
QA_colour = (22, 93, 214)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.init()


# Класс, отвечающий за информацию об игре и команде

class settings_section:
    """
    screen: экран, на котором будет отрисована вся информация

    version: версия игры

    dev: ник разработчика на гитхабе и его имя

    teamlead: ник тимлида на гитхабе и его емя

    QA: ник тестировщика на гитхабе и его имя

    f: используемый шрифт для отрисовки
    """

    def __init__(self, screen):
        self.screen = screen
        self.version = 1.0
        self.dev = 'GraC2H5OH(Nikita)'
        self.teamlead = 'Kateeeee2222(Ekaterina)'
        self.QA = 'kaba404ek(Vitaliy)'
        self.f = pygame.font.Font('fonts/Teletactile.ttf', 34)

    """
    Функция, отвечающая за отрисовку экрана с информацией о команде и версии игры
    В начале мы заливаем экран черным, а потом выводим весь текст
    """

    def text(self):
        self.screen.fill(BLACK)

        teamlead_text = self.f.render('team lead', 1, WHITE)
        teamled_text_position = teamlead_text.get_rect(center=(600, 100))
        self.screen.blit(teamlead_text, teamled_text_position)
        teamlead_nickname = self.f.render('{}'.format(self.teamlead), 1, teamlead_colour)
        teamlead_nickname_position = teamlead_nickname.get_rect(center=(600, 200))
        self.screen.blit(teamlead_nickname, teamlead_nickname_position)

        version_text = self.f.render('version {}'.format(self.version), 1, WHITE)
        version_text_position = version_text.get_rect(center=(600, 700))
        self.screen.blit(version_text, version_text_position)

        main_dev_text = self.f.render('main developer', 1, WHITE)
        main_dev_text_position = main_dev_text.get_rect(center=(600, 300))
        self.screen.blit(main_dev_text, main_dev_text_position)
        main_dev_nickname = self.f.render('{}'.format(self.dev), 1, dev_colour)
        main_dev_nickname_position = main_dev_nickname.get_rect(center=(600, 400))
        self.screen.blit(main_dev_nickname, main_dev_nickname_position)

        QA_text = self.f.render('QA', 1, WHITE)
        QA_text_position = QA_text.get_rect(center=(600, 500))
        self.screen.blit(QA_text, QA_text_position)
        QA_nickname = self.f.render('{}'.format(self.QA), 1, QA_colour)
        QA_nickname_position = QA_nickname.get_rect(center=(600, 600))
        self.screen.blit(QA_nickname, QA_nickname_position)


# Класс, отвечающий за функциональность кнопки назад в настройках

class back_button:

    """
    screen: экран, на котором будет отрисована кнопка

    image: картинка кнопки

    rect: создание области из картинки

    rect.x: расположение кнопки по оси x

    rect.y: расположение кнопки по оси y

    rect.width: ширина области в пикселях

    rect.height: высота области в пикселях

    is_pressed: была ли нажата кнопка
    """

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('pictures/back.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1150
        self.rect.y = 0
        self.rect.width = 50
        self.rect.height = 50
        self.is_pressed = False

    """
    Функция, отвечающая за вывод кнопки на экран
    """

    def button_show(self):
        self.screen.blit(self.image, self.rect)

    """
    event: событие, которое произошло (клик мышкой, перемещений курсора и т.д.)
    Функция, отвечающая за клики мышки по кнопке назад.
    Каждый вызов функции она проверяет кликнул ли пользователь
    Если да, то получаем координаты мышки и проверяем, попали ли они
    В область кнопки. Если да, то  меняем значение переменной, 
    Отвечающей за клики по кнопке
    """

    def is_clicked(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed():
                if self.rect.collidepoint(x, y):
                    self.is_pressed = True
