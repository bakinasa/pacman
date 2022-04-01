import pygame
from objects.image import ImageObject

import constants
from objects.grain import Grain
from objects.biggrain import BigGrain


class Pacman(ImageObject):
    filename = 'images/pacman/pacman-R.png'

    # Directions of movement on the field
    AVAILABLE_DIRECTIONS = [
        [0, 0, 'R'],  # stay
        [1, 0, 'R'],  # right
        [0, -1, 'U'],  # up
        [-1, 0, 'L'],  # left
        [0, 1, 'D'],  # down
    ]
    # Keys of direction of movement
    KEY_DIRECTIONS = {
        pygame.K_d: 1,
        pygame.K_w: 2,
        pygame.K_a: 3,
        pygame.K_s: 4,
    }
    # Pacman's speed
    SPEED = 2

    # Pacman initialisation
    def __init__(self, game, x, y):
        super().__init__(game, None, x, y)
        self.direction = 0
        self.last_update = pygame.time.get_ticks()
        self.is_eating = False
        self.eaten_grains = 0
        self.start_fear_time = 0
        self.sound_eat = pygame.mixer.Sound('sounds/eat_fruit.wav')
        self.sound_eat.set_volume(0.1)  # Громкость от 0 до 1
        self.sound_start_fear = pygame.mixer.Sound('sounds/power_pellet.wav')
        self.sound_start_fear.set_volume(0.1)
        self.sound_update = pygame.time.get_ticks()
        self.wanted_direction = 0

    def get_current_cell_index(self):
        field = self.game.scenes[self.game.SCENE_GAME].field
        field_offset_x = field.rect.x
        field_offset_y = field.rect.y
        column = (self.rect.centery - field_offset_x) // field.CELL_WIDTH
        row = (self.rect.centerx - field_offset_y) // field.CELL_WIDTH
        return column, row

    # Processing of events coming to the scene
    def get_place(self):
        return self.rect

    def process_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key not in self.KEY_DIRECTIONS.keys():
            return
        self.wanted_direction = self.KEY_DIRECTIONS[event.key]

    # Logical processes of the Pacman
    def process_logic(self):
        if self.rect.centerx == 392 and (self.rect.centery == 212 or self.rect.centery == 213):
            self.rect.centerx = 10
            self.rect.centery = 212
        elif self.rect.centerx == 10 and (self.rect.centery == 212 or self.rect.centery == 213):
            self.rect.centerx = 392
            self.rect.centery = 212
        if constants.DEFAULT_MAP[
            (self.rect.centery - 10 + 7 * self.AVAILABLE_DIRECTIONS[self.direction][1]) // 14][
            (self.rect.centerx - 10 + 7 * self.AVAILABLE_DIRECTIONS[self.direction][0]) // 14] == 1:
            self.AVAILABLE_DIRECTIONS[0][2] = self.AVAILABLE_DIRECTIONS[self.direction][2]
            self.direction = 0
        if ((self.rect.centerx - 10) % 14 == 7 or (self.rect.centerx - 10) % 14 == 6) and (
                (self.rect.centery - 10) % 14 == 7 or (self.rect.centery - 10) % 14 == 6):
            if constants.DEFAULT_MAP[
                (self.rect.centery - 10 + 8 * self.AVAILABLE_DIRECTIONS[self.wanted_direction][1]) // 14
            ][
                (self.rect.centerx - 10 + 8 * self.AVAILABLE_DIRECTIONS[self.wanted_direction][0]) // 14
            ] != 1:
                self.direction = self.wanted_direction
                direction_letter = self.AVAILABLE_DIRECTIONS[self.direction][2]
                self.filename = f'{self.filename[0:-5]}{direction_letter}.png'
                self.image = pygame.image.load(self.filename)

        self.rect.x += self.AVAILABLE_DIRECTIONS[self.direction][0]
        self.rect.y += self.AVAILABLE_DIRECTIONS[self.direction][1]

        # Animation
        now = pygame.time.get_ticks()
        if now - self.last_update > 250:  # Если прошло 250мс
            self.last_update = now
            direction_letter = self.AVAILABLE_DIRECTIONS[self.direction][2]
            if self.filename.startswith('images/pacman/pacman_eat'):
                self.filename = f'images/pacman/pacman-{direction_letter}.png'
            else:
                self.filename = f'images/pacman/pacman_eat-{direction_letter}.png'
            self.image = pygame.image.load(self.filename)

        # eating grains
        next_x, next_y = self.get_current_cell_index()
        next_cell = self.game.scenes[self.game.SCENE_GAME].field.get_value(next_x, next_y)
        if not isinstance(next_cell, int):
            self.is_eating = True
            if isinstance(next_cell, Grain):
                self.game.scenes[self.game.SCENE_GAME].score_ingame_label.add_score(10)
            elif isinstance(next_cell, BigGrain):
                self.game.scenes[self.game.SCENE_GAME].score_ingame_label.add_score(50)
                self.game.scenes[self.game.SCENE_GAME].fear_mode = True
                self.game.scenes[self.game.SCENE_GAME].time_start_fear = pygame.time.get_ticks()
                self.sound_start_fear.play()
            self.game.scenes[self.game.SCENE_GAME].field.set_value(next_x, next_y, 0)
            self.eaten_grains += 1
            if self.eaten_grains == 246:
                self.game.set_scene(self.game.SCENE_GAMEOVER)
        else:
            self.is_eating = False

        # Звук после съедения
        if self.is_eating is True:
            if now - self.sound_update > round(self.sound_eat.get_length() * 1000) + 50:
                # +50 это задержка перед следующим воиспроизведением
                self.sound_update = now
                self.sound_eat.play()

    def get_place(self):
        return self.rect
