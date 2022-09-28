#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    for i in matrix:
        mat.append([j**2 for j in i])
    return mat
