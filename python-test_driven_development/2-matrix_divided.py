#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): A matrix (list of lists) of integers/floats.
        div (int/float): The divisor.

    Returns:
        list of lists: A new matrix with each element divided by div
        and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if each row of the matrix is not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(all(isinstance(x, (int, float)) for x in row)
                    for row in matrix)):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)

    len_row = len(matrix[0])
    if not all(len(row) == len_row for row in matrix):
        msg2 = "Each row of the matrix must have the same size"
        raise TypeError(msg2)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row]
                  for row in matrix]
    return new_matrix
