#!/usr/bin/python3

"""
Problem: You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
         and each box may contain keys to the other boxes.
Task: Writing method that will determine if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Function to determine if all the boxes can be opened.
    
    Arguments:
    boxes: A list of lists where each inner list represents a box, 
           and contains keys to other boxes.

    Returns:
    True if all boxes can be opened, False otherwise.
    """
    # Check if input is a list and not empty
    if type(boxes) is not list:
        return False
    elif len(boxes) == 0:
        return False

    # Iterate through each box starting from the second box (index 1)
    for k in range(1, len(boxes) - 1):
        boxes_checked = False  # Flag to check if the current box k can be opened

        # Iterate through all boxes to find if any box contains the key to box k
        for idx in range(len(boxes)):
            # Check if box k's key is in another box and it's not the same box
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break  # If box k can be opened, exit the inner loop

        # If no box contains the key to box k, return False
        if not boxes_checked:
            return False

    # If all boxes can be opened, return True
    return True
