#!/usr/bin/python3
'''Island Perimeter'''

def island_perimeter(grid):

    max_w = 0
    max_h = 0

    # width of the grid
    for a in range(len(grid)):
        width = 0
        for b in range(len(grid[0])):
            width += grid[a][b]
        
        if width > max_w:
            max_w = width
    
    # height of grid
    for c in range(len(grid[0])):
        height = 0
        for d in range(len(grid)):
            height += grid[d][c]

        if height > max_h:
            max_h = height
    
    # calculate and return perimeter
    perimiter = (max_h * 2) + (max_w * 2)
            

    return perimiter