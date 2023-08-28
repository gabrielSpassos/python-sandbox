#!/usr/bin/python
from node import Node

def bfs(root, target):
    queue = []
    root.visited = True
    queue.append(root)

    print('BFS Path:', end=' ')
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


def dfs(root, target):
    visited = []

    def interative_dfs(root, target, visited):
        visited.append(root)
        non_visited = [root]
        print('DFS Path:', end=' ')
        while len(non_visited) != 0:
            node = non_visited.pop();
            print(node.value, ' - ', end=' ')
            if (node.value == target):
                print('')
                return True

            for neighbor in node.connections:
                if (neighbor not in visited):
                    visited.append(neighbor)
                    non_visited.append(neighbor) 

        print('')
        return False

    return interative_dfs(root, target, visited)
