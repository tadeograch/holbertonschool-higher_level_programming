#!/usr/bin/python3
'''Technical interview preparation'''


def find_peak(list_of_integers):
    '''Finds a peak in a list of unsorted integers'''

    n = len(list_of_integers)
    if n == 0:
        return None
    half = int(n / 2)
    if list_of_integers[half] < list_of_integers[half - 1]:
        for i in range(1, half):
            if list_of_integers[i] >= list_of_integers[i - 1]:
                if list_of_integers[i] >= list_of_integers[i + 1]:
                    return list_of_integers[i]
    elif list_of_integers[half] < list_of_integers[half + 1]:
        for i in range(half + 1, n):
            if list_of_integers[i] >= list_of_integers[i - 1]:
                if list_of_integers[i] >= list_of_integers[i + 1]:
                    return list_of_integers[i]
    else:
        return list_of_integers[half]
