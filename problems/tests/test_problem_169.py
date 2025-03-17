import unittest

from problems.problem_169 import Solution as Solution1
from problems.problem_169_2 import Solution as Solution2


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution_1 = Solution1()
        self.solution_2 = Solution2()

    def test_majorityElement(self):
        for solution in [self.solution_1, self.solution_2]:
            self.assertEqual(solution.majorityElement([3, 2, 3]), 3)
            self.assertEqual(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)
