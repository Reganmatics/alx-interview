#!/usr/bin/pyhton3
"""
island perimeter calculator
"""


def island_perimeter(grid):
    # Find the first land cell
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Use DFS to find the island and its perimeter
                return dfs(i, j, grid)


def dfs(i, j, grid):
    # Base case: cell is out of bounds or is water
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) \
            or grid[i][j] == 0:
        return 1
    # Base case: cell is already visited
    if grid[i][j] == -1:
        return 0

    # Mark cell as visited
    grid[i][j] = -1

    # Recursively visit neighboring cells
    perimeter = dfs(i+1, j, grid)
    perimeter += dfs(i-1, j, grid)
    perimeter += dfs(i, j+1, grid)
    perimeter += dfs(i, j-1, grid)

    # Return the perimeter contribution of this cell
    return perimeter
