#!/usr/bin/python

def is_perfect_password(password):
    count_capital = 0
    count_number = 0
    count_special = 0

    if len(password) != 32:
        print("Invalid password size")
        return False

    if '!' in password:
        print("Invalid ! char")
        return False

    if '_' in password:
        print("Invalid _ char")
        return False

    for c in password:
        if c.isupper():
            count_capital += 1
        
        if c.isnumeric():
            count_number += 1

        if c == "#" or c == "*" or c == "-" or c == "$":
            count_special += 1 

    if count_capital < 2:
        print("Invalid count of capital letters", count_capital)
        return False

    if count_number < 2:
        print("Invalid count of numbers", count_number)
        return False

    if count_special != 2:
        print("Invalid count of special chars", count_special)
        return False

    return get_longest_unique_chars_count(password) >= 26


def get_longest_unique_chars_count(password):
    string_indexes_set = set(list(range(len(password))))
    char_set = set()
    left = 0
    result = 0

    for right in string_indexes_set:
        while password[right] in char_set:
            char_set.remove(password[right])
            left += 1

        char_set.add(password[right])
        result = max(result, right - left + 1)

    return result