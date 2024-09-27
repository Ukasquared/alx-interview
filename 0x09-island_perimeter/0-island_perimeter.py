#!/usr/bin/python3
""" island perimeter """


def island_perimeter(grid):
    """island perimeter
    module """
    total_peri = 0
    grid_len = len(grid)
    for i in range(grid_len):
        row_len = len(grid[i])
        for j in range(row_len):
            if grid[i][j] == 1:
                total_peri += 4
                if i > 0 and grid[i - 1][j] == 1:
                    total_peri -= 1
                if i < grid_len - 2 and grid[i + 1][j] == 1:
                    total_peri -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    total_peri -= 1
                if j < row_len -2 and grid[i][j + 1] == 1:
                    total_peri -= 1
    return total_peri    
