from pathlib import Path
from objects.base_ghost import BaseGhost


class Inky(BaseGhost):
    filename = str(Path('.') / 'images' / 'ghosts' / 'inky' / 'ghost-inkyR.png')

    def __init__(self, game, x, y):
        super(Inky, self).__init__(game, x, y)
        self.pacman = self.game.scenes[self.game.SCENE_GAME].pacman
        self.blinky = self.game.scenes[self.game.SCENE_GAME].blinky

    def get_pacman_cell(self):
        cell_x = (self.pacman.rect.centerx - self.game.field.rect.x) // self.game.field.CELL_WIDTH
        cell_y = (self.pacman.rect.centery - self.game.field.rect.y) // self.game.field.CELL_WIDTH
        return [cell_x, cell_y]

    def get_target(self):
        pacman_pos = self.get_pacman_cell()
        pacman_pos[0] += 2 * self.pacman.AVAILABLE_DIRECTIONS[self.pacman.direction][0]
        pacman_pos[1] += 2 * self.pacman.AVAILABLE_DIRECTIONS[self.pacman.direction][1]
        target = pacman_pos
        blinky_pos = self.blinky.get_cell_index(self.blinky.direction)
        target[0] += (pacman_pos[0] - blinky_pos[0])
        target[1] += (pacman_pos[1] - blinky_pos[1])
        return target[0] * 14 + self.game.field.rect.x, target[1] * 14+self.game.field.rect.x
