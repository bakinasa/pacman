"""
This file contains class GameScene.
This class is the scene of the game
"""

import time

import pygame

from constants import RED
from objects.Clyde import Clyde
from objects.blinky import Blinky
from objects.pinky import Pinky
from objects.cherry import CherryObject
from objects.field import Field
from objects.highscoreingamelabel import HighScoreInGameLabel
from objects.inky import Inky
from objects.lives import Lives
from objects.pacman import Pacman
from objects.pinky import Pinky_can_moove
from objects.scoresingamelabel import ScoresInGameLabel
from objects.text import TextObject
from scenes.base import BaseScene


class GameScene(BaseScene):

    def __init__(self, game):
        super().__init__(game)
        self.fear_mode = False
        self.time_start_fear = 0
        self.field = Field(self.game, 10, 10)

    def on_activate(self):
        if len(self.objects) != 0:
            return

        super(GameScene, self).on_activate()

        self.objects.append(self.field)

        self.pacman = Pacman(self.game, self.field.rect.x + 14 * 14, self.field.rect.y + 14 * 23)
        self.objects.append(self.pacman)

        self.score_ingame_label = ScoresInGameLabel(self.game, 670, 50, 25)
        self.objects.append(self.score_ingame_label)

        self.blinky = Blinky(self.game, self.field.rect.y + 13 * 14, self.field.rect.x + 14 * 11)
        self.objects.append(self.blinky)

        self.inky = Inky(self.game, self.field.rect.y + 14 * 12, self.field.rect.x + 14 * 14)
        self.inky.set_time(time.time())
        self.objects.append(self.inky)

        self.pinky = Pinky(self.game, self.field.rect.y + 14 * 13, self.field.rect.x + 14 * 14)
        self.pinky.set_time(time.time())
        self.objects.append(self.pinky)

        self.clyde = Clyde(self.game, self.field.rect.y+14*11, self.field.rect.x+14*13)
        self.objects.append(self.clyde)

        self.cherry = CherryObject(self.game, 20, 525)
        self.objects.append(self.cherry)

        self.lives = Lives(self.game)
        self.objects.append(self.lives)

        self.highscore_ingame_label = HighScoreInGameLabel(self.game, 750, 100, 25)
        self.objects.append(self.highscore_ingame_label)
        self.objects.append(TextObject(self.game, 500, 50, 'Scores: ', RED, 25))
        self.objects.append(TextObject(self.game, 535, 100, 'Highscores: ', RED, 25))

    def all_ghost_to_cage(self):
        self.blinky.rect.x = self.blinky.start_x
        self.blinky.rect.y = self.blinky.start_y
        self.inky.rect.x = self.inky.start_x
        self.inky.rect.y = self.inky.start_y
        self.pinky.rect.x = self.pinky.start_x
        self.pinky.rect.y = self.pinky.start_y

    def process_event(self, event):
        """Processing events coming
               to the scene"""
        super(GameScene, self).process_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.set_scene(self.game.SCENE_MENU)

            if event.key == pygame.K_p:
                self.game.set_scene(self.game.SCENE_PAUSE)

    def process_logic(self):
        super().process_logic()
        self.process_fear_mode_ending()
        self.process_gameover_on_death()

    def process_gameover_on_death(self):
        if not self.lives.is_alive():
            self.game.set_scene(self.game.SCENE_GAMEOVER)

    def process_fear_mode_ending(self):
        now = pygame.time.get_ticks()
        if self.fear_mode:
            if now - self.time_start_fear >= 10000:
                self.fear_mode = False

    def set_new_highscore(self):
        self.game.highscores.add_score('Vasya', 0)
