#!/usr/bin/python3
'''Island Perimeter'''


def island_perimeter(grid):
    '''Island perimeter documentaion'''
    hi = [None, 0]
    wi = [None, 0]

    # width of the grid
    for a in range(len(grid)):
        for b in range(len(grid[0])):

            if wi[0] == None and grid[a][b] == 1:
                wi[0] = b
            elif wi[0] is not None and b < wi[0] and grid[a][b] == 1:
                wi[0] = b
            
            if b > wi[1] and grid[a][b] == 1:
                wi[1] = b


    # height of grid
    for c in range(len(grid[0])):
        for d in range(len(grid)):

            if hi[0] == None and grid[d][c] == 1:
                hi[0] = d
            elif hi[0] is not None and d < hi[0] and grid[d][c] == 1:
                hi[0] = d
            
            if d > hi[1] and grid[d][c] == 1:
                hi[1] = d


    # calculate width and height
    height = (hi[1] - hi[0]) + 1
    width = (wi[1] - wi[0]) + 1

    # calculate perimeter
    perimeter = height * 2 + width * 2

    return perimeter