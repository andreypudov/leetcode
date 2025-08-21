import unittest

from problems.problem_167 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_twoSum(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [1, 2])
        self.assertEqual(self.solution.twoSum([2, 3, 4], 6), [1, 3])
        self.assertEqual(self.solution.twoSum([-1, 0], -1), [1, 2])
