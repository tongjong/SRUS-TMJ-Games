import unittest
from typing import Tuple

from app.player import Player
from app.player_hashmap import PlayerHashMap


class TestPlayerHashMap(unittest.TestCase):
    def setUp(self):
        self.SIZE = 10
        self.hashmap = PlayerHashMap()
        self.player_1 = Player("1", "John")

    # get_index
    def test_get_index(self):
        index_of_1 = self.hashmap.get_index("1")
        index_of_1_too = self.hashmap.get_index("1")
        index_of_120 = self.hashmap.get_index("120")
        index_of_121 = self.hashmap.get_index("121")
        index_of_player_instance = self.hashmap.get_index(self.player_1)

        self.assertEqual(index_of_1, index_of_1_too)
        self.assertNotEqual(index_of_120, index_of_121)
        self.assertEqual(index_of_1, index_of_player_instance)
        self.assertTrue(index_of_120 < self.SIZE)

    # get_item
    def test_get_item_returns_none_when_list_empty(self):
        value_of_1 = self.hashmap["1"]
        value_of_player_1 = self.hashmap[self.player_1.uid]

        self.assertIsNone(value_of_1, value_of_player_1)

    def test_get_item_returns_tuple_when_list_not_empty(self):
        self.hashmap["1"] = "John"
        self.hashmap["2"] = "Mary"

        value_of_1 = self.hashmap["1"]
        value_of_2 = self.hashmap["2"]

        self.assertIsNotNone(value_of_1, value_of_2)
        self.assertIsInstance(value_of_1, Tuple)
        self.assertIsInstance(value_of_2, Tuple)
        self.assertEqual(value_of_1[1].name, "John")
        self.assertEqual(value_of_2[1].name, "Mary")
        self.assertEqual(value_of_2[0], self.hashmap.get_index("2"))

    # set
    def test_set_item_updates_value_if_player_already_exists(self):
        self.hashmap["1"] = "John"

        self.hashmap["1"] = "John Doe"

        self.assertEqual(self.hashmap["1"][1].name, "John Doe")

    def test_set_item_adds_new_player_node_to_hashmap_if_the_player_does_not_exist(self):
        self.hashmap["1"] = "John"
        self.hashmap["11"] = "Mary"

        self.assertEqual(self.hashmap["1"][1].name, "John")
        self.assertEqual(self.hashmap["1"][1].uid, "1")
        self.assertEqual(self.hashmap["11"][1].name, "Mary")
        self.assertEqual(self.hashmap["11"][1].uid, "11")

    # del
    def test_del_item_raise_key_value_exception_if_player_does_not_exist(self):
        with self.assertRaises(KeyError) as err:
            del self.hashmap["1"]

        self.assertEqual(err.exception.args[0], "Player not found")

    def test_del_item_removes_player_from_hashmap_if_the_player_exists(self):
        self.hashmap["1"] = "John"
        self.hashmap["2"] = "Mary"

        del self.hashmap["1"]

        self.assertTrue(len(self.hashmap) == 1)
        self.assertIsNone(self.hashmap["1"])
        self.assertIsNotNone(self.hashmap["2"])

    # len
    def test_len_returns_number_of_players_in_hashmap(self):
        self.hashmap["1"] = "John"
        self.hashmap["2"] = "Mary"
        self.hashmap["3"] = "David"

        number_of_players = len(self.hashmap)

        self.assertEqual(number_of_players, 3)

    # display
    def test_display_returns_empty_list_when_hashmap_has_no_players(self):
        result = self.hashmap.display()

        self.assertTrue(len(result) == 0)
        self.assertEqual(result, [])

    def test_display_returns_player_list_index_and_all_players_in_the_list(self):
        self.hashmap["10"] = "John"
        self.hashmap["20"] = "Alex"
        self.hashmap["30"] = "Mary"
        index_of_10 = self.hashmap.get_index("10")
        index_of_20 = self.hashmap.get_index("20")
        index_of_30 = self.hashmap.get_index("30")

        players = self.hashmap.display()
        result_of_10 = f'{index_of_10}: Unique Id: 10, Player Name: John | '
        result_of_20 = f'{index_of_20}: Unique Id: 20, Player Name: Alex | '
        result_of_30 = f'{index_of_30}: Unique Id: 30, Player Name: Mary | '

        self.assertIn(result_of_10, players)
        self.assertIn(result_of_20, players)
        self.assertIn(result_of_30, players)


