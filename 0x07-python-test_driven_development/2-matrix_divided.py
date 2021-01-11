#!/usr/bin/python3

"""
1. Divide a matrix
A function that divides all elements of a matrix
matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    """
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    length_error = "Each row of the matrix must have the same size"
    if not isinstance(matrix, list) or len(matrix) < 2:
        raise TypeError(matrix_error)
    elif not isinstance(matrix[0], list):
        raise TypeError(matrix_error)
    else:
        lenght = len(matrix[0])
        for item in matrix:
            if lenght != len(item):
                raise TypeError(length_error)
            if not isinstance(item, list):
                raise TypeError(matrix_error)
            else:
                for value in item:
                    if not isinstance(value, (int, float)):
                        raise TypeError(matrix_error)

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = []
    index = 0
    for l in matrix:
        new_in = []
        new.append(new_in)
        for m in range(0, len(l)):
            new_in.append(round(l[m] / div, 2))
    return (new)
