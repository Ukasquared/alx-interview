#!/usr/bin/python3
"""pascal triangle"""

def pascal_triangle(n):
    """builds the pascal triangle"""
    if type(n) is not int:
        raise TypeError("type is not an integer")
    if n <= 0:
        return []
    queue = []
    for i in range(n):
        if i == 0:
            queue.append([1])
        if i == 1:
            queue.append([1, 1]) 
        if i > 1:
            prv_list_len = len(queue[i - 1])
            in_list = [queue[i - 1][j] + queue[i - 1][j + 1]
                        for j in range(prv_list_len - 1)]
            in_list.insert(0, 1)
            in_list.append(1)
            queue.append(in_list)
    return queue
