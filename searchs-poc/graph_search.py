#!/usr/bin/python
from node import Node

def bfs(root, target):
    queue = []
    root.visited = True
    queue.append(root)

    print('Path:', end=' ')
    while len(queue) != 0:
        node = queue.pop(0)
        print(node.value, ' - ', end=' ')
        if (node.value == target):
            print('')
            return True

        for neighbor in node.connections:
            if (not neighbor.visited):
                neighbor.visited = True
                queue.append(neighbor)

    print('')
    return False
