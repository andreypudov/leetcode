import unittest

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

    def reverseList(self, head: [int], expected: [int]):
        helper = ListHelper()

        head = helper.makeList(head)
        expected = helper.makeList(expected)
        actual = self.solution.reverseList(head)

        assert helper.compareList(expected, actual)


if __name__ == "__main__":
    unittest.main()
