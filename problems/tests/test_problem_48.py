import unittest
from typing import List

from problems.problem_48 import Solution as Solution1
from problems.problem_48_2 import Solution as Solution2


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution_1 = Solution1()
        self.solution_2 = Solution2()

    def test_rotate(self):
        for solution in [self.solution_1, self.solution_2]:
            self.__rotate(
                solution,
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
            )
            self.__rotate(
                solution,
                [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
                [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
            )

    def __rotate(
        self, solution, matrix: List[List[int]], expected: List[List[int]]
    ):
        solution.rotate(matrix)
        self.assertEqual(matrix, expected)
