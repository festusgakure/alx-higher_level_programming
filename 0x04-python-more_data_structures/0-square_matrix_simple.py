#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    #Create an empty array of the same size as matrix
    rows = len(matrix)
    col = len(matrix[0])
    new_matrix = [[0 for _ in range(col)] for _ in range(rows)]

    for i in range(rows):
        for j in range(len(matrix[i])):
            new_matrix[i][j]=matrix[i][j]**2
    return new_matrix
