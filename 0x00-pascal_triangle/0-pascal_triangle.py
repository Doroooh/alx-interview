#!/usr/bin/python3
"""A module for generating Pascal's Triangle up to a specified number of rows."""

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.
    
    Args:
        n (int): The number of rows to generate.
        
    Returns:
        list: A list of lists where each inner list represents a row in Pascal's Triangle.
    """
    # Return an empty list if the input is less than or equal to zero
    if n <= 0:
        return []

    # Initialize the outer list to hold the rows of Pascal's Triangle
    pascal_t = []

    # Loop through each row index 'i' to build Pascal's Triangle row by row
    for i in range(n):
        # Create a new row and add the number '1' at the start of each row
        pascal_t.append([])
        pascal_t[i].append(1)

        # Fill the current row based on the sum of two numbers from the previous row
        for j in range(1, i):
            # Get the values from the previous row that need to be added
            left_value = pascal_t[i-1][j-1]
            right_value = pascal_t[i-1][j]
            # Append their sum to the current row
            pascal_t[i].append(left_value + right_value)

        # Add '1' at the end of the row for all rows except the first one
        if i != 0:
            pascal_t[i].append(1)

    return pascal_t
