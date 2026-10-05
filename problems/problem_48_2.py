# 48. Rotate Image
#
# You are given an n x n 2D matrix representing an image, rotate the image by
# 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        self.__transpose(matrix)
        self.__reverse(matrix)

    def __transpose(selgf, matrix: List[List[int]]):
        # we assume matrix is NxN
        rows = len(matrix)

        for row in range(0, rows):
            for column in range(row + 1, rows):
                buffer = matrix[row][column]
                matrix[row][column] = matrix[column][row]
                matrix[column][row] = buffer

    def __reverse(selgf, matrix: List[List[int]]):
        rows = len(matrix)

        for row in range(0, rows):
            matrix[row].reverse()
