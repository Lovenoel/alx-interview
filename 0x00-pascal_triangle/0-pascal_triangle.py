"""
A module of a function def pascal_triangle(n): that returns a 
list of lists of integers representing the Pascal’s triangle of n:
Returns an empty list if n <= 0
"""

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n.
    
    Args:
    n (int): Number of rows of the triangle.
    
    Returns:
    List of lists: Pascal's triangle up to n rows.
    """
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Generate each row based on the previous row
    for i in range(1, n):
        prev_row = triangle[-1]  # Last row in the triangle
        new_row = [1]  # Start the new row with 1
        # Calculate the middle values for the new row
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # End the new row with 1
        triangle.append(new_row)
    
    return triangle
