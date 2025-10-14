import unittest

from problems.problem_45 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_jump(self):
        self.assertEqual(self.solution.jump([2, 3, 1, 1, 4]), 2)
        self.assertEqual(self.solution.jump([2, 3, 0, 1, 4]), 2)
        self.assertEqual(self.solution.jump([4, 1, 1, 3, 1, 1, 1]), 2)
        self.assertEqual(self.solution.jump([2, 1, 1, 1, 1]), 3)
        self.assertEqual(self.solution.jump([2, 3, 0, 1, 4]), 2)
        self.assertEqual(self.solution.jump([2, 3, 1, 1, 4]), 2)
        # self.assertEqual(self.solution.jump([0]), _)
        # self.assertEqual(self.solution.jump([1]), _)
        self.assertEqual(self.solution.jump([3, 2, 1]), 1)
        # [2,2,0,1,1,4]
        # [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
        # [10,9,8,7,6,5,4,3,2,1,1,0]
