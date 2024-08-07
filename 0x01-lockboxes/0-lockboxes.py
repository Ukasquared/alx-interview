#!/usr/bin/env python3
"""check if all boxes
can be opened"""
from collections import deque


def canUnlockAll(boxes: list) -> bool:
    """returns true if all
    boxes can be opened
    otherwise false
    Each boxes(index) reps the node
    and has a list with reps
    the keys(edges)"""
    start = 0
    visited = set()
    queue = deque([start])
    while len(queue) != 0:
        vertex = queue.popleft()
        visited.add(vertex)
        conn_vertex = boxes[vertex]
        if len(conn_vertex) != 0:
            for key in conn_vertex:
                if key < len(boxes):
                    if key not in visited:
                        queue.append(key)
    if len(visited) == len(boxes):
        return True
    return False
