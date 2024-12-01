import unittest

from problems.problem_392 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_isSubsequence(self):
        self.assertTrue(self.solution.isSubsequence("abc", "ahbgdc"))
        self.assertFalse(self.solution.isSubsequence("axc", "ahbgdc"))
