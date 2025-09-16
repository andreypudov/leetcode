import unittest

from problems.problem_55 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_divide(self):
        self.assertTrue(self.solution.canJump([2, 3, 1, 1, 4]))
        self.assertFalse(self.solution.canJump([3, 2, 1, 0, 4]))
        self.assertTrue(self.solution.canJump([0]))
        self.assertFalse(self.solution.canJump([0, 1]))
        self.assertTrue(self.solution.canJump([2, 0, 0]))
