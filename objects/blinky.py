from pathlib import Path
from objects.base_ghost import BaseGhost


class Blinky(BaseGhost):
    filename = str(Path('.') / 'images' / 'ghosts' / 'blinky' / 'ghost-blinkyU.png')

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
