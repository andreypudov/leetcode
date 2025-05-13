import unittest

from problems.problem_20 import Solution as Solution1
from problems.problem_20_2 import Solution as Solution2
from problems.protocols.problem_20 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution_1 = Solution1()
        self.solution_2 = Solution2()

    def test_threeSumClosest(self):
        for solution in [self.solution_1, self.solution_2]:
            self.isValid(solution)

    def isValid(self, solution: Solution):
        self.assertTrue(solution.isValid("()"))
        self.assertTrue(solution.isValid("()[]{}"))
        self.assertFalse(solution.isValid("(]"))
        self.assertTrue(solution.isValid("([])"))
        self.assertFalse(solution.isValid("]"))
        self.assertFalse(solution.isValid("[]]"))
