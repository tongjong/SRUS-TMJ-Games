import unittest
from app.player import Player
import random

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
        manually_sorted_players = [self.alice, self.bob, self.charlie]

        sorted_players = sorted(players)

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        self.assertTrue(self.alice < self.bob)

    def test_sort(self):
        sorted_players_descend = Player.sort([self.alice, self.bob, self.charlie])
        sorted_players_ascend = Player.sort([self.alice, self.bob, self.charlie], descend=False)
        manually_sorted_players_ascend = [self.alice, self.bob, self.charlie]
        manually_sorted_players_descend = [self.charlie, self.bob, self.alice]

        self.assertListEqual(sorted_players_ascend, manually_sorted_players_ascend)
        self.assertListEqual(sorted_players_descend, manually_sorted_players_descend)

    def test_sort_with_1000_players(self):
        players = [Player(f"{i:03}", f"Player {i}", score=random.randint(0, 1000)) for i in range(1000)]

        sorted_players_using_custom_alg = Player.sort(players, descend=False)
        sorted_players_using_built_in_alg = sorted(players)

        self.assertListEqual(sorted_players_using_built_in_alg, sorted_players_using_custom_alg)

    def test_sort_with_sorted_list_with_1000_players(self):
        players = [Player(f"{i:03}", f"Player {i}", score=i) for i in range(1000)]

        sorted_players_using_custom_alg = Player.sort(players, descend=False)
        sorted_players_using_built_in_alg = sorted(players)

        self.assertListEqual(sorted_players_using_built_in_alg, sorted_players_using_custom_alg)