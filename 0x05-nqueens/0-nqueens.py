#!/usr/bin/python3

import sys

# Main function to solve the N-Queens problem by placing N queens on an NxN board
def solve(row, column):
    # Start with an empty solution list
    solver = [[]]
    # Attempt to place queens row by row
    for q in range(row):
        solver = place_queen(q, column, solver)
    return solver

# Function to place a queen in a row, checking all columns for valid positions
def place_queen(q, column, prev_solver):
    solver_queen = []
    # Iterate over each partial solution from the previous row
    for array in prev_solver:
        # Check each column to see if a queen can be placed without conflicts
        for x in range(column):
            if is_safe(q, x, array):
                solver_queen.append(array + [x])  # Add column position to the solution
    return solver_queen

# Function to check if placing a queen at (q, x) is safe
def is_safe(q, x, array):
    # Check if there's already a queen in the same column
    if x in array:
        return False
    # Check for queens in diagonals by comparing row/column differences
    return all(abs(array[column] - x) != q - column for column in range(q))

# Initialize function to validate and parse command line argument
def init():
    # Ensure the program is run with exactly one argument (N)
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    # Check if the argument is a positive integer
    if sys.argv[1].isdigit():
        the_queen = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    # Check that N is at least 4, as smaller boards don't have solutions
    if the_queen < 4:
        print("N must be at least 4")
        sys.exit(1)
    return the_queen

# Function to execute the N-Queens solution and print formatted output
def n_queens():
    # Parse and validate the input for the number of queens
    the_queen = init()
    # Solve the N-Queens problem for an NxN board
    solver = solve(the_queen, the_queen)
    # Format and print each solution as a list of [row, column] pairs
    for array in solver:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)

# Run the main function if this script is executed directly
if __name__ == '__main__':
    n_queens()
