import unittest
from typing import List

from problems.helpers.list import ListHelper
from problems.problem_141 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_hasCycle(self):
        self.assertTrue(self.hasCycle([3, 2, 0, -4], 1))
        self.assertTrue(self.hasCycle([1, 2], 0))
        self.assertFalse(self.hasCycle([1], -1))
        self.assertFalse(self.hasCycle([1, 2], -1))
        self.assertFalse(
            self.hasCycle(
                [
                    -21,
                    10,
                    17,
                    8,
                    4,
                    26,
                    5,
                    35,
                    33,
                    -7,
                    -16,
                    27,
                    -12,
                    6,
                    29,
                    -12,
                    5,
                    9,
                    20,
                    14,
                    14,
                    2,
                    13,
                    -24,
                    21,
                    23,
                    -21,
                    5,
                ],
                -1,
            )
        )

    def hasCycle(self, head: List[int], pos: int):
        helper = ListHelper()

        head = helper.make_list_with_cycle(head, pos)

        return self.solution.hasCycle(head)
