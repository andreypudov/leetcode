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
        self.assertEqual(self.solution.myAtoi("-91283472332"), -2147483648)
        self.assertEqual(self.solution.myAtoi("91283472332"), 2147483647)
        self.assertEqual(self.solution.myAtoi("3.14159"), 3)
        self.assertEqual(self.solution.myAtoi(" "), 0)
        self.assertEqual(self.solution.myAtoi("+-12"), 0)
        self.assertEqual(self.solution.myAtoi("-+12"), 0)
        self.assertEqual(self.solution.myAtoi("00000-42a1234"), 0)
        self.assertEqual(self.solution.myAtoi("   +0 123"), 0)
        self.assertEqual(self.solution.myAtoi("  +  413"), 0)
