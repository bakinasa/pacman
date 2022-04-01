import pygame


# DrawableObject class. This class is parent of each drawable object
class DrawableObject():

    # DrawableObject initializer
    def __init__(self, game):
        self.game = game
        self.rect = pygame.rect.Rect(0, 0, 0, 0)

    # Moving method
    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y

    # Moving by center method
    def move_center(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y

    # Porcess event method
    def process_event(self, event):
        pass

    # Process logic method
    def process_logic(self):
        pass

    # Process draw method
    def process_draw(self):
        pass  # use self.game.screen for drawing, padawan
