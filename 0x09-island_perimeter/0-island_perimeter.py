#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid):
    """Return perimeter of the island described in grid.

    grid is a list of list of integers:
    - 0 represents water
    - 1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes” (water inside that isn’t connected to
    the water surrounding the island).

    Args:
        grid (list of list of int): the grid representing the island

    Returns:
        int: the perimeter of the island
    """
    # Determining number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Initializing the perimeter variable to 0
    perimeter = 0

    # Looping
    for a in range(rows):
        for b in range(cols):
            if grid[a][b] == 1:
                # Check the top edge
                if a == 0 or grid[a-1][b] == 0:
                    perimeter += 1
                # Check the bottom edge
                if a == rows-1 or grid[a+1][b] == 0:
                    perimeter += 1
                # Check the left edge
                if b == 0 or grid[a][b-1] == 0:
                    perimeter += 1
                # Check the right edge
                if b == cols-1 or grid[a][b+1] == 0:
                    perimeter += 1

    # total perimeter
    return perimeter
