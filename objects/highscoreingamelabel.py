from objects.text import TextObject
from constants import RED


class HighScoreInGameLabel(TextObject):
    def __init__(self, game, x=0, y=0, size=25):
        if len(game.highscores.get_highscores()) == 0:
            self.highscore = 0
        else:
            self.highscore = game.highscores.get_highscores()[0][1]
        super().__init__(game, x, y, f'{self.highscore}', RED, size)
