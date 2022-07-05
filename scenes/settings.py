import pygame.key

from scenes.base import BaseScene
from objects.button import ButtonObject
from objects.text import TextObject
from objects.image import ImageObject

from constants import YELLOW, RED, BLACK


class SettingsScene(BaseScene):
    UP_INDEX = 0
    DOWN_INDEX = 1
    LEFT_INDEX = 2
    RIGHT_INDEX = 3
    MUTE_INDEX = 4
    MUSIC_INDEX = 5
    SPEAKER_INDEX = 10

    def __init__(self, game):
        super().__init__(game)
        self.settings = self.game.settings
        self.create_images()
        self.create_logo()
        self.objects.append(
            ButtonObject(
                self.game, self.game.width // 2 - 150, self.game.height - 125, 300, 50,
                RED, self.back_to_menu, 'Применить'
            )
        )
        self.buttons = [
            ButtonObject(self.game, self.game.width // 2 - 200, self.game.height // 2 - 125, 150, 50, YELLOW,
                         self.change_up_control, text=f'{chr(self.settings.get_key("up"))}'),
            ButtonObject(self.game, self.game.width // 2 - 175, self.game.height // 2 - 75, 150, 50, YELLOW,
                         self.change_down_control, text=f'{chr(self.settings.get_key("down"))}'),
            ButtonObject(self.game, self.game.width // 2 - 150, self.game.height // 2 - 25, 150, 50, YELLOW,
                         self.change_left_control, text=f'{chr(self.settings.get_key("left"))}'),
            ButtonObject(self.game, self.game.width // 2 - 125, self.game.height // 2 + 25, 150, 50, YELLOW,
                         self.change_right_control, text=f'{chr(self.settings.get_key("right"))}'),
            ButtonObject(self.game, self.game.width // 2 - 100, self.game.height // 2 + 75, 150, 50, YELLOW,
                         self.change_mute_control, text=f'{chr(self.settings.get_key("mute"))}'),
            ButtonObject(self.game, self.game.width // 2 + 200, self.game.height // 2 - 245, 50, 52, BLACK,
                         self.change_music_control)
        ]

        self.add_buttons()

    def create_logo(self):
        self.objects.append(
            TextObject(
                self.game,
                x=self.game.width // 2 - 100, y=self.game.height // 2 - 230,
                text="Настройки", color=YELLOW, size=75
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
                self.game, filename="images/menu/background.png",
                x=0, y=0
            )
        )

    def add_buttons(self):
        self.objects.append(self.buttons[self.UP_INDEX])
        self.objects.append(self.buttons[self.DOWN_INDEX])
        self.objects.append(self.buttons[self.LEFT_INDEX])
        self.objects.append(self.buttons[self.RIGHT_INDEX])
        self.objects.append(self.buttons[self.MUTE_INDEX])
        self.objects.append(self.buttons[self.MUSIC_INDEX])
        self.objects.append(self.speaker_status())

        self.objects.append(
            TextObject(self.game, self.game.width // 2 - 300, self.game.height // 2 - 100, "Вверх: ", YELLOW))
        self.objects.append(
            TextObject(self.game, self.game.width // 2 - 275, self.game.height // 2 - 50, "Вниз: ", YELLOW))
        self.objects.append(
            TextObject(self.game, self.game.width // 2 - 250, self.game.height // 2, "Влево: ", YELLOW))
        self.objects.append(
            TextObject(self.game, self.game.width // 2 - 225, self.game.height // 2 + 50, "Вправо: ", YELLOW))
        self.objects.append(
            TextObject(self.game, self.game.width // 2 - 225, self.game.height // 2 + 100, "Выкл. звук: ", YELLOW))

    def speaker_status(self):
        if self.settings.get_key("music") == 'on':
            return ImageObject(self.game, filename="images/speaker.png",
                               x=self.game.width // 2 + 200, y=self.game.height // 2 - 245)
        else:
            return ImageObject(self.game, filename="images/speaker2.png",
                               x=self.game.width // 2 + 200, y=self.game.height // 2 - 245)

    def change_up_control(self):
        print('changing up control')
        self.settings.set_key('up', self.get_pressed_key())
        self.settings.save_to_file()
        self.objects[self.UP_INDEX + 4] = ButtonObject(self.game, self.game.width // 2 - 200, self.game.height // 2 -
                                                       125, 150, 50, YELLOW, self.change_up_control,
                                                       text=f'{chr(self.settings.get_key("up"))}')

    def change_down_control(self):
        print('changing down control')
        self.settings.set_key('down', self.get_pressed_key())
        self.settings.save_to_file()
        self.objects[self.DOWN_INDEX + 4] = ButtonObject(self.game, self.game.width // 2 - 175, self.game.height // 2 -
                                                         75, 150, 50, YELLOW, self.change_down_control,
                                                         text=f'{chr(self.settings.get_key("down"))}')

    def change_left_control(self):
        print('changing left control')
        self.settings.set_key('left', self.get_pressed_key())
        self.settings.save_to_file()
        self.objects[self.LEFT_INDEX + 4] = ButtonObject(self.game, self.game.width // 2 - 150, self.game.height // 2 -
                                                         25, 150, 50, YELLOW, self.change_left_control,
                                                         text=f'{chr(self.settings.get_key("left"))}')

    def change_right_control(self):
        print('changing right control')
        self.settings.set_key('right', self.get_pressed_key())
        self.settings.save_to_file()
        self.objects[self.RIGHT_INDEX + 4] = ButtonObject(self.game, self.game.width // 2 - 125, self.game.height // 2 +
                                                          25, 150, 50, YELLOW, self.change_right_control,
                                                          text=f'{chr(self.settings.get_key("right"))}')

    def change_mute_control(self):
        print('changing mute control')
        self.settings.set_key('mute', self.get_pressed_key())
        self.settings.save_to_file()
        self.objects[self.MUTE_INDEX + 4] = ButtonObject(self.game, self.game.width // 2 - 100, self.game.height // 2 +
                                                         75, 150, 50, YELLOW, self.change_mute_control,
                                                         text=f'{chr(self.settings.get_key("mute"))}')

    def change_music_control(self):
        if self.settings.get_key('music') == 'on':
            self.settings.set_key_music('music', 'off')
            self.on_deactivate()
            self.objects[self.SPEAKER_INDEX] = ImageObject(self.game, filename="images/speaker2.png",
                                                           x=self.game.width // 2 + 200, y=self.game.height // 2 - 245)
            self.settings.save_to_file()
        else:
            self.settings.set_key_music('music', 'on')
            self.on_activate()
            self.objects[self.SPEAKER_INDEX] = ImageObject(self.game, filename="images/speaker.png",
                                                           x=self.game.width // 2 + 200, y=self.game.height // 2 - 245)
            self.settings.save_to_file()

    @staticmethod
    def get_pressed_key():
        ret = None
        while not ret:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    ret = event.key
                    break
        return ret

    def process_event(self, event):
        super(SettingsScene, self).process_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.set_scene(self.game.SCENE_MENU)

    def back_to_menu(self):
        self.game.set_scene(self.game.SCENE_MENU)

    def on_activate(self):
        if self.settings.get_key('music') == 'on':
            pygame.mixer.music.load("Background music/Under_the_hood.mp3")
            pygame.mixer.music.play(-1, fade_ms=200)

    def on_deactivate(self):
        pygame.mixer.music.pause()
