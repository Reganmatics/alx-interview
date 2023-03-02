#!/usr/bin/pyhton3
"""
island perimeter calculator
"""


def island_perimeter(grid):
    """
    compute the perimeter of island in grid
    """

    height = len(grid)
    width = len(grid[0])
    count = 0
    for row in grid:
        count += row.count(1)
    perimeter = 2 * (count + 1)

    return perimeter
