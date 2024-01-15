#!/usr/bin/python

import unittest

from main import *

class Test(unittest.TestCase):
    def test_basic(self):
        assert "Hello" == hello()

    
    def test_solution(self):
        input = [3, 1, 2, 4, 5]
        output = solution(input)
        assert [12, 3] == output