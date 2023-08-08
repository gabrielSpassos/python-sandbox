#!/usr/bin/python
import unittest

from array_search import *

class Test(unittest.TestCase):
    array = [5, 14, 56, 128, 873, 1000, 43443, 54321, 477543, 2727373]
    

    def test_linear_search(self):
        assert 4 == linear_search(self.array, 873)
        assert -1 == linear_search(self.array, 999)

    
    def test_binary_search(self):
        assert 4 == binary_search(self.array, 873)
        assert -1 == binary_search(self.array, 999)
