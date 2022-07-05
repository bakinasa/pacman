import pygame

pygame.init()

from scenes.base import BaseScene

from objects.text import TextObject
from objects.button import ButtonObject
from objects.nameingame import NameInGame
from objects.names_table import Names_table

from constants import RED, YELLOW


class NameScene(BaseScene):
    name = ""

    def __init__(self, game):
        super().__init__(game)
        self.objects.append(
            TextObject(
                self.game, self.game.width // 2, self.game.height // 2 - 250, 'Введите ваше имя', YELLOW, 50
            )
        )

        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 100, self.game.height // 2 + 150, 200, 50,
                RED, self.back_to_menu, 'ОК'
            )
        )

        self.objects.append(
            TextObject(
                self.game, self.game.width // 2, self.game.height // 2, '_____', YELLOW, 60
            )
        )

        self.nameingame = NameInGame(self.game, self.game.width // 2, self.game.height // 2 , 42)
        self.objects.append(self.nameingame)

    def back_to_menu(self):
        self.game.set_scene(self.game.SCENE_HIGHSCORE)
        self.name = ""
        self.nameingame.get_name()

    def process_event(self, event):
        super(NameScene, self).process_event(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.name = self.name[:-1]
                self.nameingame.update_name(self.name)

            elif len(self.name) < 5:
                self.name += event.unicode
                self.nameingame.update_name(self.name)
