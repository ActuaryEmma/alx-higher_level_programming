#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        square_row = []
        for i in row:
            square_row.append(i * i)
        result.append(square_row)
    return (result)
