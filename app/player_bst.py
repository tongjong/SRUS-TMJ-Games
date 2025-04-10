from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, player: Player) -> PlayerBNode:
        if self._root is None:
            self._root =  PlayerBNode(player)
            return self._root
        else:
            return self._insert_bnode(self._root, player)

    def search(self, name: str) -> Player | None:
        return self._search_bnode(self._root, name)

    def _search_bnode(self, root: PlayerBNode, name: str) -> Player | bool:
        if root is None:
            return False
        if root.player.name.upper() == name.upper():
            return root.player
        if name.upper() < root.player.name.upper():
            return self._search_bnode(root.left, name)
        else:
            return self._search_bnode(root.right, name)

    def _insert_bnode(self, root: PlayerBNode, player: Player) -> PlayerBNode:
        if player.name < root.player.name:
            if root.left is None:
                root.left = PlayerBNode(player)
                return root.left
            else:
                return self._insert_bnode(root.left, player)
        else:
            if root.right is None:
                root.right = PlayerBNode(player)
                return root.right
            else:
                return self._insert_bnode(root.right, player)




