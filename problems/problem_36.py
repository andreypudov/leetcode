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

from array import array
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        def is_unique(numbers: memoryview) -> bool:
            mask = 0
            for n in numbers:
                if n == 0:
                    continue
                bit = 1 << n
                if mask & bit:
                    return False
                mask |= bit
            return True

        def row(i: int, mv: memoryview) -> memoryview:
            return mv[i * N : (i + 1) * N]

        def col(j: int, mv: memoryview) -> memoryview:
            return mv[j : N * N : N]

        def block(r: int, c: int, mv: memoryview) -> memoryview:
            start_row = r * 3
            start_col = c * 3
            for dr in range(3):
                row_start = (start_row + dr) * N + start_col
                row_view = mv[row_start : row_start + 3]
                for x in row_view:
                    yield x

        flat = [0 if ch == "." else int(ch) for row in board for ch in row]
        buffer = array("b", flat)
        mem_view = memoryview(buffer)

        for index in range(0, 9):
            if not is_unique(row(index, mem_view)):
                return False

            if not is_unique(col(index, mem_view)):
                return False

        for r in range(0, 3):
            for c in range(0, 3):
                if not is_unique(block(r, c, mem_view)):
                    return False

        return True
