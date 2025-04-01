import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.alice = Player('01', "Alice", 5)
        self.bob = Player('02', "Bob", 10)
        self.charlie = Player('03', "Charlie", 15)

    def test_uid_property_returns_uid_value(self):
        player_1 = Player("1", "John")
        self.assertEqual(player_1.uid, "1")

    def test_name_property_returns_name_value(self):
        player_1 = Player("1", "John")
        self.assertEqual(player_1.name, "John")

    def test_sort_player(self):

        players = [self.alice, self.bob, self.charlie]
        manually_sorted_players = [self.bob, self.alice, self.charlie]

        sorted_players = sorted(players)

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        self.assertTrue(self.alice < self.bob)


