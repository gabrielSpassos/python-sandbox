#!/usr/bin/python
import math

"""
Linear search implementation
@param array: list to search
@param target: target value to search
@return: the index of the target element or -1 if don't found the element
"""
def linear_search(array, target):
    for index, value in enumerate(array):
        if value == target:
            return index
        
    return -1


"""
Binary search implementation
@param array: list to search
@param target: target value to search
@return: the index of the target element or -1 if don't found the element
"""
def binary_search(array, target):
    head = 0
    tail = len(array) - 1

    while (head <= tail):
        mid = math.floor((head + tail) / 2)
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            tail = mid - 1
        else:
            head = mid + 1

    return -1