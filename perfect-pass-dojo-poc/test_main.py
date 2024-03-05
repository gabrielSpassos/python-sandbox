#!/usr/bin/python

import unittest

from main import *

class Test(unittest.TestCase):    
    def test_should_return_false_for_password_size(self):
        password = "abcde"
        assert False == is_perfect_password(password)

    def test_should_return_false_for_invalid_bang_character(self):
        password = "abcdefghijklmnopqrstuvxywz01234!"
        assert False == is_perfect_password(password)

    def test_should_return_false_for_invalid_underscore_character(self):
        password = "abcdefghijklmnopqrstuvxywz01234_"
        assert False == is_perfect_password(password)

    def test_should_return_false_for_not_enough_capital_letters(self):
        password = "abcdefghijklmnopqrstuvxywz012345"
        assert False == is_perfect_password(password)

    def test_should_return_false_for_not_enough_numbers(self):
        password = "ABcdefghijklmnopqrstuvxywzabcdef"
        assert False == is_perfect_password(password)

    def test_should_return_false_for_not_enough_special_chars(self):
        password = "ABcdefghij-$#nopqrstuvxywz01abcd"
        assert False == is_perfect_password(password)

    def test_should_return_false_for_not_unique_chars(self):
        password = "aaaabsbdSGhdjjdsgdgdsghshd$*24ds"
        assert False == is_perfect_password(password)
    
    def test_should_return_true(self):
        password = "ABcdefghijklmnopqrstuvxywz01$*24"
        assert True == is_perfect_password(password)