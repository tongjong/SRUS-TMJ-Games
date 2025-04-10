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


    def _insert_bnode(self, root: PlayerBNode, player: Player) -> PlayerBNode:
        if player < root.player:
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


if __name__ == '__main__':
    dan = Player('04', "Dan", 25)
    alice = Player('01', "Alice", 5)
    bob = Player('02', "Bob", 10)
    charlie = Player('03', "Charlie", 15)
    player_bst = PlayerBST()

    dan_node = player_bst.insert(dan)
    alice_node = player_bst.insert(alice)
    bob_node = player_bst.insert(bob)
    charlie_node = player_bst.insert(charlie)

    print(dan_node.left.player.name)


