import unittest

from problems.helpers.list import ListHelper
from problems.problem_160 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_getIntersectionNode(self):
        self.getIntersectionNode([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], [1, 8, 4, 5])
        self.getIntersectionNode([1, 9, 1, 2, 4], [3, 2, 4], [2, 4])
        self.getIntersectionNode([2, 6, 4], [1, 5], [])

    def getIntersectionNode(
        self, head_a: list[int], head_b: list[int], expected: list[int]
    ):
        helper = ListHelper()

        head_a = helper.make_list(head_a)
        head_b = helper.make_list(head_b)

        expected = helper.make_list(expected)
        actual = self.solution.getIntersectionNode(head_a, head_b)

        assert helper.compare_lists(expected, actual)
