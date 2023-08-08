#!/usr/bin/python
from array_search import linear_search, binary_search
from node import Node
from graph_search import bfs


list = [-1, 5, 7, 9, 43, 76]


def graphs_operations():
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

    bfs(node_one, node_eight)
    return node_one


def run():
    print(linear_search(list, 43))
    print(linear_search(list, 2))
    print(binary_search(list, 43))
    print(binary_search(list, 2))

    graphs_operations()


if __name__ == '__main__':
    run()
