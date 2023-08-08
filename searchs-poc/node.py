#!/usr/bin/python

class Node:
    def __init__(self, value, connections, visited=False):
        self.value = value
        self.connections = connections
        self.visited = visited


    def to_string(self):
        connections_to_string = list(map(lambda connection_node: connection_node.to_string(), self.connections))
        result = f'Node: {self.value}. Visited: {self.visited}. Connections: {connections_to_string}'
        return str(result)


    #Getter
    @property
    def value(self):
        return self._value

    
    #Setter
    @value.setter
    def value(self, value):
        self._value = value


    #Getter
    @property
    def connections(self):
        return self._connections

    
    #Setter
    @connections.setter
    def connections(self, connections):
        self._connections = connections

    
    #Getter
    @property
    def visited(self):
        return self._visited


    #Setter
    @visited.setter
    def visited(self, visited):
        self._visited = visited
