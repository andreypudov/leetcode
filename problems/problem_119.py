# 119. Pascal's Triangle II
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # row_0 = [1]
        # row_1 = [1, 1]
        # row_2 = [1, 2, 1]
        # row_3 = [1, 3, 3, 1]
        # row_4 = [1, 4, 6, 4, 1]
        # row_5 = [1, 5, 10, 10, 5, 1]
        # row_6 = [1, 6, 15, 20, 15, 6, 1]
        # row_7 = [1, 7, 21, 35, 35, 21, 7, 1]
        # row_8 = [1, 8, 28, 56, 70, 56, 28, 8, 1]

        answer = [1]
        for _ in range(rowIndex):
            answer = self.nextPascalRow(answer)
        return answer

    def nextPascalRow(self, row: list[int]) -> list[int]:
        return [1] + [row[i]+row[1+i] for i in range(len(row) - 1)] + [1]
