import unittest

from problems.problem_119 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_getRow(self):
        self.assertEqual(self.solution.getRow(3), [1, 3, 3, 1])
        self.assertEqual(self.solution.getRow(0), [1])
        self.assertEqual(self.solution.getRow(1), [1, 1])
