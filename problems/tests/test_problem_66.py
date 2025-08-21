import unittest

from problems.problem_66 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_plusOne(self):
        self.assertEqual(self.solution.plusOne([1, 2, 3]), [1, 2, 4])
        self.assertEqual(self.solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
        self.assertEqual(self.solution.plusOne([9]), [1, 0])
        self.assertEqual(self.solution.plusOne([9, 9]), [1, 0, 0])
