import pygame
from objects.image import ImageObject


class Lives(ImageObject):

    filename = 'images/pacman_life.png' # потом здесь будет выбранное дизайнерами изображение

    def __init__(self, game, x=None, y=None):
        super().__init__(game)
        self.count = 3
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x if x else 20
        self.rect.y = y if y else self.game.height - self.rect.height - 10

    # Метод, который вызывается при съедении Пакмена
    def i_was_eaten(self):
        if self.count > 0:
            self.count -= 1

    # Метод, проверяющий остались ли у Пакмена жизни
    def is_alive(self):
        return True if self.count > 0 else False

    # Отрисовка по кол-ву жизней
    def process_draw(self):
        x = self.rect.x
        for i in range (self.count):
            self.game.screen.blit(self.image, (x, self.rect.y))
            x += 40
