#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    mat=[]
    new = lambda x: x**2
    for i in matrix:
             mat.append([j**2 for j in i])
    return mat
