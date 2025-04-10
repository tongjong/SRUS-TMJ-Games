import unittest

from app.player import Player
from app.player_bst import PlayerBST


class TestPlayerBts(unittest.TestCase):
    def setUp(self):
        self.dan = Player('04', "Dan", 25)
        self.alice = Player('01', "Alice", 5)
        self.bob = Player('02', "Bob", 10)
        self.charlie = Player('03', "Charlie", 15)

        self.players = [self.dan, self.alice, self.bob, self.charlie]

        self.player_bst = PlayerBST()

    def test_insert_creates_valid_bst(self):
        dan_node = self.player_bst.insert(self.dan)
        alice_node = self.player_bst.insert(self.alice)
        bob_node = self.player_bst.insert(self.bob)
        charlie_node = self.player_bst.insert(self.charlie)

        self.assertEqual(dan_node.left.player, self.alice)
        self.assertEqual(alice_node.right.player, self.bob)
        self.assertEqual(bob_node.right.player, self.charlie)
        self.assertIsNone(charlie_node.right)
        self.assertIsNone(charlie_node.left)

    def test_search_returns_player_if_found(self):
        for player in self.players:
            self.player_bst.insert(player)

        result_alice = self.player_bst.search("alice")
        result_bob = self.player_bst.search("BOB")

        self.assertEqual(result_alice.name, self.alice.name)
        self.assertEqual(result_bob.name, self.bob.name)

    def test_search_returns_false_if_not_found(self):
        for player in self.players:
            self.player_bst.insert(player)

        result = self.player_bst.search("doesnotexist")

        self.assertFalse(result)

