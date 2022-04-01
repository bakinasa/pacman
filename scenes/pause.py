import pygame
pygame.init()

from constants import RED
from constants import ORANGE
from objects.button import ButtonObject
from scenes.base import BaseScene
from objects.text import TextObject

class PauseScene(BaseScene):
    text_format = "P A U S E"

    def __init__(self, game):
        super().__init__(game)
        self.settings = self.game.settings
        self.objects.append(
            TextObject(
                self.game, self.game.width // 2, self.game.height // 2 - 100, self.text_format, color=ORANGE)
        )

        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 150, self.game.height // 2 - 20 - 25, 300, 50,
                RED, self.start_game, text='Продолжить игру'
            )
        )
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 150, self.game.height // 2 + 25, 300, 50,
                RED, self.game.exit_game, text='Выход из игры'
            )
        )
    def start_game(self):
        self.game.set_scene(self.game.SCENE_GAME)

    def on_activate(self):
        if self.settings.get_key('music') == 'on':
            pygame.mixer.music.load("Background music/Tiny_break.mp3")
            pygame.mixer.music.play(-1, fade_ms = 200)

    def on_deactivate(self):
        pygame.mixer.music.pause()
