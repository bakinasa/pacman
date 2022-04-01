import random
from math import sqrt
from pathlib import Path

import pygame

from constants import DEFAULT_MAP
from objects.image import ImageObject


class BaseGhost(ImageObject):
    # filename = 'images/ghost-victim.png'  # так как это базовый класс, выбрал по стандарту это изображение
    filename = 'images/ghosts/inky/ghost-inkyD.png'  # Для примера
    image = pygame.image.load(filename)

    AVAILABLE_DIRECTIONS = [
        [1, 0, 'R'],  # right
        [0, -1, 'U'],  # up
        [-1, 0, 'L'],  # left
        [0, 1, 'D'],  # down
    ]

    def __init__(self, game, x, y):
        super().__init__(game)
        self.rect.x = x
        self.rect.y = y
        self.start_x = x
        self.start_y = y
        self.direction = 2
        self.field = self.game.scenes[self.game.SCENE_GAME].field
        self.save_time = 0
        self.start_filename = self.filename
        self.sound_eat = pygame.mixer.Sound('sounds/death_1.wav')
        self.sound_eat.set_volume(0.1)  # Громкость от 0 до 1
        self.sound_eat_ghost = pygame.mixer.Sound('sounds/eat_ghost.wav')
        self.sound_eat_ghost.set_volume(0.2)  # Громкость от 0 до 1

    def set_time(self, time):
        self.save_time = time

    def check_collisions(self):
        if self.rect.colliderect(self.game.scenes[self.game.SCENE_GAME].pacman.rect):
            game_scene = self.game.scenes[self.game.SCENE_GAME]
            if game_scene.fear_mode is True:  # Если был режим охоты то съедают призрака
                game_scene.score_ingame_label.add_score(200)
                self.sound_eat_ghost.play()
                self.rect.x = self.start_x
                self.rect.y = self.start_y
            else:  # Если не было режима охоты, то пакман съедается
                game_scene.lives.i_was_eaten()
                game_scene.pacman.rect.x = self.field.rect.x + 14 * 14
                game_scene.pacman.rect.y = self.field.rect.y + 14 * 23
                self.sound_eat.play()
                game_scene.all_ghost_to_cage()  # Возвращаем всех призраков на изначальыне места

    def get_cell_index(self, direction):
        field_offset_x = self.field.rect.x
        field_offset_y = self.field.rect.y
        current_direction = self.AVAILABLE_DIRECTIONS[direction]
        column = (self.rect.centery - field_offset_x + 8 * current_direction[1]) // self.field.CELL_WIDTH
        row = (self.rect.centerx - field_offset_y + 8 * current_direction[0]) // self.field.CELL_WIDTH
        return column, row

    def is_in_cage(self, x, y):
        if 14 * 11 + self.field.rect.x < x < 14 * 16 + self.field.rect.x:
            if 14 * 11 + self.field.rect.y < y < 14 * 17 + self.field.rect.y:
                return True
        return False

    def get_target(self):
        """ Переопределите эту функцию, возвращая x и y нужной цели, чтобы призрак гнался за ней """
        return self.game.scenes[self.game.SCENE_GAME].pacman.rect.center

    def get_all_except_back_direction(self):
        directions = []
        for direction in range(0, 4):
            if (self.direction + 2) % 4 != direction:
                cell = self.get_cell_index(direction)
                if DEFAULT_MAP[cell[0]][cell[1]] != 1:
                    directions.append(direction)
        return directions

    def get_random_direction(self):
        directions = self.get_all_except_back_direction()
        return random.choice(directions)

    def get_target_direction(self):
        """ Функция возварщает оптимальное направление к цели, которое вы указываете в виде массива [x, y] """
        # ---- Выбираем 3 направления, исключая направление назад или обратно в клетку и где есть стены ----
        directions = self.get_all_except_back_direction()

        # ---- Сравниваем, что ближе --------
        target = self.get_target()
        target_x, target_y = target[0], target[1]
        min_length = 999999
        best_direction = 0
        for direction in directions:
            cell_x = self.rect.centerx + 7 * self.AVAILABLE_DIRECTIONS[direction][0]
            cell_y = self.rect.centery + 7 * self.AVAILABLE_DIRECTIONS[direction][1]
            length = sqrt(pow(abs(cell_x - target_x), 2) + pow(abs(cell_y - target_y), 2))
            if length < min_length:
                min_length = length
                best_direction = direction

        return best_direction

    def process_logic(self):
        if self.is_in_cage(self.rect.x, self.rect.y) is False:
            self.check_collisions()  # Проверяем коллизию
            self.process_teleport()
            self.process_get_optimal_direction()

        else:
            self.process_cell_exit()

        self.process_image_changing()

        # ------ Двигаем призрака в нужную сторону ------
        self.rect.x += self.AVAILABLE_DIRECTIONS[self.direction][0]
        self.rect.y += self.AVAILABLE_DIRECTIONS[self.direction][1]

    def process_image_changing(self):
        # Поворот изображение во время смены направления и смена картинки при страхе
        if self.game.scenes[self.game.SCENE_GAME].fear_mode is True:  # Если режим страха
            self.filename = 'images/ghost-victim.png'
            self.image = pygame.image.load(self.filename)
        else:
            if self.start_filename.startswith(  # Смена изображение в сторону направления
                    str(Path('.') / 'images' / 'ghosts')):  # Чтобы базовый класс тоже нормально отображался
                direction_letter = self.AVAILABLE_DIRECTIONS[self.direction][2]
                self.filename = f'{self.start_filename[0:-5]}{direction_letter}.png'
                self.image = pygame.image.load(self.filename)

    def process_cell_exit(self):
        up_cell = self.get_cell_index(1)
        if DEFAULT_MAP[up_cell[0]][up_cell[1]] == 1:  # Если стенка сверху
            left_cell = self.get_cell_index(2)
            if DEFAULT_MAP[left_cell[0]][left_cell[1]] == 1 or DEFAULT_MAP[left_cell[0] - 1][
                left_cell[1] - 1] == 1:  # Если сверху и слева стенка, то идём направо
                self.direction = 0
            else:  # Если сверху и справа стенка, то идём налево
                self.direction = 2
        else:
            if ((self.rect.centerx - 10) % 14 == 7 or (self.rect.centerx - 10) % 14 == 6) and (
                    (self.rect.centery - 10) % 14 == 7 or (self.rect.centery - 10) % 14 == 6):
                self.direction = 1

    def process_teleport(self):
        # ---- Телепорт слево на право и наоборот -------
        if self.rect.centerx == 392 and (self.rect.centery == 212 or self.rect.centery == 213):
            self.rect.centerx = 10
            self.rect.centery = 212
        elif self.rect.centerx == 10 and (self.rect.centery == 212 or self.rect.centery == 213):

            self.rect.centerx = 392
            self.rect.centery = 212

    def process_get_optimal_direction(self):
        if ((self.rect.centerx - 10) % 14 == 7 or (self.rect.centerx - 10) % 14 == 6) and (
                (self.rect.centery - 10) % 14 == 7 or (self.rect.centery - 10) % 14 == 6):
            if self.game.scenes[self.game.SCENE_GAME].fear_mode is True:
                # ---- при испуге рандомное направление -----
                self.direction = self.get_random_direction()
            else:
                # ---- ищем оптимальное направление, чтобы поймать пакмана --------
                self.direction = self.get_target_direction()
