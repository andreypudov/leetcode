import unittest

from problems.problem_16 import Solution as Solution1
from problems.problem_16_2 import Solution as Solution2
from problems.protocols.problem_16 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution_1 = Solution1()
        self.solution_2 = Solution2()

    def test_threeSumClosest(self):
        for solution in [self.solution_1, self.solution_2]:
            self.threeSumClosest(solution)

    def threeSumClosest(self, solution: Solution):
        self.assertEqual(solution.threeSumClosest([-1, 2, 1, -4], 1), 2)
        self.assertEqual(solution.threeSumClosest([0, 0, 0], 1), 0)
        self.assertEqual(
            solution.threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2),
            -2,
        )
        self.assertEqual(solution.threeSumClosest([1, 2, 7, 13], 12), 10)
