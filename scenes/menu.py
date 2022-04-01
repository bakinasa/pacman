"""
This file contains class MenuScene.
This class is the scene of the menu for game
"""
import pygame
pygame.init()
from constants import ORANGE, YELLOW, RED, GREY, BLACK
from objects.button import ButtonObject
from scenes.base import BaseScene
from objects.image import ImageObject
from objects.text import TextObject


class MenuScene(BaseScene):

    def __init__(self, game):
        super().__init__(game)
        self.settings = self.game.settings
        if self.settings.get_key('music') == 'on':
            pygame.mixer.music.load("Background music/Packed.mp3")
            pygame.mixer.music.play(-1)
        self.create_logo()
        self.create_images()
        self.create_buttons()


    def create_logo(self):
        self.objects.append(
            TextObject(
                self.game,
                x=self.game.width // 2 - 100, y=self.game.height // 2 - 230,
                text="Pacman", color=YELLOW, size=100
            )
        )
        self.objects.append(
            TextObject(
                self.game,
                x=self.game.width // 2 - 200, y=self.game.height // 2 + 275,
                text="\u00A9 МШП, Online S101_04, 2021", color=YELLOW, size=20
            )
        )

    def create_images(self):
        self.objects.append(
            ImageObject(
                self.game, filename="images/menu/background_pacman.png",
                x=0, y=0
            )
        )

    def create_buttons(self):
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 375, self.game.height // 2 - 90, 200, 50,
                YELLOW, self.start_game, 'Играть'
            )
        )
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 350, self.game.height // 2 - 30, 200, 50,
                YELLOW, self.record_list, 'Рекорды'
            )
        )
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 325, self.game.height // 2 + 30, 200, 50,
                YELLOW, self.options, 'Настройки'
            )
        )
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 300, self.game.height // 2 + 90, 200, 50,
                YELLOW, self.about_programm, 'О создателях'
            )
        )
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 275, self.game.height // 2 + 150, 200, 50,
                RED, self.game.exit_game, 'Выход'
            )
        )

    def start_game(self):
        """
                Starting the game
                """
        self.game.set_scene(self.game.SCENE_GAME)

    def record_list(self):
        self.game.set_scene(self.game.SCENE_HIGHSCORE)

    def options(self):
        self.game.set_scene(self.game.SCENE_SETTINGS)

    def about_programm(self):
        self.game.set_scene(self.game.SCENE_GAMEABOUT)

    def on_activate(self):
        if self.settings.get_key('music') == 'on':
            pygame.mixer.music.load("Background music/Packed.mp3")
            pygame.mixer.music.play(-1, fade_ms = 200)
            self.game.scenes[self.game.SCENE_GAME].objects.clear()

    def on_deactivate(self):
        pygame.mixer.music.pause()
