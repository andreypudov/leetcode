import unittest
from typing import Optional

from problems.core.list import ListNode
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

    def getIntersectionNode(self, headA: [int], headB: [int], expected: [int]):
        helper = ListHelper()

        headA = helper.makeList(headA)
        headB = helper.makeList(headB)

        expected = helper.makeList(expected)
        actual = self.solution.getIntersectionNode(headA, headB)

        assert helper.compareList(expected, actual)


if __name__ == "__main__":
    unittest.main()
