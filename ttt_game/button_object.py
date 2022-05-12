import pygame

# Класс, описывающий общее поведение кнопок в меню

class button:

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
        self.image = pygame.image.load('pictures/play.png')
        """
        Так как пустым поле оставить нельзя, было выбрано 
        # случайное изображение
        """
        self.rect = self.image.get_rect()
        self.rect.x = 475
        self.rect.y = 200
        self.rect.width = 250
        self.rect.height = 100
        self.is_pressed = False

    """
    Функция, для вывода кнопки на экран
    """

    def button_show(self):
        self.screen.blit(self.image, self.rect)

    """
    event: событие, которое произошло (клик мышкой, перемещений курсора и т.д.)
    Функция, отвечающая за клики мышки по кнопке.
    Каждый вызов функции она проверяет кликнул ли пользователь
    Если да, то получаем координаты мышки и проверяем, попали ли они
    В игровое поле. Если да, то  меняем значение переменной,
    Отвечающей за клики по кнопке
    """

    def is_clicked(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed():
                if self.rect.collidepoint(x, y):
                    self.is_pressed = True

    """
    Функция - некий костыль, при импорте класса в другой файл и использовании его для наследования
    Оказалось, что метод is_clicked() не хочет ничего возвращать(там был return)
    И поэтому было принято решение во всех классах создавать переменные для изменения состояния кнопки.
    А эта функция нужна только для 'отжатия кнопки' в исходное состояние
    """

    def return_to_false(self):
        if self.is_pressed:
            self.is_pressed = False
