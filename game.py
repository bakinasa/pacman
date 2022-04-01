"""
This file contains class "Game".
The "Game" class contains screen and scene configurations.
Also has methods for rendering scenes, closing the game.
"""

# imports
import pygame

from constants import BLACK
from scenes.game import GameScene
from scenes.gameover import GameOverScene
from scenes.menu import MenuScene

from scenes.about import AboutScene
from scenes.pause import PauseScene
from scenes.menu_highscores import HighscoreScene
from scenes.settings import SettingsScene


# "Game" class
from system.settings import Settings
from system.highscore import HighScore


class Game:
    # window size
    size = width, height = 800, 600

    # scene indexes
    SCENE_MENU = 0
    SCENE_GAME = 1
    SCENE_GAMEOVER = 2
    SCENE_HIGHSCORE = 3
    SCENE_PAUSE = 4
    SCENE_GAMEABOUT = 5
    SCENE_SETTINGS = 6
    current_scene_index = SCENE_MENU

    def __init__(self):
        # class variables
        self.screen = pygame.display.set_mode(self.size)

        self.settings = Settings()
        self.highscores = HighScore()

        self.scenes = [
            MenuScene(self),
            GameScene(self),
            GameOverScene(self),
            HighscoreScene(self),
            PauseScene(self),
            AboutScene(self),
            SettingsScene(self)
        ]
        self.field = self.scenes[self.SCENE_GAME].field

        self.game_over = False

    # Handling a "game end" button click
    @staticmethod
    def exit_button_pressed(event):
        return event.type == pygame.QUIT

    # exit with hotkey ctrl + q
    @staticmethod
    def exit_hotkey_pressed(event):
        return event.type == pygame.KEYDOWN and event.mod & pygame.KMOD_CTRL and event.key == pygame.K_q

    # activated when the game is closed
    def process_exit_events(self, event):
        if Game.exit_button_pressed(event) or Game.exit_hotkey_pressed(event):
            self.exit_game()

    # activate events
    def process_all_events(self):
        for event in pygame.event.get():
            self.process_exit_events(event)
            self.scenes[self.current_scene_index].process_event(event)

    # activate logic
    def process_all_logic(self):
        self.scenes[self.current_scene_index].process_logic()

    # set scene
    def set_scene(self, index):
        self.scenes[self.current_scene_index].on_deactivate()
        self.current_scene_index = index
        self.scenes[self.current_scene_index].on_activate()

    # scene rendering process
    def process_all_draw(self):
        self.screen.fill(BLACK)
        self.scenes[self.current_scene_index].process_draw()
        pygame.display.flip()

    # function for activate logic, events, render scene and call the process of closing the game
    def main_loop(self):
        while not self.game_over:
            self.process_all_events()
            self.process_all_logic()
            self.process_all_draw()
            pygame.time.wait(10)

    def exit_game(self):
        print('Игра окончена!!!')
        self.game_over = True
