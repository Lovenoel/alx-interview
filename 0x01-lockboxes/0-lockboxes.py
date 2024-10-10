#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes: list of lists, where each inner list represents the keys
               contained in a box.

    Returns:
        True if all boxes can be opened, otherwise False.
    """
    # Track the number of boxes
    num_boxes = len(boxes)
    # Track opened boxes using a set to avoid duplicates
    opened = set([0])  # The first box is always open
    # Use a stack to manage the boxes we need to check
    stack = [0]  # Start with the first box

    # While there are boxes to check in the stack
    while stack:
        # Get a box from the stack
        current_box = stack.pop()

        # Go through all keys in the current box
        for key in boxes[current_box]:
            # If this key opens a box that hasn't been opened yet
            if key not in opened and key < num_boxes:
                # Mark this box as opened
                opened.add(key)
                # Add this box to the stack to check its keys later
                stack.append(key)

    # If the number of opened boxes is equal to the total number of boxes
    return len(opened) == num_boxes
