import unittest

from problems.problem_16 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_threeSumClosest(self):
        self.assertEqual(self.solution.threeSumClosest([-1, 2, 1, -4], 1), 2)
        self.assertEqual(self.solution.threeSumClosest([0, 0, 0], 1), 0)
        self.assertEqual(
            self.solution.threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2),
            -2,
        )
