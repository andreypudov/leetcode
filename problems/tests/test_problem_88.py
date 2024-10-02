import unittest
from typing import List

from problems.problem_88 import Solution as Solution1
from problems.problem_88_2 import Solution as Solution2
from problems.protocols.problem_88 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution_1 = Solution1()
        self.solution_2 = Solution2()

    def test_merge(self):
        for solution in [self.solution_1, self.solution_2]:
            self.__merge(
                solution,
                [1, 2, 3, 0, 0, 0],
                3,
                [2, 5, 6],
                3,
                [1, 2, 2, 3, 5, 6],
            )
            self.__merge(solution, [1], 1, [], 0, [1])
            self.__merge(solution, [0], 0, [1], 1, [1])
            self.__merge(
                solution,
                [2, 5, 6, 0, 0, 0],
                3,
                [1, 2, 3],
                3,
                [1, 2, 2, 3, 5, 6],
            )

    def __merge(
        self,
        solution: Solution,
        nums1: List[int],
        m: int,
        nums2: List[int],
        n: int,
        expected: List[int],
    ):
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)
