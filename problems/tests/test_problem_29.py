import unittest

from problems.problem_29 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_divide(self):
        self.assertEqual(self.solution.divide(10, 3), 3)
        self.assertEqual(self.solution.divide(7, -3), -2)

        self.assertEqual(self.solution.divide(-1, 1), -1)
        self.assertEqual(self.solution.divide(1, -1), -1)
        self.assertEqual(self.solution.divide(-1, -1), 1)

        self.assertEqual(self.solution.divide(7, 2), 3)
        self.assertEqual(self.solution.divide(4, 3), 1)
        self.assertEqual(self.solution.divide(1, 2), 0)

        self.assertEqual(self.solution.divide(1024, 3), 341)
        self.assertEqual(self.solution.divide(2037, 3), 679)
        self.assertEqual(self.solution.divide(2**32, 6), 715827882)

        self.assertEqual(self.solution.divide(2147483648, 1), 2147483647)
        self.assertEqual(self.solution.divide(-2147483648, -1), 2147483647)
        self.assertEqual(self.solution.divide(-2147483648, 1), -2147483648)
