#!/usr/bin/python

def hello():
    return "Hello"


def solution(input):
    min_value = 9999999
    max_value = 0
    left = 0
    right = len(input) - 1

    while left < right:
        area = (right - left) * min(input[left], input[right])
        max_value = max(max_value, area)
        min_value = min(min_value, area)

        if input[left] < input[right]:
            left += 1
        else:
            right -= 1

    return [max_value, min_value]
