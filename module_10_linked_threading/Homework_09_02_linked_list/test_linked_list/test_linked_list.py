import unittest
from LinkedListClass import Node, LinkedList


class TestNode(unittest.TestCase):

    def test_Node(self):
        node_1 = Node('data_test_1')
        self.assertEqual(node_1.data, "data_test_1")
        self.assertEqual(node_1.next_node, None)
        node_2 = Node('data_test_2', node_1)
        self.assertEqual(node_2.data, 'data_test_2')
        self.assertEqual(node_2.next_node, node_1)

class LinkedListClass(unittest.TestCase):

    linkedlist = LinkedList()

    def test_01_init(self):
        self.assertEqual(self.linkedlist.head, None)

    def test_02_insert_at_head(self):
        self.linkedlist.insert_at_head('data_test_1')
        self.assertIsNotNone(self.linkedlist.head)
        self.assertEqual(self.linkedlist.head.data, 'data_test_1')
        self.assertEqual(self.linkedlist.insert_at_head('data_test_2'), "Узел с данными data_test_2 добавлен в начало списка")


    def test_03_insert_at_end(self):
        self.linkedlist.insert_at_end('data_test_3')
        self.assertEqual(self.linkedlist.insert_at_end('data_test_3'), 'Узел с данными data_test_3 добавлен в конец списка')

