import pygame

from objects.base import DrawableObject


# TextObject class
class TextObject(DrawableObject):

    # TextObject class initializer
    def __init__(self, game, x, y, text, color, size=30):
        super().__init__(game)
        self.color = color
        self.y = y
        self.x = x
        self.font = pygame.font.Font('fonts/Tahoma.ttf', size)
        self.update_text(text)

    # Method of updating text
    def update_text(self, text):
        self.text = text
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect()
        self.move_center(self.x, self.y)

    # Process draw method
    def process_draw(self):
        self.game.screen.blit(self.surface, self.rect)
