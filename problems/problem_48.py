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

        width = len(matrix)
        levels = width // 2

        for level in range(levels):
            limit = width - level - 1

            for rotation in range(level, limit):
                left_top = matrix[level][rotation]
                right_top = matrix[rotation][limit]
                right_bottom = matrix[limit][width - rotation - 1]
                left_bottom = matrix[width - rotation - 1][level]

                matrix[level][rotation] = left_bottom
                matrix[rotation][limit] = left_top
                matrix[limit][width - rotation - 1] = right_top
                matrix[width - rotation - 1][level] = right_bottom
