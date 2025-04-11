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

    def sort(self, root: PlayerBNode) -> list:
        if root is None:
            return []
        return self.sort(root.left) + [root.player] + self.sort(root.right)

    def create_balanced_bst(self, sorted_list):
        if not sorted_list:
            return None

        mid_index = len(sorted_list) // 2
        root = sorted_list[mid_index]
        root.left = self.create_balanced_bst(sorted_list[:mid_index])
        root.right = self.create_balanced_bst(sorted_list[mid_index+1:])
        return root

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



if __name__ == '__main__':
    dan = Player('04', "Dan", 25)
    alice = Player('01', "Alice", 5)
    bob = Player('02', "Bob", 10)
    charlie = Player('03', "Charlie", 15)
    ethan = Player('05', "Alic", 2)

    players = [dan, alice, bob, charlie, ethan]
    player_bst = PlayerBST()
    for player in players:
        player_bst.insert(player)

    sorted_list = player_bst.sort(player_bst.root)
    print(sorted_list)
    print(player_bst.create_balanced_bst(sorted_list))
