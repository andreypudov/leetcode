import unittest

from problems.problem_15 import Solution as Solution1
from problems.problem_15_2 import Solution as Solution2


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution_1 = Solution1()
        self.solution_2 = Solution2()

    def test_threeSum(self):
        for solution in [self.solution_1, self.solution_2]:
            self.assertEqual(
                solution.threeSum([-1, 0, 1, 2, -1, -4]),
                [[-1, 0, 1], [-1, -1, 2]],
            )
            self.assertEqual(solution.threeSum([0, 1, 1]), [])
            self.assertEqual(solution.threeSum([0, 0, 0]), [[0, 0, 0]])
            self.assertEqual(solution.threeSum([1, 2, -2, -1]), [])
