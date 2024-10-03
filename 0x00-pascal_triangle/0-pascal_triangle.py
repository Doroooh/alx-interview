#!/usr/bin/python3
"""Pascal Triangle"""

#!/usr/bin/python3
"""A module for generating Pascal's Triangle up to a specified number of rows."""

def pascal_triangle(n):
    """
    Generating Pascal's Triangle up to n rows.
    
    Args:
        n (int): Number of rows to generate.
        
    Returns:
        list: A list of lists where each inner list represents a row in Pascal's Triangle.
    """
    # Return an empty list if input is less than or equal to zero
    if n <= 0:
        return []

    # Initializing outer list to hold rows of Pascal's Triangle
    pascal_t = []

    # Looping through every row index 'r' to build Pascal's Triangle row by row
    for r in range(n):
        # Creating a new row and add the number '1' at the start of each row
        pascal_t.append([])
        pascal_t[r].append(1)

        # Filling the current row based on the sum of two numbers from the previous row
        for m in range(1, r):
            # Get the values from the previous row that need to be added
            left_value = pascal_t[r-1][m-1]
            right_value = pascal_t[r-1][m]
            # Append their sum to the current row
            pascal_t[r].append(left_value + right_value)

        # Add '1' at the end of the row for all rows except the first one
        if r != 0:
            pascal_t[r].append(1)

    return pascal_t
