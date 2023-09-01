#!/usr/bin/python3
""" N queens puzzle Algorithm """
import sys


def is_safe(board, row, col, N):
    """ Checks if it's safe to place a queen at the given row
        and column on the board of size NxN."""
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True


def solve_nqueens(N):
    """ Solves the N Queens problem for a given board size NxN. """
    def backtrack(col):
        """ Recursively explores all possible placements of
            queens on the board. """
        nonlocal solutions
        if col == N:
            solutions.append([row[:] for row in board])
            return
        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1
                backtrack(col + 1)
                board[i][col] = 0

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    backtrack(0)

    for solution in solutions:
        print(solution)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solve_nqueens(N)
