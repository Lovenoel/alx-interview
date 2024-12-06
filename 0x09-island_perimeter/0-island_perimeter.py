#!/usr/bin/python3
"""
Defines a function that calculates the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): 2D grid representation of the island

    Returns:
        int: Perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # If the cell is land
                # Add 4 sides for the land
                perimeter += 4
                # Subtract 2 for each adjacent land cell
                if r > 0 and grid[r - 1][c] == 1:  # Check upward
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:  # Check leftward
                    perimeter -= 2

    return perimeter
