#!/usr/bin/python3

"""Lock boxes Algorithm"""


def canUnlockAll(boxes):
    """A function that determines if all the boxes can be opened."""
    n = len(boxes)
    visited = [False] * n
    queue = [0]  # Start with the first box (index 0)

    while queue:
        box = queue.pop(0)
        visited[box] = True

        for key in boxes[box]:
            if not visited[key]:
                queue.append(key)

    return all(visited)
