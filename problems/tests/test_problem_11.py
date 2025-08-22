import unittest

from problems.problem_11 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_maxArea(self):
        # self.assertEqual(self.solution.maxArea([1,8,6,2,5,4,8,3,7]), 49)
        # self.assertEqual(self.solution.maxArea([1,1]), 1)
        self.assertEqual(self.solution.maxArea([1, 0, 0, 0, 0, 0, 0, 2, 2]), 8)
        # self.assertEqual(self.solution.maxArea([4,3,2,1,4]), 16)
