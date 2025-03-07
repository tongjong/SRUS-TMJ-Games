from typing import List
from app.player import Player
from app.player_list import PlayerList


class PlayerHashMap:
    def __init__(self, size:int =10):
        self._size = size
        self._hash_table: List[PlayerList] = [PlayerList() for _ in range(self._size)]

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self._size
        else:
            return Player.hash(key) % self._size