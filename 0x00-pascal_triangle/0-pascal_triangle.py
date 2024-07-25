#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    
    pascal = []

    for i in range(n):
        row = [1]

        if i > 0:
            for j in range(i):
                row.append(pascal[i-1][j-1] + pascal[i-1][j])

            row.append(1)

        pascal.append(row)

    return pascal