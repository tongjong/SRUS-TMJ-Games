from app.player import Player


class PlayerBNode:
    def __init__(self, player: Player):
        self._player = player
        self._left = None
        self._right = None

    @property
    def player(self):
        return self._player

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @left.setter
    def left(self, player: Player):
        self._left = player

    @right.setter
    def right(self, player: Player):
        self._right = player
