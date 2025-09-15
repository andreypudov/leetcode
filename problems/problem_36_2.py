# 36. Valid Sudoku
#
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
#
#     - Each row must contain the digits 1-9 without repetition.
#     - Each column must contain the digits 1-9 without repetition.
#     - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits
#       1-9 without repetition.
#
# Note:
#
#     - A Sudoku board (partially filled) could be valid but is not
#       necessarily solvable.
#     - Only the filled cells need to be validated according to the
#       mentioned rules.

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_list(numbers: List[str]) -> bool:
            numbers_filtered = [n for n in numbers if n != "."]
            return len(set(numbers_filtered)) == len(numbers_filtered)

        for row in board:
            if not is_valid_list(row):
                return False

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                block_numbers = [row[i : i + 3] for row in board[j : j + 3]]
                flattened = [n for row in block_numbers for n in row]
                if not is_valid_list(flattened):
                    return False

        transposed = list(map(list, zip(*board)))
        for row in transposed:
            if not is_valid_list(row):
                return False

        return True
