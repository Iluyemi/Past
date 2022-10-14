#!/usr/bin/python3

def matrix_divided(matrix, div):
    for i in matrix:
        for j in i:
            try:
                j = int(j)
            except TypeError:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats)

