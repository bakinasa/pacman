"""This file contains class BaseScene.
Class BaseScene a parent class for other scene classes. 
It contains the main actions for other scenes
"""
import pygame


class BaseScene:
    def __init__(self, game):
        self.game = game
        self.objects = []

    def on_activate(self):
        """
        Turning on the scene
        """
        pass

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.set_scene(self.game.SCENE_MENU)
        """Processing events coming
        to the scene"""
        for object in self.objects:
            object.process_event(event)



    def process_logic(self):
        """
        Activate logic
        """
        for object in self.objects:
            object.process_logic()

    def process_draw(self):
        """Drawing"""
        for object in self.objects:
            object.process_draw()

    def on_deactivate(self):
        """

        Turning off the scene

        """
        pass
