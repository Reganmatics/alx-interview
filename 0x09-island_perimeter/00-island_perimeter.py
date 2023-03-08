#!/usr/bin/pyhton3
"""
island perimeter calculator
"""


def island_perimeter(grid):
    """
    base calculator for perimeter
    """
    # Check if grid is empty
    if not grid:
        return 0

    # Check if grid is rectangular and within size limits
    height = len(grid)
    width = len(grid[0])
    if not all(len(row) == width for row in grid) or height > 100 \
            or width > 100:
        raise ValueError("Grid is not rectangular or exceeds size limits")

    # Find the first land cell
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                # Use DFS to find the island and its perimeter
                return dfs(i, j, grid)


def dfs(i, j, grid):
    """
    Depth first Search implementation
    """
    # Check if cell is out of bounds or is water
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) \
            or grid[i][j] == 0:
        return 1

    # Check if cell is already visited
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
