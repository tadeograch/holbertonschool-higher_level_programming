#!/usr/bin/python3
'''Technical interview preparation'''


def find_peak(list_of_integers):
    '''Finds a peak in a list of unsorted integers'''

    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        if(list_of_integers[0] >= list_of_integers[1]):
            return list_of_integers[0]
        else:
            return list_of_integers[1]

    mid = n // 2
    return aux_func(list_of_integers, mid)


def aux_func(list_i, n):
    '''Recursive aux function'''
    if n < 2:
        return list_i[n]

    if list_i[n] < list_i[n - 1]:
        return aux_func(list_i, n // 2)
    elif list_i[n] < list_i[n + 1]:
        return aux_func(list_i, n + (n // 2))
    else:
        return list_i[n]
