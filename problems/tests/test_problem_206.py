import unittest
from typing import List

from problems.helpers.list import ListHelper
from problems.problem_206 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_reverseList(self):
        self.reverseList([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
        self.reverseList([1, 2], [2, 1])
        self.reverseList([], [])

    def reverseList(self, head: List[int], expected: List[int]):
        helper = ListHelper()

        head = helper.make_list(head)
        expected = helper.make_list(expected)
        actual = self.solution.reverseList(head)

        self.assertTrue(helper.compare_lists(expected, actual))
