#!/usr/bin/python3

"""
there are n number of locked boxes. Every box is numbered sequentially from 0 to n - 1, and every box contains keys to the other boxes.
Assignement: Writing the method that determines if all boxes can be opened.
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
    
    # Checking if input is a list and ensuring it is non-empty
    if type(boxes) is not list:
        return False  # If not a list, immediately return False
    elif len(boxes) == 0:
        return False  # If list is empty, return False
    
    # Iterating over every box starting from index 1 (box 0 is always open)
    for r in range(1, len(boxes) - 1):
        boxes_checked = False  # Flagging for checking if current box 'r' can be opened
        
        # Looping through all boxes to find a key to box 'r'
        for idx in range(len(boxes)):
            # Checking if current box contains the key to box 'r'
            # Ensuring the box doesn't contain its own key (r != idx)
            boxes_checked = r in boxes[idx] and r != idx
            
            # If a key to box 'r' is found, stop searching
            if boxes_checked:
                break
        
        # If no key was found for box 'r', return False as it cannot be opened
        if not boxes_checked:
            return False
    
    # If all boxes can be opened, return True
    return True
