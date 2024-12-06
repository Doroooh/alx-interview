#!/usr/bin/python3
"""Island perimeter computing module.
This module contains a function that computes the perimeter of an island
represented as a grid. The island is defined as 1s in the grid, and water
is represented as 0s. The grid does not contain any lakes (i.e., water 
inside the island), and the grid is completely surrounded by water.
"""

def island_perimeter(grid):
    """
    Computes the perimeter of an island with no lakes.

    Args:
        grid (list of list of int): A grid where 1 represents land and 0 represents water.
    
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0  # Initialize perimeter counter

    # Check if the input is a valid grid
    if type(grid) != list:
        return 0
    
    r = len(grid)  # Number of rows in the grid
    
    # Iterate through each row and cell in the grid
    for a, row in enumerate(grid):
        s = len(row)  # Number of columns in the current row
        
        for b, cell in enumerate(row):
            if cell == 0:
                # Skip water cells
                continue
            
            # Determine the edges that contribute to the perimeter
            edges = (
                # Top edge: Cell is on the first row or the cell above is water
                a == 0 or (len(grid[a - 1]) > b and grid[a - 1][b] == 0),
                
                # Right edge: Cell is on the last column or the cell to the right is water
                b == s - 1 or (s > b + 1 and row[b + 1] == 0),
                
                # Bottom edge: Cell is on the last row or the cell below is water
                a == r - 1 or (len(grid[a + 1]) > b and grid[a + 1][b] == 0),
                
                # Left edge: Cell is on the first column or the cell to the left is water
                b == 0 or row[b - 1] == 0,
            )
            
            # Add the number of edges that contribute to the perimeter
            perimeter += sum(edges)
    
    return perimeter
