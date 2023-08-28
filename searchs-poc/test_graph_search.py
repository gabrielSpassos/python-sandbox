#!/usr/bin/python
import unittest

from graph_search import *
from node import Node

class Test(unittest.TestCase):
    def test_bfs_with_root_as_destiny(self):
        node_one = self.create_graph()
        target = 1
        assert True == bfs(node_one, target)


    def test_bfs_should_find_path(self):
        node_one = self.create_graph()
        target = 8
        assert True == bfs(node_one, target)


    def test_bfs_should_not_find_path(self):
        node_one = self.create_graph()
        target = 11
        assert False == bfs(node_one, target)

    
    def test_dfs_with_root_as_destiny(self):
        node_one = self.create_graph()
        target = 1
        assert True == dfs(node_one, target)

    
    def test_dfs_should_find_path(self):
        node_one = self.create_graph()
        target = 10
        assert True == dfs(node_one, target)

    
    def test_dfs_should_not_find_path(self):
        node_one = self.create_graph()
        target = 11
        assert False == dfs(node_one, target)


    def create_graph(self):
        node_nine = Node(9, [])
        node_five = Node(5, [node_nine])
        node_two = Node(2, [node_five])

        node_ten = Node(10, [])
        node_six = Node(6, [node_ten])
        node_seven = Node(7, [])
        node_three = Node(3, [node_six, node_seven])

        node_eight = Node(8, [])
        node_four = Node(4, [node_eight])

        node_one = Node(1, [node_two, node_three, node_four])
        return node_one;