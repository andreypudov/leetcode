import unittest
from typing import List

from problems.problem_27 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_removeElement(self):
        self.__removeElement([3, 2, 2, 3], 3, [2, 2, 2, 3], 2)
        self.__removeElement(
            [0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4, 0, 4, 2], 5
        )
        self.__removeElement([], 0, [], 0)
        self.__removeElement([1], 1, [1], 0)

    def __removeElement(
        self,
        nums: List[int],
        val: int,
        expected_nums: List[int],
        expected_k: int,
    ) -> None:
        k = self.solution.removeElement(nums, val)

        self.assertEqual(k, expected_k)
        self.assertEqual(nums, expected_nums)
