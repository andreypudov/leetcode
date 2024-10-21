import unittest
from typing import List

from problems.problem_26 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_removeDuplicates(self):
        self.__removeDuplicates([1, 1, 2], [1, 2, 2], 2)
        self.__removeDuplicates(
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4, 2, 2, 3, 3, 4], 5
        )
        self.__removeDuplicates([], [], 0)
        self.__removeDuplicates([1], [1], 1)
        self.__removeDuplicates([1, 1], [1, 1], 1)
        self.__removeDuplicates([1, 2], [1, 2], 2)

    def __removeDuplicates(
        self, nums: List[int], expected_nums: List[int], expected_k: int
    ) -> None:
        k = self.solution.removeDuplicates(nums)

        self.assertEqual(k, expected_k)
        self.assertEqual(nums, expected_nums)
