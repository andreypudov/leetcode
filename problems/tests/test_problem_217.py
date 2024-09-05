import unittest

from problems.problem_217 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_containsDuplicate(self):
        self.assertTrue(self.solution.containsDuplicate([1, 2, 3, 1]))
        self.assertFalse(self.solution.containsDuplicate([1, 2, 3, 4]))
        self.assertTrue(self.solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
