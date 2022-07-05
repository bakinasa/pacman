import pygame
pygame.init()

from constants import YELLOW, RED
from objects.button import ButtonObject
from scenes.base import BaseScene
from objects.image import ImageObject
from objects.text import TextObject

class AboutScene(BaseScene):

    TEXT_ABOUT1 = [
                  "Pacman, Версия 1.0.0",
                  "\u00A9 МШП Online,",
                  "S101_04, 2021",
                  "Все права защищены",
                  "",
                  "Препод:",
                  "Смирнов Андрей",
                  "",
                  "Тимлид:",
                  "Шадрин Иван",
                  "",
                  ""]
    TEXT_ABOUT2 = [
                  "Пакман:",
                  "Бунегин Дмитрий",
                  "",
                  "Призраки:",
                  "Родина Елизавета",
                  "Кудрявцев Эдуард",
                  "Сидоров Роман",
                  "Улитина Анна",
                  "",
                  "Дизайн уровня:",
                  "Бондаренко Дмитрий",
                  "",
                  "Дизайн и музыка:",
                  "Лавриненко Данил",
                  ""]
    TEXT_ABOUT3 = [
                  "Меню и сцены:",
                  "Бунегин Дмитрий",
                  "Шадрин Иван",
                  "Зибров Игорь",
                  "Бакина София",
                  "Улитина Анна",
                  "Озден Хусейн",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  ""]

    def __init__(self, game):
        super().__init__(game)
        self.settings = self.game.settings
        self.create_logo()
        #self.create_images()
        self.create_about()
        self.create_buttons()

    def create_logo(self):
        self.objects.append(
            TextObject(
                self.game,
                x=self.game.width // 2, y=self.game.height // 2 - 230,
                text="О создателях", color=YELLOW, size=72
            )
        )
        self.objects.append(
            TextObject(
                self.game,
                x=self.game.width // 2 - 200, y=self.game.height // 2 + 275,
                text="\u00A9 МШП, Online S101_04, 2021", color=YELLOW, size=20
            )
        )

    def create_about(self):

        offset = 300 // len(self.TEXT_ABOUT1)
        currentPosition = 50
        for line in self.TEXT_ABOUT1:
            self.objects.append(
                TextObject(
                    self.game,
                    x=self.game.width // 2 - 250, y=self.game.height // 2 - currentPosition - 100,
                    text=line, color=YELLOW, size=18
                )
            )
            currentPosition -= offset

        offset = 400 // len(self.TEXT_ABOUT2)
        currentPosition = 50
        for line in self.TEXT_ABOUT2:
            self.objects.append(
                TextObject(
                    self.game,
                    x=self.game.width // 2, y=self.game.height // 2 - currentPosition - 100,
                    text=line, color=YELLOW, size=18
                )
            )
            currentPosition -= offset

        offset = 400 // len(self.TEXT_ABOUT3)
        currentPosition = 50
        for line in self.TEXT_ABOUT3:
            self.objects.append(
                TextObject(
                    self.game,
                    x=self.game.width // 2 + 250, y=self.game.height // 2 - currentPosition - 100,
                    text=line, color=YELLOW, size=18
                )
            )
            currentPosition -= offset


    def create_images(self):
        self.objects.append(
            ImageObject(
                self.game, filename="images/menu/background.png",
                x=0, y=0
            )
        )

    def create_buttons(self):
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 350, self.game.height // 2 + 150, 200, 50,
                RED, self.start_menu, 'Назад'
            )
        )

    def start_menu(self):
        self.game.set_scene(self.game.SCENE_MENU)

    def on_activate(self):
        if self.settings.get_key('music') == 'on':
            pygame.mixer.music.load("Background music/What_about_us.mp3")
            pygame.mixer.music.play(-1, fade_ms = 200)

    def on_deactivate(self):
        pygame.mixer.music.pause()

