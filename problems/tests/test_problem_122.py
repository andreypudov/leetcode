import unittest

from problems.problem_122 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_climbStairs(self):
        self.assertEqual(
            self.solution.maxProfit([7, 1, 4, 5, 3, 4, 5, 6, 5, 4]), 7
        )  # 5-1=4, 6-3=3
        self.assertEqual(
            self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 7
        )  # 5-1=4, 6-3=3
        self.assertEqual(self.solution.maxProfit([1, 2, 3, 4, 5]), 4)  # 5-1=4
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)  #
        self.assertEqual(self.solution.maxProfit([1, 5]), 4)
        self.assertEqual(self.solution.maxProfit([5, 1]), 0)
        self.assertEqual(self.solution.maxProfit([5]), 0)
        self.assertEqual(self.solution.maxProfit([1, 4, 7, 8, 6, 4]), 7)  # 7
