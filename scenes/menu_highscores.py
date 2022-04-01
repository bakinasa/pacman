import pygame

from constants import GREEN, RED, YELLOW
from objects.button import ButtonObject
from objects.highscores_table import Highscores_table
from objects.names_table import Names_table
from objects.text import TextObject
from scenes.base import BaseScene


class HighscoreScene(BaseScene):

    def __init__(self, game):
        super().__init__(game)
        self.settings = self.game.settings
        self.objects.append(
            TextObject(
                self.game, self.game.width // 2, 30, 'Таблица рекордов', YELLOW, 60
            )
        )
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 360, self.game.height - 100, 320, 50,
                RED, self.back_to_menu, 'Вернуться в меню'
            )
        )
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 + 40, self.game.height - 100, 320, 50,
                RED, self.reset_highscores, 'Сбросить результаты'
            )
        )
        self.objects.append(TextObject(self.game, self.game.width // 2 - 200, 90, 'Имя:', YELLOW))
        self.objects.append(TextObject(self.game, self.game.width // 2 + 200, 90, 'Счет:', YELLOW))

        self.objects.append(
            TextObject(
                self.game,
                x=self.game.width // 2 - 200, y=self.game.height // 2 + 275,
                text="\u00A9 МШП, Online S101_04, 2021", color=YELLOW, size=20
            )
        )

        self.highscores = self.game.highscores
        highscore_list = self.highscores.get_highscores()
        self.highscores_table = []
        self.names_table = []

        for i in range(len(highscore_list)):
            self.highscores_table.append(Highscores_table(self.game, highscore_list[i][1], i))
            self.names_table.append(Names_table(self.game, highscore_list[i][0], i))
            self.objects.append(self.names_table[i])
            self.objects.append(self.highscores_table[i])

    def back_to_menu(self):
        self.game.set_scene(self.game.SCENE_MENU)

    def reset_highscores(self):
        self.highscores.make_clear()
        for highscore in self.highscores_table:
            highscore.update('')

        for name in self.names_table:
            name.update('')

    def on_activate(self):
        if self.settings.get_key('music') == 'on':
            pygame.mixer.music.load("Background music/Champions.mp3")
            pygame.mixer.music.play(-1, fade_ms = 200)

    def on_deactivate(self):
        pygame.mixer.music.pause()

    def process_event(self, event):
        super(HighscoreScene, self).process_event(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.set_scene(self.game.SCENE_MENU)
