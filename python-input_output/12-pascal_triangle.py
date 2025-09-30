#!/usr/bin/python3
"""Module for generating Pascal's triangle.

This module provides functionality to generate Pascal's triangle up to a
specified number of rows, returning the triangle as a list of lists where
each inner list represents a row of the triangle.
"""


def pascal_triangle(n):
    """Generate Pascal's triangle with n rows.

    Pascal's triangle is a triangular array of numbers where each number is
    the sum of the two numbers directly above it. The triangle starts with
    1 at the top, and each row begins and ends with 1.

    Args:
        n (int): The number of rows to generate. Must be an integer.
                If n <= 0, returns an empty list.

    Returns:
        list: A list of lists representing Pascal's triangle.
             Each inner list contains the integers for that row.
             Returns empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]

        if i > 0:
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)

        triangle.append(row)

    return triangle
