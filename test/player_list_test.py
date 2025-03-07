import unittest
from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.player_list = PlayerList()

        self.player_1 = Player("1", "John")
        self.player_node_1 = PlayerNode(self.player_1)

        self.player_2 = Player("2", "Mary")
        self.player_node_2 = PlayerNode(self.player_2)

        self.player_3 = Player("3", "Bob")
        self.player_node_3 = PlayerNode(self.player_3)

    def test_add_at_head_when_player_list_empty(self):
        self.player_list.add_at_head(self.player_node_1)

        self.assertEqual(self.player_list.head, self.player_node_1)
        self.assertIsNone(self.player_list.tail)

    def test_add_at_head_when_player_list_has_one_node(self):
        self.player_list.add_at_head(self.player_node_1)
        self.player_list.add_at_head(self.player_node_2)

        self.assertEqual(self.player_list.head, self.player_node_2)
        self.assertEqual(self.player_list.tail, self.player_node_1)
        self.assertEqual(self.player_node_2.next_node, self.player_node_1)
        self.assertEqual(self.player_node_1.prev_node, self.player_node_2)

    def test_add_at_head_when_player_list_has_more_than_one_node(self):
        self.player_list.add_at_head(self.player_node_1)
        self.player_list.add_at_head(self.player_node_2)
        self.player_list.add_at_head(self.player_node_3)

        self.assertEqual(self.player_list.head, self.player_node_3)
        self.assertEqual(self.player_list.tail, self.player_node_1)
        self.assertIsNone(self.player_list.head.prev_node)
        self.assertIsNone(self.player_list.tail.next_node)
        self.assertEqual(self.player_node_2.next_node, self.player_node_1)
        self.assertEqual(self.player_node_2.prev_node, self.player_node_3)
        self.assertEqual(self.player_node_1.prev_node, self.player_node_2)
        self.assertEqual(self.player_node_3.next_node, self.player_node_2)