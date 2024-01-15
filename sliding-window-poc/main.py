#!/usr/bin/python


def get_max_window_sum(array, window_size):
    array_size = len(array)
    if (array_size < window_size):
        print("Invalid window size", window_size, "for array", array)
        return -1

    # slice the initial array with the length of window_size
    sub_array = array[:window_size]
    window_sum = sum(sub_array)

    max_sum = window_sum
    for i in range(array_size - window_size):
        window_sum = window_sum - array[i] + array[i + window_size]
        max_sum = max(window_sum, max_sum)
    
    return max_sum


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_max_window_sum(array, 3))