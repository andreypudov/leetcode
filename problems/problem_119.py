# 119. Pascal's Triangle II
#
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the
# Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [1]
        for _ in range(rowIndex):
            answer = self.nextPascalRow(answer)
        return answer

    def nextPascalRow(self, row: List[int]) -> List[int]:
        return [1] + [row[i] + row[1 + i] for i in range(len(row) - 1)] + [1]
