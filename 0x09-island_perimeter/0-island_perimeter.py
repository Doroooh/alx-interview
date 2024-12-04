#!/usr/bin/python3
"""0x1C. Island Perimeter, task 0. Island Perimeter

This module defines a function that calculates the perimeter of an "island"
represented by a grid of 1s surrounded by water represented by 0s.

"""

def island_perimeter(grid):
    """Calculate the perimeter of an island in a 2D grid.

    Given a 2D grid where 1s represent land and 0s represent water, this function 
    calculates the total perimeter of the contiguous landmass (island). The perimeter 
    is determined by counting the exposed edges of the 1s where they are adjacent 
    to water (0s) or the edge of the grid.

    Args:
        grid (list of lists of ints): 2D list representation of the island, where
                                      1 indicates land and 0 indicates water.

    Returns:
        int: The perimeter of the island, calculated as the number of edges of 1s
             that are adjacent to 0s or the grid boundaries.

    """
    # Initialize perimeter counter to 0
    perimeter = 0
    
    # Iterate through each cell in the grid (y is the row index, x is the column index)
    for s in range(len(grid)):
        for t in range(len(grid[0])):
            
            # Check if the current cell is land (1)
            if grid[s][t]:
                
                # Check if the left neighbor is water or if we're at the left edge
                if t == 0 or not grid[s][t - 1]:
                    perimeter += 1  # Add to perimeter if left neighbor is water or boundary
                
                # Check if the right neighbor is water or if we're at the right edge
                if t == len(grid[0]) - 1 or not grid[s][t + 1]:
                    perimeter += 1  # Add to perimeter if right neighbor is water or boundary
                
                # Check if the top neighbor is water or if we're at the top edge
                if s == 0 or not grid[s - 1][t]:
                    perimeter += 1  # Add to perimeter if top neighbor is water or boundary
                
                # Check if the bottom neighbor is water or if we're at the bottom edge
                if s == len(grid) - 1 or not grid[s + 1][t]:
                    perimeter += 1  # Add to perimeter if bottom neighbor is water or boundary
    
    # Return the total perimeter of the island
    return perimeter
