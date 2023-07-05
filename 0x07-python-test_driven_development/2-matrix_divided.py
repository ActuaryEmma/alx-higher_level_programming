#!/usr/bin/python3
"""
no module imported
"""
def matrix_divided(matrix, div):
    """
    method that divided each value in matrix by div if int
    """
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        new_row = []
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix\
                                (list of lists) of integers/floats")
            new_row.append(round(matrix[i][j] / div, 2))
        new_matrix.append(new_row)
    return new_matrix
