#!/usr/bin/python3
'''Rotate 2D Matrix'''

def rotate_2d_matrix(matrix):
    '''Rotates a 2D matrix'''
    rows = len(matrix)

    arr = [[] for j in range(rows)]

    # rotate matrix
    for a in range(len(matrix[-1])):
        for b in range(len(matrix) - 1, -1, -1):
            arr[a].append(matrix[b][a])

    # assign values to original matrix
    for z in range(len(arr)):
        for c in range(len(arr)):
            matrix[z][c] = arr[z][c]