#!/usr/bin/python3
""" Rotate 2d Matrix Algo """


def rotate_2d_matrix(matrix: list):
    """ Rotates a 2D matrix 90 degrees clockwise """
    size = len(matrix)

    rotated_matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            rotated_matrix[i][j] = matrix[size - 1 - j][i]

    for i in range(size):
        for j in range(size):
            matrix[i][j] = rotated_matrix[i][j]
