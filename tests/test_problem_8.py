import unittest

from problems.problem_8 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_findMedianSortedArrays(self):
        self.assertEqual(self.solution.myAtoi("42"), 42)
        self.assertEqual(self.solution.myAtoi("   -42"), -42)
        self.assertEqual(self.solution.myAtoi(" -042"), -42)
        self.assertEqual(self.solution.myAtoi("1337c0d3"), 1337)
        self.assertEqual(self.solution.myAtoi("0-1"), 0)
        self.assertEqual(self.solution.myAtoi("words and 987"), 0)
        self.assertEqual(self.solution.myAtoi("4193 with words"), 4193)
