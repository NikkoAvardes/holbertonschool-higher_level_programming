#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print()
        for j in i:
            print("{}".format(j), end=' ')
    print()
