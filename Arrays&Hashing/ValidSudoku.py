# https://leetcode.com/problems/valid-sudoku/

import collections


def isValidSudoku(board):

    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    boxes = collections.defaultdict(set)  # r/3, c/3

    for r in range(9):
        for c in range(9):
            # check if it is empty or not
            if board[r][c] == ".":
                continue
            # check if it is duplicated in row or column or matrix
            if (
                board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in boxes[(r // 3), (c // 3)]
            ):
                return False
            # add to row, column and matrix

            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            boxes[(r // 3), (c // 3)].add(board[r][c])
    return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(isValidSudoku(board))
