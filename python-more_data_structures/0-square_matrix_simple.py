#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[matrix[i][j] ** 2 for j in range(len(matrix[0]))]
                  for i in range(len(matrix))]
    return new_matrix
