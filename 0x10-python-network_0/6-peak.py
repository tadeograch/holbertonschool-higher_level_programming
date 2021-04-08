#!/usr/bin/python3
'''Technical interview preparation'''


def find_peak(list_of_integers):
    '''Finds a peak in a list of unsorted integers'''

    list_length = len(list_of_integers)
    if list_length == 0:
        return None
    if list_length < 2:
        return None

    for i in range(1, list_length - 1):
        if list_of_integers[i] >= list_of_integers[i - 1]:
            if list_of_integers[i] >= list_of_integers[i + 1]:
                return list_of_integers[i]
