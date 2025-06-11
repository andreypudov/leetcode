import unittest

from problems.problem_121 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_climbStairs(self):
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)
        self.assertEqual(self.solution.maxProfit([8, 2, 4, 1, 5, 8]), 7)
        self.assertEqual(self.solution.maxProfit([5, 10, 1, 2]), 5)
