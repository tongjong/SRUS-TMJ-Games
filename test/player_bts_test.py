import unittest

from app.player import Player
from app.player_bst import PlayerBST


class TestPlayerBts(unittest.TestCase):
    def test_insert_creates_valid_bst(self):
        dan = Player('04', "Dan", 25)
        alice = Player('01', "Alice", 5)
        bob = Player('02', "Bob", 10)
        charlie = Player('03', "Charlie", 15)

        player_bst = PlayerBST()
        dan_node = player_bst.insert(dan)
        alice_node = player_bst.insert(alice)
        bob_node = player_bst.insert(bob)
        charlie_node = player_bst.insert(charlie)

        self.assertEqual(dan_node.left.player, alice)
        self.assertEqual(alice_node.right.player, bob)
        self.assertEqual(bob_node.right.player, charlie)
        self.assertIsNone(charlie_node.right)
        self.assertIsNone(charlie_node.left)