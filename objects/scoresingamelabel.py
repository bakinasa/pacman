from objects.text import TextObject
from constants import RED


class ScoresInGameLabel(TextObject):
    def __init__(self, game, x=0, y=0, size=25):
        self.scores = 0
        super().__init__(game, x, y, f'{self.scores}', RED, size)

    def add_score(self, scores):
        self.scores += scores
        TextObject.update_text(self, f'{self.scores}')

    def get_scores(self):
        return self.scores
