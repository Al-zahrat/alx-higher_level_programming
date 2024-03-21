#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    i = []
    s = []
    for i in matrix:
        s.append(list(map(lambda x: x * x, i)))
    return s
